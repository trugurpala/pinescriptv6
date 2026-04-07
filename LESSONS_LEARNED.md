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

---

### Hacim Olmadan EMA Cross = Muhtemelen Fakeout
- **Durum / Situation:** EMA crossover sinyali geldi ama fiyat hemen geri döndü
- **Sebep / Cause:** Düşük hacimli gürültü, EMA'yı kısaca kesti
- **Çözüm / Fix:** Hacim filtresi + HTF trend filtresi ekle

```pine
//@version=6
// Sinyal sadece yeterli hacim + HTF trend uyumunda geçerli
float volAvg = ta.sma(volume, 20)
float htfEma = request.security(syminfo.tickerid, "60",
    ta.ema(close, 50)[1], lookahead=barmerge.lookahead_on)
bool signal  = ta.crossover(ta.ema(close,9), ta.ema(close,21))
              and volume > volAvg * 1.5   // hacim onayı / volume confirm
              and close > htfEma          // HTF trend yönü / HTF direction
```

- **Referans / Reference:** `concepts/signal_quality.md`

---

### request.security() lookahead_on + [1] = Repainting Yok
- **Not / Note:** MTF filtresi kullanırken repainting önlemek için her zaman `[1]` ekle
- **Çözüm / Fix:**

```pine
//@version=6
// ❌ Repainting yapar / Causes repainting
float htf = request.security(syminfo.tickerid, "60", ta.ema(close,50))

// ✅ Repainting yok / No repainting
float htf = request.security(syminfo.tickerid, "60",
    ta.ema(close, 50)[1], lookahead=barmerge.lookahead_on)
```

---

### alertcondition() Strategy İçinde Çalışmaz
- **Hata / Warning:** `"alertcondition()" has no effect inside strategies`
- **Sebep / Cause:** `alertcondition()` sadece indicator'larda çalışır. Strategy'lerde `alert()` kullanılmalı.
- **Çözüm / Fix:** Strategy içinde `alert()` fonksiyonunu `if` bloğu içinde kullan.

```pine
//@version=6
// ❌ Yanlış / Wrong — strategy içinde
// alertcondition(bullCross, "Long", "Long signal")

// ✅ Doğru / Correct — strategy içinde
if bullCross
    alert("VİOP Long — " + syminfo.ticker + " @ " + str.tostring(close), alert.freq_once_per_bar)
```

---

### barstate.islast + label.new Strategy'de Güvenilmez
- **Hata / Warning:** `Strategies without "calc_on_every_tick = true" only calculate on confirmed chart bars. In this case, "barstate.islast" may not initially return "true" on realtime bars`
- **Sebep / Cause:** Strategy varsayılan olarak her bar kapanışında hesaplar. `barstate.islast` realtime bar'da çalışmaz.
- **Çözüm / Fix:** Ya `calc_on_every_tick=true` ekle, ya da label'ı kaldır / indicator'a taşı. Genellikle label'ı kaldırmak en temiz çözüm.

```pine
//@version=6
// ❌ Strategy'de sorunlu
// strategy("Test", calc_on_every_tick=false)  // default
// if barstate.islast
//     label.new(...)

// ✅ Seçenek 1: calc_on_every_tick ekle
strategy("Test", overlay=true, calc_on_every_tick=true)

// ✅ Seçenek 2: Label'ı kaldır, sadece bgcolor/plot kullan
bgcolor(inSession ? color.new(color.blue, 96) : na)
```

---

### Çok Satırlı Boolean — "and" Satır Başında Olamaz
- **Hata / Error:** `Mismatched input "and" expecting set "end of line without line continuation"`
- **Sebep / Cause:** Pine Script v6'da çok satırlı ifadelerde `and`/`or` operatörü bir sonraki satırın **başında** olamaz. Önceki satırın **sonunda** olmalı veya tüm ifade tek satırda yazılmalı.
- **Çözüm / Fix:** Ya tek satırda yaz, ya da operatörü önceki satırın sonuna taşı.

```pine
//@version=6
// ❌ Yanlış / Wrong
bool longEntry = (condition1)
                    and condition2    // HATA: "and" satır başında

// ✅ Doğru 1 / Correct 1 — tek satır
bool longEntry = condition1 and condition2

// ✅ Doğru 2 / Correct 2 — operatör satır sonunda
bool longEntry = condition1 and
                 condition2
```

---

### calc_on_every_tick=true Backtest'i Bozar
- **Uyarı / Warning:** `"Standart olmayan çizelgelerde backtesting yapmak gerçekçi olmayan sonuçlar üretir"`
- **Sebep / Cause:** `calc_on_every_tick=true` strategy'yi her realtime tick'te çalıştırır. Geçmiş barlarda tick verisi olmadığından backtest sonuçları gerçekçi olmaz. TradingView bu yüzden uyarı verir.
- **Çözüm / Fix:** `calc_on_every_tick=false` (default) kullan. `barstate.islast` tablo/label için sorun değil — her bar kapanışında güncellenir, yeterlidir.

```pine
//@version=6
// ❌ Yanlış / Wrong — backtest'i bozar
strategy("Test", calc_on_every_tick=true)

// ✅ Doğru / Correct — default, backtest güvenilir
strategy("Test", overlay=true)
// barstate.islast tablo için sorunsuz çalışır
```
