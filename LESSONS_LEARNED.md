# Lessons Learned — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: Bu dosya AI tarafından otomatik güncellenir. Her Pine Script v6 hata çözümü buraya eklenir.
EN: This file is auto-updated by the AI. Every Pine Script v6 error fix is appended here.

---

## Format

```markdown
### [Kısa Başlık / Short Title]
- **Hata / Error:** `exact error text`
- **Sebep / Cause:** ...
- **Çözüm / Fix:** ...
```

---

## Kayıtlı Hatalar / Recorded Errors

---

### ta.stoch() v6'da Tuple Döndürmez
- **Hata / Error:** `Cannot call 'ta.stoch' with these arguments`
- **Sebep / Cause:** v6'da `ta.stoch()` sadece `K` (float) döndürür. v5'te tuple döndürürdü.
- **Çözüm / Fix:** `[k, d] = ta.stoch(...)` yerine önce K al, sonra D için SMA hesapla.

```pine
//@version=6
// ❌ Yanlış — v5 syntax
// [k, d] = ta.stoch(high, low, close, 14)

// ✅ Doğru — v6
float rawK = ta.stoch(high, low, close, 14)  // sadece K döner
float k    = ta.sma(rawK, 3)                 // K smoothing
float d    = ta.sma(k, 3)                    // D = SMA of K
```

---

### math.avg() v6'da Yok
- **Hata / Error:** `Undeclared identifier 'math.avg'`
- **Sebep / Cause:** `math.avg()` Pine Script v6'da bulunmuyor.
- **Çözüm / Fix:** Manuel ortalama hesapla: `(a + b) / 2`

```pine
//@version=6
// ❌ Yanlış
// float mid = math.avg(ta.highest(20), ta.lowest(20))

// ✅ Doğru
float mid = (ta.highest(20) + ta.lowest(20)) / 2
```

---

### request.security() İçinde Tuple — Doğru Kullanım
- **Hata / Error:** Yanlış tipde atama
- **Sebep / Cause:** request.security'ye tuple geçerken köşeli parantez gerekli.
- **Çözüm / Fix:** Köşeli parantez içinde tuple yaz.

```pine
//@version=6
// ✅ Doğru — tuple ile birden fazla değer
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
    [high[1], low[1], close[1]], lookahead=barmerge.lookahead_on)
```

---

### strategy.commission.cash_per_contract — Geçerli Değer
- **Not / Note:** Futures için `strategy.commission.cash_per_contract` geçerlidir.
- **Kullanım / Usage:**

```pine
//@version=6
strategy("ES Demo",
    commission_type  = strategy.commission.cash_per_contract,
    commission_value = 4.0)  // $4 per side
```

---
