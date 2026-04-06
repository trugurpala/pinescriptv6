# Type System & Explicit Declarations
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v6'da tipler artık explicit olarak belirtilmesi **öneriliyor** (zorunlu değil ama iyi pratik).

```pine
// v5 — tip belirtmek opsiyoneldi
//@version=5
length = input(14, "Length")
myVar  = close * 2

// v6 — explicit tip önerilen pratik
//@version=6
int   length = input.int(14, "Length")
float myVar  = close * 2
```

### input() → input.*

```pine
// ❌ v5
length = input(14, "Length", type=input.integer)
src    = input(close, "Source", type=input.source)
tf     = input("D", "Timeframe", type=input.resolution)
col    = input(color.red, "Color", type=input.color)

// ✅ v6
int    length = input.int(14,    "Length")
float  src    = input.source(close, "Source")
string tf     = input.string("D",  "Timeframe")
color  col    = input.color(color.red, "Color")
```

### var ve varip — değişen yok, ama artık typed

```pine
//@version=6
var float   cumSum = 0.0     // tip explicit — önerilen
var int     barCount = 0
varip float tickSum = 0.0
```

---

## EN | English

In v6, explicit type declarations are **recommended** (not required, but good practice).

### input() → input.* functions

```pine
// ❌ v5
length = input(14, "Length", type=input.integer)

// ✅ v6
int length = input.int(14, "Length")
```
