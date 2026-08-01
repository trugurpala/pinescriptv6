from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Callable
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


SENSITIVE_QUERY_KEYS = {
    "access_token",
    "api_key",
    "key",
    "password",
    "secret",
    "token",
}


@dataclass(frozen=True)
class SourceLinkResult:
    source_id: str
    url: str
    status: str
    detail: str


def validate_source_url(url: object) -> str | None:
    if not isinstance(url, str):
        return "URL must be text"
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        return "URL must use HTTPS and include a host"
    if parsed.username or parsed.password:
        return "URL must not contain credentials"
    query_keys = {key.casefold() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    if query_keys & SENSITIVE_QUERY_KEYS:
        return "URL must not contain a sensitive query key"
    return None


class _SafeRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        problem = validate_source_url(newurl)
        if problem:
            raise URLError(f"unsafe redirect: {problem}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _fetch(url: str, timeout: int) -> int:
    request = Request(
        url,
        headers={
            "User-Agent": "Pine-Script-Agent-Kit/1 link-check (+https://github.com/trugurpala/pinescriptv6)",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.1",
        },
        method="GET",
    )
    opener = build_opener(_SafeRedirectHandler())
    with opener.open(request, timeout=timeout) as response:
        response.read(1)
        return int(response.status)


def check_source_links(
    sources: object,
    *,
    fetch: Callable[[str, int], int] = _fetch,
    timeout: int = 15,
) -> list[SourceLinkResult]:
    if not isinstance(sources, dict) or not isinstance(sources.get("sources"), list):
        return [SourceLinkResult("sources", "", "not-verified", "invalid source registry")]
    results: list[SourceLinkResult] = []
    for source in sorted(sources["sources"], key=lambda item: str(item.get("id", ""))):
        if not isinstance(source, dict):
            results.append(SourceLinkResult("unknown", "", "not-verified", "invalid source entry"))
            continue
        source_id = str(source.get("id", "unknown"))
        url = str(source.get("url", ""))
        problem = validate_source_url(url)
        if problem:
            results.append(SourceLinkResult(source_id, url, "not-verified", problem))
            continue
        try:
            status_code = fetch(url, timeout)
        except (HTTPError, URLError, OSError, TimeoutError) as error:
            results.append(SourceLinkResult(source_id, url, "not-verified", str(error)))
            continue
        status = "ok" if 200 <= status_code < 400 else "not-verified"
        results.append(SourceLinkResult(source_id, url, status, f"HTTP {status_code}"))
    return results
