# Collections - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## array<type>
```pine
var arr = array.new<float>(0)
var arr2 = array.new<float>(10, 0.0)

arr.push(close)
arr.unshift(close)
float last = arr.pop()
float first = arr.shift()
arr.clear()

arr.get(0)
arr.set(0, close)
arr.size()
arr.first(), arr.last()

arr.avg(), arr.max(), arr.min()
arr.sum(), arr.stdev(), arr.median()

arr.sort()
arr.sort(order.descending)
arr.reverse()
arr.slice(from, to)
arr.includes(val)
arr.indexof(val)
```

## map<keyType, valueType>
```pine
var m = map.new<string, float>()
m.put("rsi", ta.rsi(close, 14))
float v = m.get("rsi")
m.remove("rsi")
m.contains("ema")
m.keys()    // array<string>
m.values()  // array<float>
```

## matrix<type>
```pine
var mat = matrix.new<float>(3, 3, 0.0)
mat.set(0, 0, close)
mat.get(0, 0)
mat.rows(), mat.columns()
matrix.mult(mat1, mat2)
mat.transpose()
```

## Sliding Window Ornegi
```pine
//@version=6
indicator("Rolling Stats")
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()
plot(arr.avg(), "Ort")
plot(arr.stdev(), "StDev")
```
