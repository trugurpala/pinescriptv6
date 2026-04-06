# Yaygin Hatalar — Pine Script v6
> Kaynak: trugurpala/pinescriptv6 | mail@ugurpala.com

## 1. "Cannot use 'series' type as argument"

**Sebep:** Fonksiyon 'simple' veya 'const' bekliyor, sen 'series' veriyorsun.

```pine
// YANLIS
length = close > open ? 14 : 20  // series int
rsi = ta.rsi(close, length)       // HATA: length series olamaz

// DOGRU
length = 14  // simple int
rsi = ta.rsi(close, length)
```

## 2. "max_bars_back" Hatasi

**Sebep:** Gecmis veriye yeterli buffer ayrılmamis.

```pine
// YANLIS — realtime barda hata verir
myVar = close[barstate.ishistory ? 100 : 500]

// DOGRU
max_bars_back(close, 500)
myVar = close[barstate.ishistory ? 100 : 500]

// VEYA indicator/strategy parametresinde
indicator("Demo", max_bars_back=500)
```

## 3. "Undeclared identifier"

**Sebep:** Degisken tanimlanmadan kullaniliyor veya yanlis scope'ta.

```pine
// YANLIS
if condition
    myVal = close * 2

plot(myVal)  // HATA: myVal if blogu disinda tanimsiz

// DOGRU
myVal = condition ? close * 2 : na
plot(myVal)
```

## 4. Memory Limit Asimi

**Sebep:** Cok fazla array/collection veri tutuluyor.

**Cozum:** 
- request.security() cagrilarini minimize et
- Array'leri gereksiz yere buyutme
- Collection'lari sadece gerekli barlarda dondur

## 5. "Loop is too long" / "Script could not be translated"

**Sebep:** For/while loop cok uzun surdü.

**Cozum:** Loop icindeki islemi optimize et, gereksiz iterasyonlari azalt.

## 6. Repainting Sorunu

**Sebep:** request.security ile gelecek veriye bakilıyor.

```pine
// REPAINTING YAPAN (yanlis)
htf_close = request.security(syminfo.tickerid, "D", close)

// REPAINTING YAPMAYAN (dogru — kapanan cubuk)
htf_close = request.security(syminfo.tickerid, "D", close[1])
// VEYA
htf_close = request.security(syminfo.tickerid, "D", close, barmerge.lookahead_off)
```
