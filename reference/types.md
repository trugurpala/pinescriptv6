# Types — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Temel Tipler
int, float, bool, string, color

## Ozel Tipler
line, linefill, box, polyline, label, table
array<type>, matrix<type>, map<keyType, valueType>
chart.point

## Tip Niteleyicileri (Qualifiers)

| Qualifier | Anlam |
|-----------|-------|
| const | Derleme zamaninda sabit |
| simple | Script baslarken bir kere belirlenir |
| input | Kullanici tarafindan belirlenir |
| series | Her barda degisebilir (en esnek) |

Esneklik sirasi: const < simple < input < series

## Tip Donusum
```pine
int(3.7)       // 3
float(3)       // 3.0
str.tostring(3.14)  // "3.14"
str.toint("42")     // 42
str.tofloat("3.14") // 3.14
```

## na Kontrolu
```pine
na(close)           // true ise close na
nz(close, 0.0)      // close na ise 0.0 dondur
not na(myVar)       // na degilse
```
