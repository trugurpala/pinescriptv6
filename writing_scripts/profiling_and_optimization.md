# Profiling ve Optimizasyon - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## Pine Profiler Nasil Acilir
Pine Editor > sag ust kosedeki ... menusunden "Profile script" sec.
Her satirin millisaniye bazinda maliyet raporu gosterilir.

## Optimizasyon Kurallari

### 1. request.security Cagrilerini Minimize Et
```pine
// YANLIS - 3 ayri cagri
dHigh  = request.security(syminfo.tickerid, "D", high)
dLow   = request.security(syminfo.tickerid, "D", low)
dClose = request.security(syminfo.tickerid, "D", close)

// DOGRU - tek cagri, tuple
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
                                          [high, low, close])
```

### 2. Hesaplamayi if Disina Al
```pine
// YANLIS - gereksiz kosullu hesaplama
if condition
    val = ta.ema(close, 200)  // Her barda degil ama yine de pahali

// DOGRU - once hesapla, sonra kullan
val = ta.ema(close, 200)
if condition
    doSomething(val)
```

### 3. Drawing Nesnelerini Limitli Tut
```pine
// YANLIS - sinırsız label birikimi
if condition
    label.new(bar_index, high, "Al")

// DOGRU - max 50 label tut
if condition
    label.new(bar_index, high, "Al")
    if label.all.size() > 50
        label.delete(label.all.first())
```

### 4. Sliding Window Icin var + push/shift
```pine
// DOGRU - sabit boyutlu sliding window
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()  // Boyut 20'de sabit kalir
```

### 5. barstate.islast ile Son Barda Yapilacak Islemler
```pine
// Pahalı hesaplamalar sadece son barda yap
if barstate.islast
    // table guncelleme, kompleks etiketler vs.
```

### 6. max_bars_back Gereksiz Artirma
```pine
// Sadece ihtiyac kadar ayarla
max_bars_back(close, 200)  // Tum script icin 5000 YERINE spesifik degisken
```
