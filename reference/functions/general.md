# General — math / str / input / alert
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## math.*
```pine
math.abs(x)               // mutlak değer / absolute value
math.round(x)             // en yakın tam sayı / nearest integer
math.round(x, decimals)   // ondalık basamak / decimal places
math.floor(x)             // aşağı yuvarla / floor
math.ceil(x)              // yukarı yuvarla / ceiling
math.max(a, b, c...)      // maksimum
math.min(a, b, c...)      // minimum
math.pow(base, exp)       // üs / power
math.sqrt(x)              // kare kök / square root
math.log(x)               // doğal logaritma / natural log
math.log10(x)             // log base 10
math.sign(x)              // işaret / sign: -1, 0 or 1
math.random(min, max)     // rastgele / random
math.pi                   // 3.14159...
math.phi                  // altın oran / golden ratio
```

## str.* — String
```pine
str.tostring(val)                    // her şey → string / anything to string
str.tostring(3.14, "#.##")           // formatlı / formatted
str.tostring(close, format.mintick)  // mintick formatı
str.tonumber(str)                    // string → float
str.toint(str)                       // string → int
str.length(str)
str.upper(str)                       // büyük harf / uppercase
str.lower(str)                       // küçük harf / lowercase
str.trim(str)                        // boşlukları temizle / trim whitespace
str.contains(str, sub)               // içeriyor mu? / contains?
str.startswith(str, prefix)
str.endswith(str, suffix)
str.replace(str, target, rep)        // ilk bulduğu / first occurrence
str.replace_all(str, target, rep)    // hepsini / all occurrences
str.split(str, sep)                  // array<string> döndürür
str.substring(str, from, to)
str.format("{0} @ {1}", syminfo.ticker, close)
```

## input.*
```pine
input.int(14,    "RSI Periyodu",   minval=1, maxval=500)
input.float(2.0, "ATR Çarpan",    step=0.1)
input.bool(true, "Sinyal Göster")
input.string("D", "Timeframe",    options=["1","5","15","60","D","W","M"])
input.source(close, "Kaynak")
input.color(color.red, "Renk")
input.time(timestamp("2024-01-01"), "Başlangıç")
```

## alert()
```pine
// Dinamik alert — kod içinde tetiklenir
alert("RSI aşağı kesti: " + str.tostring(rsi), alert.freq_once_per_bar)
alert("Fiyat: " + str.tostring(close),         alert.freq_once_per_bar_close)
alert(msg,                                      alert.freq_all)

// Statik alert — kullanıcı TradingView'da tetikler
alertcondition(buySignal,  "Al Sinyali",  "Al: {{close}}")
alertcondition(sellSignal, "Sat Sinyali", "Sat: {{close}}")
```

## Zaman / Time
```pine
timestamp("2024-01-01")
timestamp("UTC+3", 2024, 1, 1, 9, 30, 0)

year(time), month(time), dayofmonth(time)
hour(time), minute(time), second(time)
dayofweek(time)   // 1=Pazar/Sunday ... 7=Cumartesi/Saturday
timenow           // şu anki Unix ms

// Seans kontrolü / Session check
isSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
```
