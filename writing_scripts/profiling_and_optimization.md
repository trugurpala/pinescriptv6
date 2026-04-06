# Profiling & Optimization
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Pine Profiler

Pine Editor → `...` menüsü → **Profile script**
Her satırın ms bazında maliyeti gösterilir.

### Optimizasyon Kuralları

**1. request.security — Çağrıları Birleştir**

```pine
// ❌ 3 ayrı çağrı
dHigh  = request.security(syminfo.tickerid, "D", high)
dLow   = request.security(syminfo.tickerid, "D", low)
dClose = request.security(syminfo.tickerid, "D", close)

// ✅ Tek çağrı, tuple
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D", [high, low, close])
```

**2. Hesaplamayı if Dışına Al**

```pine
// ❌ if içinde pahalı hesaplama
if condition
    val = ta.ema(close, 200)

// ✅ Her barda hesapla, sadece kullanımı koşulla
val = ta.ema(close, 200)
if condition
    doSomething(val)
```

**3. Sliding Window — Sabit Boyut**

```pine
// ✅ Push + shift ile boyut sabit kalır
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()
```

**4. Drawing — Biriken Nesneleri Temizle**

```pine
// ❌ Sonsuz label birikir
if condition
    label.new(bar_index, high, "sinyal")

// ✅ Max 50 tut
if condition
    label.new(bar_index, high, "sinyal")
    if label.all.size() > 50
        label.delete(label.all.first())
```

**5. Son Bar İşlemleri**

```pine
// Pahalı hesaplamalar sadece son barda
if barstate.islast
    // tablo güncelleme, kompleks label vs.
```

---

## EN | English

### Pine Profiler

Pine Editor → `...` menu → **Profile script**
Shows per-line cost in milliseconds.

### Optimization Rules

**1. request.security — Combine Calls**

```pine
// ❌ 3 separate calls
dHigh  = request.security(syminfo.tickerid, "D", high)
dLow   = request.security(syminfo.tickerid, "D", low)
dClose = request.security(syminfo.tickerid, "D", close)

// ✅ Single call, tuple
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D", [high, low, close])
```

**2. Move Calculations Outside if**

```pine
// ❌ Expensive calc inside if
if condition
    val = ta.ema(close, 200)

// ✅ Calculate every bar, conditionally use
val = ta.ema(close, 200)
if condition
    doSomething(val)
```

**3. Sliding Window — Fixed Size**

```pine
// ✅ Push + shift keeps size constant
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()
```

**4. Drawing — Clean Up Accumulating Objects**

```pine
// ❌ Labels accumulate forever
if condition
    label.new(bar_index, high, "signal")

// ✅ Keep max 50
if condition
    label.new(bar_index, high, "signal")
    if label.all.size() > 50
        label.delete(label.all.first())
```

**5. Last-Bar-Only Operations**

```pine
// Expensive work only on the last bar
if barstate.islast
    // table updates, complex labels, etc.
```
