# Collections — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## array<type>
```pine
// Olustur
var arr = array.new<float>(0)
var arr2 = array.new<float>(10, 0.0)  // 10 elemanli, hepsi 0

// Eleman ekle/sil
arr.push(close)           // sona ekle
arr.unshift(close)        // basa ekle
float last = arr.pop()    // sondan sil ve dondur
float first = arr.shift() // badan sil ve dondur

// Erisim
arr.get(0)                // 0. eleman
arr.set(0, close)         // 0. elemani guncelle
arr.size()                // eleman sayisi

// Hesaplama
arr.avg()                 // ortalama
arr.max()                 // maksimum
arr.min()                 // minimum
arr.sum()                 // toplam
arr.stdev()               // standart sapma

// Diger
arr.sort()                // sirala
arr.reverse()             // ters cevir
arr.slice(from, to)       // dilim
arr.includes(val)         // icerir mi?
arr.indexof(val)          // ilk index
arr.clear()               // temizle
```

## map<keyType, valueType>
```pine
var myMap = map.new<string, float>()
myMap.put("rsi", ta.rsi(close, 14))
myMap.put("ema", ta.ema(close, 20))

float rsiVal = myMap.get("rsi")
myMap.remove("rsi")
myMap.size()
myMap.keys()   // array<string> dondurur
myMap.values() // array<float> dondurur
```

## matrix<type>
```pine
var mat = matrix.new<float>(3, 3, 0.0)  // 3x3, hepsi 0
mat.set(0, 0, close)    // satir 0, sutun 0
mat.get(0, 0)           // deger al
mat.rows()              // satir sayisi
mat.columns()           // sutun sayisi
mat.row(0)              // 0. satiri array olarak al
matrix.mult(mat1, mat2) // matris carpimi
```
