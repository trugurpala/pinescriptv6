# General Fonksiyonlar — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## math.*
```pine
math.abs(x)           // mutlak deger
math.round(x)         // yuvarlama
math.round(x, digits) // ondalik basamak
math.floor(x)         // asagi yuvarla
math.ceil(x)          // yukari yuvarla
math.max(a, b, ...)   // maksimum
math.min(a, b, ...)   // minimum
math.pow(base, exp)   // us alma
math.sqrt(x)          // kare kok
math.log(x)           // dogal logaritma
math.log10(x)         // 10 tabaninda logaritma
math.sign(x)          // isaretini dondur (-1, 0, 1)
math.random(min, max) // rastgele sayi
```

## str.* (String)
```pine
str.tostring(val)            // her tipe string
str.tostring(val, "#.##")    // format ile
str.tostring(val, format.mintick)
str.tonumber(str)            // string to float
str.toint(str)               // string to int
str.length(str)              // uzunluk
str.upper(str)               // buyuk harf
str.lower(str)               // kucuk harf
str.contains(str, sub)       // icerir mi?
str.startswith(str, prefix)  // ile basliyor mu?
str.endswith(str, suffix)    // ile bitiyor mu?
str.replace(str, target, replacement)
str.split(str, separator)    // array<string> dondurur
str.format("{0} @ {1}", ticker, close)
```

## input.*
```pine
input.int(14, "RSI Length", minval=1, maxval=500)
input.float(2.0, "Multiplier", step=0.1)
input.bool(true, "Show Labels")
input.string("D", "Timeframe", options=["1","5","15","60","D","W"])
input.source(close, "Source")
input.color(color.red, "Color")
input.time(timestamp("2024-01-01"), "Start Date")
```

## alert()
```pine
alert("RSI asagi kesti!", alert.freq_once_per_bar)
alertcondition(condition, "Alert Name", "RSI gecisi")
```

## Zaman
```pine
timestamp("2024-01-01")           // Unix timestamp
timestamp("UTC+3", 2024, 1, 1, 9) // Timezone ile
year(time), month(time), dayofmonth(time)
hour(time), minute(time), second(time)
dayofweek(time)  // 1=Pazar, 2=Pazartesi...
```
