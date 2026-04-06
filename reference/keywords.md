# Keywords — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Kontrol Akisi

```pine
// if / else if / else
if close > open
    strategy.entry("Long", strategy.long)
else if close < open
    strategy.entry("Short", strategy.short)

// switch
switch timeframe.period
    "D"  => bgcolor(color.new(color.blue, 90))
    "W"  => bgcolor(color.new(color.green, 90))
    => bgcolor(na)

// for
for i = 0 to 9
    sum += close[i]

// for..in (array)
for [i, val] in myArray
    sum += val

// while
while condition
    // ...
```

## var ve varip
```pine
var float cumSum = 0.0    // kalici, bir kere baslatilir
varip int ticks = 0       // rollback'e direncli
```

## Fonksiyon Tanimlama
```pine
// Normal fonksiyon
myFunc(x, y) =>
    x * y + close

// Method
method myMethod(array<float> arr, float val) =>
    arr.push(val)
    arr
```

## import / export (library)
```pine
import username/libraryName/1 as lib
export myFunc(float x) => x * 2
```
