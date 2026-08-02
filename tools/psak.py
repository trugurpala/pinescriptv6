from __future__ import annotations

import argparse
import json
from pathlib import Path
from collections.abc import Sequence

from psaklib.examples import build_manifest
from psaklib.links import check_source_links
from psaklib.rendering import check_outputs, write_outputs
from psaklib.validation import load_json, validate_critical_files, validate_repository


ROOT = Path(__file__).resolve().parents[1]
LOCAL_VALIDATION_LIMITS = (
    "TradingView compilation",
    "Runtime/chart behavior",
    "Repaint behavior",
    "Alert delivery",
    "Market data",
    "Profitability",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="psak", description="Validate and render Pine Script Agent Kit data."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate canonical repository data")
    render = subparsers.add_parser("render", help="render deterministic adapters")
    render.add_argument("--check", action="store_true", help="check for drift")
    subparsers.add_parser("check", help="run all offline quality gates")
    subparsers.add_parser("links", help="check registered source links")
    manifest = subparsers.add_parser("manifest", help="build the Pine manifest")
    manifest.add_argument("--write", action="store_true", help="write the manifest")
    return parser


def _print_issues() -> int:
    issues = validate_repository(ROOT)
    if not issues:
        print("OK: repository data is valid")
        _print_local_validation_limits()
        return 0
    for issue in issues:
        print(f"ERROR {issue.code} {issue.path}: {issue.message}")
    return 1


def _print_local_validation_limits() -> None:
    for limit in LOCAL_VALIDATION_LIMITS:
        print(f"NOT CHECKED: {limit}")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "validate":
        return _print_issues()
    if args.command == "manifest":
        manifest = build_manifest(ROOT)
        content = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
        if args.write:
            path = ROOT / "examples/manifest.json"
            path.write_text(content, encoding="utf-8", newline="\n")
            print(f"WROTE {path.relative_to(ROOT).as_posix()}")
        else:
            print(content, end="")
        return 0
    if args.command == "render":
        if args.check:
            issues = check_outputs(ROOT)
            if issues:
                for issue in issues:
                    print(f"ERROR {issue.code} {issue.path}: {issue.message}")
                return 1
            print("OK: generated outputs are current")
            return 0
        for path in write_outputs(ROOT):
            print(f"WROTE {path.relative_to(ROOT).as_posix()}")
        return 0
    if args.command == "check":
        issues = validate_repository(ROOT)
        issues.extend(validate_critical_files(ROOT))
        issues.extend(check_outputs(ROOT))
        if issues:
            for issue in sorted(set(issues)):
                print(f"ERROR {issue.code} {issue.path}: {issue.message}")
            return 1
        print("OK: all offline checks passed")
        _print_local_validation_limits()
        return 0
    if args.command == "links":
        results = check_source_links(load_json(ROOT / "knowledge/sources.json"))
        for result in results:
            prefix = "OK" if result.status == "ok" else "NOT VERIFIED"
            print(f"{prefix} {result.source_id} {result.url}: {result.detail}")
        return 0 if results and all(result.status == "ok" for result in results) else 1
    print(f"ERROR command-not-ready: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
