# Lessons Learned — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TradingView: https://tr.tradingview.com/u/trugurpala/
> X (Twitter): https://x.com/trugurpala

---

## Bu Dosya Nedir? / What Is This File?

TR: Bu dosya Pine Script v6 geliştirme sırasında karşılaşılan gerçek hataları ve çözümlerini
    kalıcı olarak saklar. AI her oturumda kodu yazmadan önce bu dosyayı okur.
    Yeni bir hata çözülünce AI bu dosyayı otomatik günceller.

EN: This file permanently stores real Pine Script v6 errors and their fixes encountered
    during development. The AI reads this before writing any code, every session.
    When a new error is solved, the AI automatically updates this file.

**Kullandığını nasıl anlarsın? / How do you know it's working?**
TR: AI bu dosyayı okuduğunda şunu söylemeli:
    "LESSONS_LEARNED.md okudum — bilinen hatalar: [liste]. Şimdi kodu yazıyorum."

EN: When the AI reads this file, it should say:
    "Read LESSONS_LEARNED.md — known errors: [list]. Now writing the code."

---

## Format

```markdown
### [Hatanın kısa adı / Short error name]
- **Hata / Error:** `TradingView'dan tam hata metni / exact text from TradingView`
- **Sebep / Cause:** Neden oluşuyor / why it happens
- **Çözüm / Fix:** Nasıl düzeltilir / how to resolve

\`\`\`pine
//@version=6
// ❌ Yanlış / Wrong
...
// ✅ Doğru / Correct
...
\`\`\`
```

---

## Kayıtlı Hatalar / Recorded Errors

---

### ta.stoch() v6'da Tuple Döndürmez
- **Hata / Error:** `Cannot call 'ta.stoch' with these arguments`
- **Sebep / Cause:** v6'da `ta.stoch()` sadece K (float) döndürür. v5'te tuple döndürürdü.
- **Çözüm / Fix:** `[k, d] = ta.stoch(...)` yerine önce K al, sonra D için SMA hesapla.

```pine
//@version=6
// ❌ Yanlış / Wrong — v5 syntax
// [k, d] = ta.stoch(high, low, close, 14)

// ✅ Doğru / Correct — v6
float rawK = ta.stoch(high, low, close, 14)  // sadece K döner / returns only K
float k    = ta.sma(rawK, 3)                 // K smoothing
float d    = ta.sma(k, 3)                    // D = SMA of K
```

---

### math.avg() v6'da Yok
- **Hata / Error:** `Undeclared identifier 'math.avg'`
- **Sebep / Cause:** `math.avg()` Pine Script v6'da kaldırıldı.
- **Çözüm / Fix:** Manuel ortalama hesapla: `(a + b) / 2`

```pine
//@version=6
// ❌ Yanlış / Wrong
// float mid = math.avg(ta.highest(20), ta.lowest(20))

// ✅ Doğru / Correct
float mid = (ta.highest(20) + ta.lowest(20)) / 2
```

---

### request.security() Tuple — Doğru Kullanım
- **Not / Note:** Birden fazla değer alırken köşeli parantez zorunlu.
- **Sebep / Cause:** Tuple syntax yanlış yazılınca type error verir.

```pine
//@version=6
// ✅ Doğru / Correct
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
    [high[1], low[1], close[1]], lookahead=barmerge.lookahead_on)
```

---

### strategy.commission.cash_per_contract Kullanımı
- **Not / Note:** Futures için `strategy.commission.cash_per_contract` kullan.

```pine
//@version=6
strategy("ES Demo",
    commission_type  = strategy.commission.cash_per_contract,
    commission_value = 4.0)  // $4 per side / taraf başı
```

---

> TR: Yeni bir hata çözünce buraya ekle. Format: başlık + hata mesajı + sebep + çözüm + kod.
> EN: When you solve a new error, add it here. Format: title + error + cause + fix + code.
