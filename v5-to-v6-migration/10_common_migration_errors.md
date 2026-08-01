# Common Migration Errors — v5 → v6
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Bu hatalar v5 kodunu v6'ya taşırken en sık karşılaşılan sorunlardır.

---

### 1. "Undeclared identifier 'study'"

```pine
// ❌ Hata
//@version=6
study("My Indicator", overlay=true)  // study() v6'da yok

// ✅ Düzeltme
//@version=6
indicator("My Indicator", overlay=true)
```

---

### 2. "Undeclared identifier 'security'"

```pine
// ❌ Hata
//@version=6
htf = security(syminfo.tickerid, "D", close)  // security() v6'da yok

// ✅ Düzeltme
//@version=6
htf = request.security(syminfo.tickerid, "D", close)
```

---

### 3. "Cannot call 'input' with these arguments"

```pine
// ❌ Hata
//@version=6
length = input(14, type=input.integer)  // eski syntax

// ✅ Düzeltme
//@version=6
int length = input.int(14, "Length")
```

---

### 4. "array.new_float is not defined"

```pine
// ❌ Hata
//@version=6
arr = array.new_float(0)  // v5 syntax

// ✅ Düzeltme
//@version=6
var arr = array.new<float>(0)
```

---

### 5. "Cannot use 'series string' as argument"

```pine
// ❌ Hata — timeframe değişken olamaz
//@version=6
string tf = close > open ? "D" : "W"  // series string
htf = request.security(syminfo.tickerid, tf, close)  // HATA

// ✅ Düzeltme — input ile sabit yap
//@version=6
string tfInput = input.string("D", "TF", options=["D","W","M"])
htf = request.security(syminfo.tickerid, tfInput, close)
```

---

### 6. "Pine Script v6 requires //@version=6"

```pine
// ❌ Hata — version eksik
indicator("Demo")

// ✅ Düzeltme
//@version=6
indicator("Demo")
```

---

### 7. plot() içinde series string kullanımı

```pine
// ❌ Hata
//@version=6
title_str = close > open ? "Bull" : "Bear"
plot(close, title=title_str)  // title series olamaz

// ✅ Düzeltme — sabit string kullan
//@version=6
plot(close, title="Price")
```

---

## EN | English

These are the most common errors when migrating v5 code to v6.

| Error | Cause | Fix |
|-------|-------|-----|
| `'study' undefined` | `study()` removed | Use `indicator()` |
| `'security' undefined` | `security()` removed | Use `request.security()` |
| `input()` argument error | Old syntax | Use `input.int()`, `input.float()` etc. |
| `array.new_float` undefined | Old syntax | Use `array.new<float>()` |
| Series string error | Dynamic string in function | Use `input.string()` |
