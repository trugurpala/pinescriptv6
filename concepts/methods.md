# Methods
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Built-in Method'lar

Nokta notasyonu ile — `array`, `matrix`, `map` türlerinde çalışır.

```pine
var arr = array.new<float>()
arr.push(close)         // array.push(arr, close) ile aynı
arr.shift()             // en eski elemanı sil
float avg = arr.avg()   // ortalama
```

### Kullanıcı Tanımlı Method

```pine
//@version=6
indicator("Method demo")

// Sabit boyutlu queue tutar
method maintainQueue(array<float> arr, float value) =>
    arr.push(value)
    arr.shift()
    arr

var queue = array.new<float>(20, na)
queue.maintainQueue(close)
plot(queue.avg(), "Rolling Avg")
```

### Method Overloading

Aynı isimde, farklı tipler için birden fazla method tanımlanabilir.

```pine
method describe(int val) =>
    "int: " + str.tostring(val)

method describe(float val) =>
    "float: " + str.tostring(val, "#.##")
```

---

## EN | English

### Built-in Methods

Dot notation — works on `array`, `matrix`, `map` types.

```pine
var arr = array.new<float>()
arr.push(close)         // same as array.push(arr, close)
arr.shift()             // remove oldest element
float avg = arr.avg()   // average
```

### User-Defined Method

```pine
//@version=6
indicator("Method demo")

// Maintains a fixed-size queue
method maintainQueue(array<float> arr, float value) =>
    arr.push(value)
    arr.shift()
    arr

var queue = array.new<float>(20, na)
queue.maintainQueue(close)
plot(queue.avg(), "Rolling Avg")
```

### Method Overloading

Multiple methods with the same name for different types.

```pine
method describe(int val) =>
    "int: " + str.tostring(val)

method describe(float val) =>
    "float: " + str.tostring(val, "#.##")
```
