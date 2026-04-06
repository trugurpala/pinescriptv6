# Collections — array / map / matrix
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## array<type>

### Oluşturma / Create
```pine
var arr  = array.new<float>(0)          // boş / empty
var arr2 = array.new<float>(10, 0.0)    // 10 eleman, hepsi 0 / 10 elements, all 0
var arr3 = array.new<int>(5, na)
```

### Eleman İşlemleri / Element Operations
```pine
arr.push(close)              // sona ekle / add to end
arr.unshift(close)           // başa ekle / add to start
arr.insert(2, close)         // index 2'ye ekle / insert at index 2
float last  = arr.pop()      // sondan sil / remove from end
float first = arr.shift()    // baştan sil / remove from start
arr.remove(2)                // index 2'yi sil / remove at index 2
arr.clear()                  // hepsini temizle / clear all
```

### Erişim / Access
```pine
arr.get(0)                   // 0. eleman
arr.set(0, close)            // güncelle / update
arr.size()                   // eleman sayısı / element count
arr.first()                  // ilk / first
arr.last()                   // son / last
```

### Hesaplama / Calculation
```pine
arr.avg()     arr.max()     arr.min()
arr.sum()     arr.stdev()   arr.median()   arr.variance()
```

### Diger / Other
```pine
arr.sort()                        // küçükten büyüğe / ascending
arr.sort(order.descending)        // büyükten küçüğe / descending
arr.reverse()
arr.slice(from, to)               // dilim / slice (yeni array / new array)
arr.copy()
arr.includes(val)                 // var mı? / contains?
arr.indexof(val)                  // ilk index (-1 yoksa)
arr.join(", ")                    // string'e / to string
```

### Sliding Window Örneği / Example
```pine
//@version=6
indicator("Rolling Stats")
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()    // boyut 20'de sabit / size stays at 20
plot(arr.avg(),   "Ortalama / Avg",  color.blue)
plot(arr.stdev(), "StDev", color.orange)
```

---

## map<keyType, valueType>
```pine
var m = map.new<string, float>()
m.put("rsi", ta.rsi(close, 14))
m.put("atr", ta.atr(14))

float rsiVal = m.get("rsi")    // değer al / get value
m.remove("rsi")                // sil / remove
bool hasKey = m.contains("atr") // var mı?
int  sz     = m.size()
array<string> keys = m.keys()
array<float>  vals = m.values()
```

---

## matrix<type>
```pine
var mat = matrix.new<float>(3, 3, 0.0)  // 3x3, hepsi 0
mat.set(0, 0, close)    // (satır, sütun, değer) / (row, col, value)
float val = mat.get(0, 0)
int rows  = mat.rows()
int cols  = mat.columns()
array<float> row0 = mat.row(0)
matrix.mult(mat1, mat2)          // matris çarpımı / matrix multiplication
mat.transpose()                  // devrik / transpose
```
