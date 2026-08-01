# input() → input.* Functions
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'teki tek `input()` fonksiyonu v6'da namespace'e ayrıldı.

### Tam dönüşüm tablosu

| v5 | v6 |
|----|-----|
| `input(14, type=input.integer)` | `input.int(14)` |
| `input(2.0, type=input.float)` | `input.float(2.0)` |
| `input(true, type=input.bool)` | `input.bool(true)` |
| `input("D", type=input.resolution)` | `input.string("D")` |
| `input(close, type=input.source)` | `input.source(close)` |
| `input(color.red, type=input.color)` | `input.color(color.red)` |
| `input(timestamp("2024-01-01"), type=input.time)` | `input.time(timestamp("2024-01-01"))` |
| `input("Label", type=input.session)` | `input.session("0930-1730")` |
| `input("AAPL", type=input.symbol)` | `input.symbol("AAPL")` |

### Gerçek örnek

```pine
// ❌ v5
//@version=5
length = input(14, title="RSI Length", type=input.integer, minval=1, maxval=500)
src    = input(close, title="Source", type=input.source)
tf     = input("D", title="Timeframe", type=input.resolution)

// ✅ v6
//@version=6
int    length = input.int(14,    "RSI Length", minval=1, maxval=500)
float  src    = input.source(close, "Source")
string tf     = input.string("D",  "Timeframe",
                    options=["1","5","15","60","D","W","M"])
```

---

## EN | English

The single v5 `input()` function was split into namespaced functions in v6.

```pine
// ❌ v5
length = input(14, type=input.integer)

// ✅ v6
int length = input.int(14, "Length")
```
