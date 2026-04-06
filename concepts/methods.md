# Methods — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Built-in Methods
Array, matrix, map turlerinde nokta notasyonu ile cagrilir:

```pine
var arr = array.new<float>()
arr.push(close)       // array.push(arr, close) ile ayni
arr.shift()           // en eski elemani sil
float avg = arr.avg() // ortalama
```

## User-Defined Method
```pine
//@version=6
indicator("Method demo")

// Ozel method tanimla
method maintainQueue(array<float> arr, float value) =>
    arr.push(value)
    arr.shift()
    arr

var queue = array.new<float>(20, na)
queue.maintainQueue(close)
plot(queue.avg())
```

## Method Overloading
Ayni isimde farkli tipler icin birden fazla method tanimlanabilir.
