# General Fonksiyonlar - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## math.*
```pine
math.abs(x)
math.round(x)
math.round(x, decimals)
math.floor(x), math.ceil(x)
math.max(a, b, c...), math.min(a, b, c...)
math.pow(base, exp)
math.sqrt(x)
math.log(x), math.log10(x)
math.sign(x)
math.random(min, max)
math.pi, math.phi
```

## str.*
```pine
str.tostring(val)
str.tostring(3.14, "#.##")
str.tostring(close, format.mintick)
str.tonumber(str), str.toint(str)
str.length(str)
str.upper(str), str.lower(str), str.trim(str)
str.contains(str, sub)
str.startswith(str, prefix)
str.endswith(str, suffix)
str.replace(str, target, rep)
str.replace_all(str, target, rep)
str.split(str, sep)
str.substring(str, from, to)
str.format("{0} @ {1}", syminfo.ticker, close)
```

## input.*
```pine
input.int(14, "Periyod", minval=1, maxval=500)
input.float(2.0, "Carpan", step=0.1)
input.bool(true, "Aktif")
input.string("D", "TF", options=["1","5","15","60","D","W","M"])
input.source(close, "Kaynak")
input.color(color.red, "Renk")
input.time(timestamp("2024-01-01"), "Baslangic")
```

## alert()
```pine
alert("Sinyal!", alert.freq_once_per_bar)
alert("Sinyal!", alert.freq_once_per_bar_close)
alert("Sinyal!", alert.freq_all)
alertcondition(buySignal, "Al Sinyali", "Al: {{close}}")
```

## Zaman
```pine
timestamp("2024-01-01")
year(time), month(time), dayofmonth(time)
hour(time), minute(time), second(time)
dayofweek(time)  // 1=Paz 2=Pzt 7=Cmt
timenow
isInSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
```
