# Limitations
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Hesaplama

| Limit | Değer |
|-------|-------|
| `max_bars_back` varsayılan | 300 |
| `max_bars_back` maksimum | 5000 |
| Maksimum değişken / fonksiyon | 1000 |
| İç içe fonksiyon derinliği | 500 |

### Drawing Limitleri

| Nesne | Varsayılan | Maksimum |
|-------|-----------|----------|
| `line` | 50 | 500 |
| `label` | 50 | 500 |
| `box` | 50 | 500 |
| `polyline` | 100 | 100 |

Artırmak için:

```pine
indicator("Demo",
    max_lines_count  = 500,
    max_labels_count = 500,
    max_boxes_count  = 500)
```

### request.* Limitleri

| Fonksiyon | Limit |
|-----------|-------|
| `request.security()` | 40 / script |
| `request.security_lower_tf()` | 40 / script |
| `request.financial()` | 40 / script |

### Koleksiyon Limitleri

| Limit | Değer |
|-------|-------|
| Eleman / koleksiyon | 100.000 |
| Koleksiyon / script | 1.000 |

### Hata Yönetimi

```pine
// Özel runtime hatası fırlat
if length < 1
    runtime.error("length en az 1 olmalı: " + str.tostring(length))

// na-safe erişim
safeVal = array.size(myArr) > 0 ? myArr.get(0) : 0.0
```

---

## EN | English

### Computation

| Limit | Value |
|-------|-------|
| `max_bars_back` default | 300 |
| `max_bars_back` maximum | 5000 |
| Max variables / function | 1000 |
| Nested function depth | 500 |

### Drawing Limits

| Object | Default | Maximum |
|--------|---------|---------|
| `line` | 50 | 500 |
| `label` | 50 | 500 |
| `box` | 50 | 500 |
| `polyline` | 100 | 100 |

To increase:

```pine
indicator("Demo",
    max_lines_count  = 500,
    max_labels_count = 500,
    max_boxes_count  = 500)
```

### request.* Limits

| Function | Limit |
|----------|-------|
| `request.security()` | 40 / script |
| `request.security_lower_tf()` | 40 / script |
| `request.financial()` | 40 / script |

### Collection Limits

| Limit | Value |
|-------|-------|
| Elements / collection | 100,000 |
| Collections / script | 1,000 |

### Error Handling

```pine
// Throw custom runtime error
if length < 1
    runtime.error("length must be at least 1: " + str.tostring(length))

// na-safe access
safeVal = array.size(myArr) > 0 ? myArr.get(0) : 0.0
```
