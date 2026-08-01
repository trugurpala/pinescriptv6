# study() → indicator()
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Pine Script v6'da `study()` kaldırıldı. Yerine `indicator()` kullanılır.

```pine
// ❌ v5
//@version=5
study("My Indicator", overlay=true, max_bars_back=500)

// ✅ v6
//@version=6
indicator("My Indicator", overlay=true, max_bars_back=500)
```

### Parametreler aynı mı?

Evet — tüm `study()` parametreleri `indicator()`'de geçerlidir:

```pine
//@version=6
indicator("Demo",
    overlay             = true,
    scale               = scale.right,
    max_bars_back       = 500,
    max_lines_count     = 200,
    max_labels_count    = 200,
    max_boxes_count     = 200,
    shorttitle          = "Demo",
    format              = format.price,
    precision           = 2)
```

### Adım adım dönüşüm

1. `//@version=5` → `//@version=6`
2. `study(` → `indicator(`
3. Parametreler aynı kalır — bir şey değiştirmeye gerek yok

---

## EN | English

`study()` was removed in Pine Script v6. Use `indicator()` instead.

```pine
// ❌ v5
//@version=5
study("My Indicator", overlay=true)

// ✅ v6
//@version=6
indicator("My Indicator", overlay=true)
```

### Migration steps

1. `//@version=5` → `//@version=6`
2. `study(` → `indicator(`
3. All parameters remain the same
