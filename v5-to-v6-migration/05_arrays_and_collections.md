# Arrays, Maps & Matrices
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### array — syntax değişti

```pine
// ❌ v5
myArr = array.new_float(0)
array.push(myArr, close)
float val = array.get(myArr, 0)

// ✅ v6 — method syntax (nokta notasyonu)
var myArr = array.new<float>(0)
myArr.push(close)
float val = myArr.get(0)
```

### map — v6'da yeni

```pine
// ✅ v6 only
var m = map.new<string, float>()
m.put("rsi", ta.rsi(close, 14))
float rsiVal = m.get("rsi")
```

### matrix — v6'da yeni

```pine
// ✅ v6 only
var mat = matrix.new<float>(3, 3, 0.0)
mat.set(0, 0, close)
float val = mat.get(0, 0)
```

### Sliding window — v6 best practice

```pine
//@version=6
indicator("Rolling Stats")
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()   // boyutu 20'de sabit tut
plot(arr.avg(), "Avg")
plot(arr.stdev(), "StDev")
```

---

## EN | English

### array — method syntax in v6

```pine
// ❌ v5
myArr = array.new_float(0)
array.push(myArr, close)

// ✅ v6
var myArr = array.new<float>(0)
myArr.push(close)
```

### map and matrix are new in v6

```pine
// ✅ v6 only
var m = map.new<string, float>()
m.put("key", 42.0)
```
