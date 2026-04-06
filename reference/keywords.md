# Keywords
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Kontrol Akışı / Control Flow

```pine
// if / else if / else
if close > open
    strategy.entry("Long", strategy.long)
else if close < open
    strategy.entry("Short", strategy.short)
else
    strategy.close_all()

// switch
switch timeframe.period
    "D" => bgcolor(color.new(color.blue, 90))
    "W" => bgcolor(color.new(color.green, 90))
    => bgcolor(na)  // default

// for
for i = 0 to 9
    sum += close[i]

// for..in — array üzerinde
for [i, val] in myArray
    total += val

// while
while condition
    counter += 1
```

### Değişken Bildirimi

```pine
var float cumSum = 0.0    // kalıcı — bir kere başlatılır
varip int ticks = 0       // rollback'e dirençli

// Tip opsiyoneldir — Pine çıkarabilir
myVar = close * 2
```

### Fonksiyon Tanımı

```pine
// Normal fonksiyon
myFunc(float x, int len) =>
    ta.ema(x, len) * 2

// Method
method myMethod(array<float> arr, float val) =>
    arr.push(val)
    arr
```

### import / export — Library

```pine
// Kullanım
import username/libraryName/1 as lib
result = lib.myFunction(close)

// Tanım (library script içinde)
export myFunc(float x) =>
    x * 2
```

---

## EN | English

### Control Flow

```pine
// if / else if / else
if close > open
    strategy.entry("Long", strategy.long)
else if close < open
    strategy.entry("Short", strategy.short)
else
    strategy.close_all()

// switch
switch timeframe.period
    "D" => bgcolor(color.new(color.blue, 90))
    "W" => bgcolor(color.new(color.green, 90))
    => bgcolor(na)  // default

// for
for i = 0 to 9
    sum += close[i]

// for..in — over array
for [i, val] in myArray
    total += val
```

### Variable Declaration

```pine
var float cumSum = 0.0    // persistent — initialized once
varip int ticks = 0       // rollback-resistant

// Type is optional — Pine can infer
myVar = close * 2
```

### Function Definition

```pine
// Regular function
myFunc(float x, int len) =>
    ta.ema(x, len) * 2

// Method
method myMethod(array<float> arr, float val) =>
    arr.push(val)
    arr
```
