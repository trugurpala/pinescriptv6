# security() → request.security()
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'te `security()` doğrudan çağrılırdı. v6'da `request.security()` oldu.

```pine
// ❌ v5
//@version=5
dailyClose = security(syminfo.tickerid, "D", close)

// ✅ v6
//@version=6
dailyClose = request.security(syminfo.tickerid, "D", close)
```

### Repainting — v5 vs v6

```pine
// ❌ v5 — repainting yapabilir
htf = security(syminfo.tickerid, "D", close)

// ✅ v6 — kapanmış bar, güvenli
htf = request.security(syminfo.tickerid, "D", close[1],
                        lookahead=barmerge.lookahead_on)
```

### Çoklu değer — tuple (v6 yeni özellik)

```pine
// ❌ v5 — ayrı ayrı çağrı
dHigh  = security(syminfo.tickerid, "D", high)
dLow   = security(syminfo.tickerid, "D", low)
dClose = security(syminfo.tickerid, "D", close)

// ✅ v6 — tek çağrı, tuple
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
                            [high[1], low[1], close[1]],
                            lookahead=barmerge.lookahead_on)
```

---

## EN | English

In v5, `security()` was called directly. In v6, it became `request.security()`.

```pine
// ❌ v5
dailyClose = security(syminfo.tickerid, "D", close)

// ✅ v6
dailyClose = request.security(syminfo.tickerid, "D", close)
```

### Key change: use tuple for multiple values

```pine
// ✅ v6 — single call, no repainting
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
                            [high[1], low[1], close[1]],
                            lookahead=barmerge.lookahead_on)
```
