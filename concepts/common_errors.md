# Common Errors
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### 1. "Cannot use 'series' type as argument"

Fonksiyon `simple` veya `const` bekliyor ama `series` veriliyor.

```pine
// ❌ Yanlış — length series olamaz
length = close > open ? 14 : 20
rsi = ta.rsi(close, length)

// ✅ Doğru — input veya sabit kullan
int length = input.int(14, "Length")
rsi = ta.rsi(close, length)
```

### 2. "max_bars_back" Hatası

Geçmiş veriye yeterli buffer ayrılmamış.

```pine
// ❌ Hata verebilir
myVar = close[500]

// ✅ Buffer'ı artır
max_bars_back(close, 500)
myVar = close[500]

// veya indicator parametresinde
indicator("Demo", max_bars_back=500)
```

### 3. "Undeclared identifier"

Değişken tanımlandığı scope dışında kullanılıyor.

```pine
// ❌ if bloğu dışında tanımsız
if condition
    myVal = close * 2
plot(myVal)  // HATA

// ✅ Dışarıda tanımla
myVal = condition ? close * 2 : na
plot(myVal)
```

### 4. Repainting

`request.security()` canlı bar verisini kullanıyor.

```pine
// ❌ Repainting yapabilir
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Kapanmış bar kullan
htf = request.security(syminfo.tickerid, "D", close[1])
```

### 5. "Loop is too long"

For/while döngüsü çok uzun sürdü.

**Çözüm:** Döngü içindeki işlemi optimize et, gereksiz iterasyonları azalt.

---

## EN | English

### 1. "Cannot use 'series' type as argument"

Function expects `simple` or `const` but received `series`.

```pine
// ❌ Wrong — length cannot be series
length = close > open ? 14 : 20
rsi = ta.rsi(close, length)

// ✅ Correct — use input or constant
int length = input.int(14, "Length")
rsi = ta.rsi(close, length)
```

### 2. "max_bars_back" Error

Not enough historical buffer allocated.

```pine
// ❌ May error
myVar = close[500]

// ✅ Increase buffer
max_bars_back(close, 500)
myVar = close[500]
```

### 3. "Undeclared identifier"

Variable used outside its declaring scope.

```pine
// ❌ Undefined outside if block
if condition
    myVal = close * 2
plot(myVal)  // ERROR

// ✅ Declare outside
myVal = condition ? close * 2 : na
plot(myVal)
```

### 4. Repainting

`request.security()` using live bar data.

```pine
// ❌ May repaint
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Use confirmed bar
htf = request.security(syminfo.tickerid, "D", close[1])
```

### 5. "Loop is too long"

For/while loop ran too long.

**Fix:** Optimize the loop body, reduce unnecessary iterations.
