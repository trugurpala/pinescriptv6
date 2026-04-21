# Pine Script v6 Knowledge Pack

Bu dosya, `Pine Script v6 Hata Hafizasi` Custom GPT icin tek dosyalik bilgi paketidir.
Kaynak repo: https://github.com/trugurpala/pinescriptv6

GPT kullanim notu:
- Bu dosyadaki kaynak path basliklarini dikkate al.
- Pine kodu uretmeden once LESSONS_LEARNED ve LLM_MANIFEST bolumlerini onceliklendir.
- Guncellik gerektiren konularda resmi TradingView Pine Script dokumanlarini kontrol et.

---



---

## Source: AGENTS.md

# Pine Script v6 Reference — Agent Instructions
> Author: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TradingView: https://tr.tradingview.com/u/trugurpala/
> X (Twitter): https://x.com/trugurpala

---

## Bu Repo Neden Var? / Why This Repo Exists?

TR: TradingView Pine Script v6 çıktığında tüm AI editörler v5 kodu yazmaya devam etti.
    Claude v5 hatalarını tekrarlıyordu. Cursor `study()` yazıyordu.
    Bu repo AI agent'lara doğru v6 referansı ve kalıcı hata hafızası verir.

EN: When Pine Script v6 launched, all AI editors kept writing v5 code.
    Claude repeated v5 errors. Cursor wrote `study()`.
    This repo gives AI agents correct v6 reference and permanent error memory.

---

## Kullandığını Nasıl Anlarsın? / How to Verify?

✅ Agent LESSONS_LEARNED.md okuduğunu belirtmeli / should mention reading it
✅ //@version=6 ile başlamalı / must start with //@version=6
✅ ta.* kullanmalı / must use ta.*
✅ Hata olunca LESSONS_LEARNED.md'ye eklemeli / must append on error
❌ v5 syntax görüyorsan repo bağlı değil / if v5 syntax, repo not connected

---

## Görev Protokolü / Task Protocol

1. `LESSONS_LEARNED.md` oku — bilinen hatalar
2. `LLM_MANIFEST.md` ile doğru referans dosyasını bul
3. O dosyayı oku
4. `//@version=6` ile başlayan kod yaz
5. Hata olunca: çöz + `LESSONS_LEARNED.md`'ye ekle

---

## Kesin Kurallar / Non-Negotiable Rules

1. `//@version=6` — her scriptin ilk satırı, istisna yok
2. `ta.*` — asla manuel hesaplama
3. `input.int()`, `input.float()` — asla bare `input()`
4. `request.security()` — asla `security()`
5. `indicator()` — asla `study()`
6. Hata çözümünü `LESSONS_LEARNED.md`'ye ekle

---

## Repo İçeriği / What's In This Repo

```
LESSONS_LEARNED.md        — Hata hafızası / Error memory (AI auto-updates)
LLM_MANIFEST.md           — Sorgu yönlendirme / Query routing
reference/                — v6 API referansı / API reference
concepts/                 — Temel kavramlar / Core concepts
examples/indicators/      — 18 indikatör / indicators
examples/strategies/      — 14 strateji / strategies
global-markets/           — 22 global market (ES, NQ, Gold, BTC, ETH, DAX, Nikkei...)
webhook-templates/        — Telegram, Discord, JSON
v5-to-v6-migration/       — v5 → v6 geçiş rehberi / migration guide
```

---

> TR: TradingView resmi Pine Script v6 dokümantasyonu temel referans materyalidir.
> TradingView bu projeyle hiçbir resmi bağlantısı bulunmamaktadır.
>
> EN: TradingView official Pine Script v6 documentation is the primary reference.
> TradingView is not affiliated with this project.

---

## LESSONS_LEARNED Özeti (11 Hata)

1. `ta.stoch()` → tuple değil
2. `math.avg()` → yok
3. `request.security()` tuple syntax
4. Futures komisyon → `cash_per_contract`
5. EMA + hacim filtresi
6. `request.security()` → `[1]` + `lookahead_on`
7. `alertcondition()` → strategy'de `alert()` kullan
8. `barstate.islast` + label → sorunlu
9. Çok satırlı `and` başta → hata
10. `calc_on_every_tick=true` → backtest bozar
11. `barstate.islast` → `barstate.isconfirmed` kullan



---

## Source: concepts\colors_and_display.md

# Colors & Display
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Temel Renkler

```pine
color.red, color.green, color.blue, color.orange, color.yellow
color.white, color.black, color.gray, color.lime, color.aqua
color.fuchsia, color.navy, color.purple, color.teal, color.silver
```

### color.new() — Şeffaflık

```pine
color.new(color.red, 0)    // tam opak
color.new(color.red, 50)   // %50 şeffaf
color.new(color.red, 100)  // tamamen şeffaf (görünmez)
```

### color.from_gradient() — Geçiş Rengi

```pine
//@version=6
indicator("Gradient RSI")
rsi = ta.rsi(close, 14)
bull = color.from_gradient(rsi, 50, 80, color.new(color.green, 70), color.green)
bear = color.from_gradient(rsi, 20, 50, color.red, color.new(color.red, 70))
plot(rsi, color = rsi >= 50 ? bull : bear)
hline(70), hline(50), hline(30)
```

### bgcolor() — Arka Plan

```pine
// Oturum vurgusu
isSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
bgcolor(isSession ? color.new(color.blue, 92) : na)
```

---

## EN | English

### Built-in Colors

```pine
color.red, color.green, color.blue, color.orange, color.yellow
color.white, color.black, color.gray, color.lime, color.aqua
color.fuchsia, color.navy, color.purple, color.teal, color.silver
```

### color.new() — Transparency

```pine
color.new(color.red, 0)    // fully opaque
color.new(color.red, 50)   // 50% transparent
color.new(color.red, 100)  // invisible
```

### color.from_gradient() — Gradient

```pine
//@version=6
indicator("Gradient RSI")
rsi = ta.rsi(close, 14)
bull = color.from_gradient(rsi, 50, 80, color.new(color.green, 70), color.green)
bear = color.from_gradient(rsi, 20, 50, color.red, color.new(color.red, 70))
plot(rsi, color = rsi >= 50 ? bull : bear)
hline(70), hline(50), hline(30)
```

### bgcolor() — Background

```pine
// Session highlight
isSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
bgcolor(isSession ? color.new(color.blue, 92) : na)
```



---

## Source: concepts\common_errors.md

# Common Errors
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### 1. "Cannot use 'series' type as argument"

Fonksiyon `simple` veya `const` bekliyor ama `series` veriliyor.

```pine
// ❌ Yanlış — length series olamaz
length = close > open ? 14 : 20
rsi = ta.rsi(close, length)

// ✅ Doğru — input veya sabit kullan
int length = input.int(14, "Length")
rsi = ta.rsi(close, length)
```

### 2. "max_bars_back" Hatası

Geçmiş veriye yeterli buffer ayrılmamış.

```pine
// ❌ Hata verebilir
myVar = close[500]

// ✅ Buffer'ı artır
max_bars_back(close, 500)
myVar = close[500]

// veya indicator parametresinde
indicator("Demo", max_bars_back=500)
```

### 3. "Undeclared identifier"

Değişken tanımlandığı scope dışında kullanılıyor.

```pine
// ❌ if bloğu dışında tanımsız
if condition
    myVal = close * 2
plot(myVal)  // HATA

// ✅ Dışarıda tanımla
myVal = condition ? close * 2 : na
plot(myVal)
```

### 4. Repainting

`request.security()` canlı bar verisini kullanıyor.

```pine
// ❌ Repainting yapabilir
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Kapanmış bar kullan
htf = request.security(syminfo.tickerid, "D", close[1])
```

### 5. "Loop is too long"

For/while döngüsü çok uzun sürdü.

**Çözüm:** Döngü içindeki işlemi optimize et, gereksiz iterasyonları azalt.

---

## EN | English

### 1. "Cannot use 'series' type as argument"

Function expects `simple` or `const` but received `series`.

```pine
// ❌ Wrong — length cannot be series
length = close > open ? 14 : 20
rsi = ta.rsi(close, length)

// ✅ Correct — use input or constant
int length = input.int(14, "Length")
rsi = ta.rsi(close, length)
```

### 2. "max_bars_back" Error

Not enough historical buffer allocated.

```pine
// ❌ May error
myVar = close[500]

// ✅ Increase buffer
max_bars_back(close, 500)
myVar = close[500]
```

### 3. "Undeclared identifier"

Variable used outside its declaring scope.

```pine
// ❌ Undefined outside if block
if condition
    myVal = close * 2
plot(myVal)  // ERROR

// ✅ Declare outside
myVal = condition ? close * 2 : na
plot(myVal)
```

### 4. Repainting

`request.security()` using live bar data.

```pine
// ❌ May repaint
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Use confirmed bar
htf = request.security(syminfo.tickerid, "D", close[1])
```

### 5. "Loop is too long"

For/while loop ran too long.

**Fix:** Optimize the loop body, reduce unnecessary iterations.



---

## Source: concepts\execution_model.md

# Execution Model
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Pine Script her cubukta soldan sağa, baştan sona çalışır.

### Historical vs Realtime

| Bar türü | Nasıl çalışır? |
|----------|----------------|
| **Historical** | Kapanmış bar. Script bir kere çalışır, sonuç commitlenir. |
| **Realtime** | Açık bar. Her tick'te yeniden çalışır. Kapanınca commit edilir. |
| **Rollback** | Realtime barda kapanış öncesi her execution rollback'lenir (`varip` hariç). |

```pine
//@version=6
indicator("Execution demo")
plot(barstate.ishistory  ? 1 : 0, "isHistory")
plot(barstate.isrealtime ? 1 : 0, "isRealtime")
plot(barstate.isconfirmed ? 1 : 0, "isClosed")
```

### var ve varip

| Keyword | Sıfırlanır mı? | Rollback? | Kullanım |
|---------|---------------|-----------|----------|
| *(yok)* | Her barda | Evet | Normal değişken |
| `var` | Hayır | Evet | Kümülatif sayaç, persistent state |
| `varip` | Hayır | **Hayır** | Realtime tick sayacı |

```pine
//@version=6
indicator("var demo")

// Normal — her barda 1
normalVar = 0
normalVar += 1
plot(normalVar)  // hep 1

// var — kümülatif
var int counter = 0
counter += 1
plot(counter)  // 1, 2, 3 ...
```

### Time Series — Geçmiş Değer

```pine
close[0]  // bu bar
close[1]  // bir önceki bar
close[5]  // 5 bar önce
```

### barstate Değişkenleri

```pine
barstate.ishistory   // geçmiş bar
barstate.isrealtime  // canlı bar
barstate.isconfirmed // kapanmış bar
barstate.islast      // son bar
barstate.isfirst     // ilk bar
barstate.isnew       // bar yeni mi açıldı?
```

---

## EN | English

Pine Script runs left to right, bar by bar, from top to bottom on every bar.

### Historical vs Realtime

| Bar type | How it works |
|----------|-------------|
| **Historical** | Closed bar. Script runs once, result committed. |
| **Realtime** | Open bar. Reruns on every tick. Committed on close. |
| **Rollback** | Before close, each execution is rolled back (`varip` exempt). |

### var and varip

| Keyword | Resets? | Rollback? | Use case |
|---------|---------|-----------|----------|
| *(none)* | Every bar | Yes | Normal variable |
| `var` | Never | Yes | Cumulative counter, persistent state |
| `varip` | Never | **No** | Realtime tick counter |

### Time Series — Historical Values

```pine
close[0]  // current bar
close[1]  // previous bar
close[5]  // 5 bars ago
```



---

## Source: concepts\methods.md

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



---

## Source: concepts\objects.md

# Objects & UDT
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### User-Defined Type (UDT) Tanımla

```pine
//@version=6
indicator("UDT demo", overlay=true)

// @type Grafikteki bir pivot noktasını temsil eder.
// @field index (int)   Bar indexi
// @field price (float) Fiyat seviyesi
// @field isHigh (bool) Pivot yüksek mi?
type PivotPoint
    int   index
    float price
    bool  isHigh
```

### Instance Oluştur

```pine
var PivotPoint lastPivot = na

if not na(ta.pivothigh(high, 5, 5))
    lastPivot := PivotPoint.new(
        index  = bar_index[5],
        price  = high[5],
        isHigh = true
    )
    label.new(lastPivot.index, lastPivot.price, "PH",
              style=label.style_label_down, color=color.red)
```

### na Kontrolü

```pine
if not na(lastPivot)
    // lastPivot güvenle kullan
    plot(lastPivot.price, "Last Pivot", color.orange)
```

### Copy

```pine
p1 = PivotPoint.new(bar_index, high, true)
p2 = p1.copy()  // shallow copy
```

---

## EN | English

### Define a User-Defined Type (UDT)

```pine
//@version=6
indicator("UDT demo", overlay=true)

// @type Represents a pivot point on the chart.
// @field index (int)   Bar index
// @field price (float) Price level
// @field isHigh (bool) Is it a pivot high?
type PivotPoint
    int   index
    float price
    bool  isHigh
```

### Create an Instance

```pine
var PivotPoint lastPivot = na

if not na(ta.pivothigh(high, 5, 5))
    lastPivot := PivotPoint.new(
        index  = bar_index[5],
        price  = high[5],
        isHigh = true
    )
    label.new(lastPivot.index, lastPivot.price, "PH",
              style=label.style_label_down, color=color.red)
```

### na Check

```pine
if not na(lastPivot)
    // safely use lastPivot
    plot(lastPivot.price, "Last Pivot", color.orange)
```

### Copy

```pine
p1 = PivotPoint.new(bar_index, high, true)
p2 = p1.copy()  // shallow copy
```



---

## Source: concepts\signal_quality.md

# Signal Quality & Fakeout Filtering — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com
> TradingView: https://tr.tradingview.com/u/trugurpala/
> GitHub: https://github.com/trugurpala/pinescriptv6

---

## TR | Neden Sahte Sinyal Olur?

Teknik indikatörler fiyatı LAG ile takip eder — gerçek hareket olduğunda
sinyal zaten "geç" gelir. Piyasa gürültüsü bu gecikmeyi istismar eder:
fiyat kısa süre kırılma yapar, sinyal tetiklenir, fiyat geri döner.

**Fakeout = kırılma görünümlü ama devam etmeyen hareket.**

---

## EN | Why Fakeouts Happen?

Technical indicators follow price with a LAG — by the time a signal fires,
the real move may be over. Market noise exploits this: price briefly breaks,
the signal triggers, then price reverses.

**Fakeout = a breakout that looks real but fails to follow through.**

---

## 4 Temel Filtre / 4 Core Filters

---

### 1. Hacim Onayı / Volume Confirmation

TR: Gerçek kırılmalar yüksek hacimle gelir. Düşük hacimli kırılma = şüpheli.
EN: Real breakouts come with high volume. Low-volume breakout = suspicious.

```pine
//@version=6
// Hacim ortalamanın kaç katı olmalı
float volMult  = input.float(1.5, "Volume Multiplier", step=0.1)
float volAvg   = ta.sma(volume, 20)
bool  volOK    = volume > volAvg * volMult   // yeterli hacim / sufficient volume

// Sinyal + hacim onayı
bool signal    = ta.crossover(ta.ema(close,9), ta.ema(close,21))
bool confirmed = signal and volOK             // onaylı sinyal / confirmed signal
```

**Ne zaman kullan / When to use:**
- Futures: ES, NQ, CL — hacim önemli
- Crypto: BTC, ETH — 24/7 hacim verisi var
- Forex: Hacim verisi yetersiz, dikkatli kullan

---

### 2. Zaman Filtresi (Bar Confirmation) / Time Filter

TR: Sinyal oluşunca hemen girmek yerine N bar bekle, fiyat seviyeyi koruyor mu?
EN: Instead of entering immediately on signal, wait N bars — does price hold?

```pine
//@version=6
int barConfirm = input.int(2, "Bar Confirmation", minval=1, maxval=5,
    tooltip="Kaç bar sinyal yönünde kapanmalı / Bars to confirm signal")

// EMA cross sonrası N bar kapanışını say
var int barCount = 0
bool rawSignal  = ta.crossover(ta.ema(close,9), ta.ema(close,21))

if rawSignal
    barCount := 0
if barCount >= 0 and barCount < barConfirm
    barCount += 1

// Sadece N bar sonra gir
bool confirmed  = barCount == barConfirm and close > ta.ema(close,21)
```

**Dezavantaj / Tradeoff:**
Daha geç giriş = daha iyi onay AMA daha kötü fiyat.
Late entry = better confirmation BUT worse price.

---

### 3. Çoklu Zaman Dilimi Filtresi / Multi-Timeframe (MTF) Filter

TR: Alt TF sinyalini üst TF trendi ile onayla. Zıt yönde sinyal alma.
EN: Confirm lower TF signal with higher TF trend. Don't trade against the HTF.

```pine
//@version=6
string htfInput = input.string("60", "HTF Timeframe",
    options=["15","30","60","240","D"])

// Üst TF EMA'sı — repainting'i önlemek için [1] kullan
float htfEma = request.security(syminfo.tickerid, htfInput,
    ta.ema(close, 50)[1], lookahead=barmerge.lookahead_on)

bool htfBull  = close > htfEma   // üst TF yükseliş trendi
bool htfBear  = close < htfEma   // üst TF düşüş trendi

// Sadece HTF trend yönünde gir
bool longOK   = ta.crossover(ta.ema(close,9), ta.ema(close,21))  and htfBull
bool shortOK  = ta.crossunder(ta.ema(close,9), ta.ema(close,21)) and htfBear
```

**Önerilen TF kombinasyonları / Recommended combinations:**
- 5M sinyal + 1H filtre
- 15M sinyal + 4H filtre
- 1H sinyal + 1D filtre

---

### 4. ATR Gürültü Filtresi / ATR Noise Filter

TR: Fiyat hareketi ATR'nin belirli bir katından büyük mü? Küçük hareketler gürültüdür.
EN: Is the price move larger than N × ATR? Small moves are noise.

```pine
//@version=6
float noiseFilter = input.float(0.5, "Min Move (ATR mult)", step=0.1,
    tooltip="Sinyalin ATR'nin kaç katı kadar hareket etmeli")

float atrVal     = ta.atr(14)
float priceMove  = math.abs(close - close[1])
bool  realMove   = priceMove > atrVal * noiseFilter   // gerçek hareket / real move

bool signal      = ta.crossover(ta.ema(close,9), ta.ema(close,21))
bool confirmed   = signal and realMove
```

---

## Birleşik Filtre Skoru / Combined Filter Score

TR: 4 filtrenin kaçı onayladı? Skor yüksekse sinyal güçlüdür.
EN: How many of the 4 filters confirm? Higher score = stronger signal.

```pine
//@version=6
indicator("Signal Quality Score [trugurpala]", overlay=false)

// Hesaplamalar
float volAvg    = ta.sma(volume, 20)
float htfEma    = request.security(syminfo.tickerid, "60",
    ta.ema(close,50)[1], lookahead=barmerge.lookahead_on)
float atrVal    = ta.atr(14)

bool volOK      = volume > volAvg * 1.5
bool htfOK      = close > htfEma
bool atrOK      = math.abs(close - close[1]) > atrVal * 0.3
bool trendOK    = ta.ema(close, 9) > ta.ema(close, 21)

// Skor: 0-4 arası
int score = (volOK ? 1 : 0) + (htfOK ? 1 : 0) + (atrOK ? 1 : 0) + (trendOK ? 1 : 0)

// Renklendirme
color c = score >= 3 ? color.green : score == 2 ? color.orange : color.red
plot(score, "Signal Score", c, style=plot.style_histogram, linewidth=4)
hline(3, "Strong", color.green, hline.style_dashed)
hline(2, "Medium", color.orange, hline.style_dotted)
```

---

## Fakeout Tespit Paterni / Fakeout Detection Pattern

TR: Klasik fakeout: fiyat seviyeyi kırar, 1-3 bar içinde geri döner.
EN: Classic fakeout: price breaks a level, returns within 1-3 bars.

```pine
//@version=6
// Pivot kırılması sonrası geri dönüş tespiti
float pivHigh   = ta.pivothigh(high, 5, 5)
var float lastPH = na
if not na(pivHigh)
    lastPH := high[5]

// Kırılma var mı?
bool brokenUp   = not na(lastPH) and high > lastPH and high[1] <= lastPH

// 1-3 bar içinde geri döndü mü? = FAKEOUT
bool fakeout    = brokenUp[1] and close < lastPH   // kırıldı ama kapandı altında
             or  brokenUp[2] and close < lastPH
             or  brokenUp[3] and close < lastPH
```

---

## AI İçin Özet / Summary for AI

TR: Bir Pine Script v6 stratejisi yazarken şu filtreleri düşün:
1. **Hacim** — `volume > ta.sma(volume,20) * 1.5`
2. **Bar onayı** — sinyal sonrası N bar bekle, seviye korunuyor mu?
3. **HTF filtresi** — `request.security(..., ta.ema(close,50)[1], lookahead_on)`
4. **ATR filtresi** — hareket gürültüden büyük mü?

EN: When writing a Pine Script v6 strategy, consider these filters:
1. **Volume** — `volume > ta.sma(volume,20) * 1.5`
2. **Bar confirmation** — wait N bars after signal, is level held?
3. **HTF filter** — `request.security(..., ta.ema(close,50)[1], lookahead_on)`
4. **ATR filter** — is the move larger than noise?

> Bu dosyayı referans al / Reference this file: `concepts/signal_quality.md`



---

## Source: concepts\timeframes.md

# Timeframes & Multi-Timeframe (MTF)
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### request.security() Temeli

```pine
//@version=6
indicator("MTF Demo", overlay=true)
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))
plot(dailyClose)
plot(weeklyEma)
```

### Repainting Önleme

```pine
// ❌ Canlı bar verisi — repainting yapabilir
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Kapanmış bar — güvenli
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

### Çoklu Değer — Tuple

```pine
[htfOpen, htfHigh, htfLow, htfClose] =
    request.security(syminfo.tickerid, "D", [open, high, low, close])
```

### Timeframe Stringleri

| String | Anlamı |
|--------|--------|
| `"1"` | 1 dakika |
| `"5"` | 5 dakika |
| `"15"` | 15 dakika |
| `"60"` | 1 saat |
| `"240"` | 4 saat |
| `"D"` | Günlük |
| `"W"` | Haftalık |
| `"M"` | Aylık |

### Grafik Timeframe'ini Kontrol Et

```pine
isDaily = timeframe.in_seconds() >= timeframe.in_seconds("D")
bgcolor(isDaily ? color.new(color.blue, 90) : na)
```

---

## EN | English

### request.security() Basics

```pine
//@version=6
indicator("MTF Demo", overlay=true)
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))
plot(dailyClose)
plot(weeklyEma)
```

### Prevent Repainting

```pine
// ❌ Live bar data — may repaint
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Confirmed bar — safe
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

### Multiple Values — Tuple

```pine
[htfOpen, htfHigh, htfLow, htfClose] =
    request.security(syminfo.tickerid, "D", [open, high, low, close])
```

### Timeframe Strings

| String | Meaning |
|--------|---------|
| `"1"` | 1 minute |
| `"5"` | 5 minutes |
| `"15"` | 15 minutes |
| `"60"` | 1 hour |
| `"240"` | 4 hours |
| `"D"` | Daily |
| `"W"` | Weekly |
| `"M"` | Monthly |



---

## Source: CONTRIBUTING.md

# Katkı Rehberi / Contributing Guide

**TR:** Bu repo Ugur Pala'nın Pine Script v6 geliştirme ortamıdır. Topluluk katkıları memnuniyetle karşılanır.
**EN:** This is Ugur Pala's Pine Script v6 development environment. Community contributions are welcome.

---

## Ne Kabul Edilir? / What's Accepted?

**TR:**
- Pine Script v6 ile yazılmış, TradingView'da test edilmiş çalışan kod
- Yeni LESSONS_LEARNED hatası — gerçek TradingView hata mesajıyla
- v5→v6 migration notları
- Yeni global market örneği (doğru seans + komisyon)
- Webhook entegrasyon şablonu
- Dokümantasyon iyileştirmesi

**EN:**
- Working code written in Pine Script v6, tested on TradingView
- New LESSONS_LEARNED error — with real TradingView error message
- v5→v6 migration notes
- New global market example (correct session + commission)
- Webhook integration template
- Documentation improvement

---

## Pine Script v6 Zorunlulukları / Requirements

```pine
//@version=6
indicator("Name")   // TR: study() değil / EN: not study()

// ✅ Doğru / Correct
float k   = ta.stoch(high, low, close, 14)  // tek değer / single value
float mid = (ta.highest(20) + ta.lowest(20)) / 2  // math.avg() yok
float htf = request.security(syminfo.tickerid, "60",
              ta.ema(close, 50)[1], lookahead=barmerge.lookahead_on)
```

**TR: Katkı yapmadan önce** [LESSONS_LEARNED.md](LESSONS_LEARNED.md) oku.
**EN: Before contributing**, read [LESSONS_LEARNED.md](LESSONS_LEARNED.md).

---

## Nasıl / How

1. Fork → `feature/açıklama` branch → PR aç
2. TR veya EN açıklama yaz
3. Pine Script v6, test edilmiş kod

**İletişim / Contact:** [Discussions](https://github.com/trugurpala/pinescriptv6/discussions) · [x.com/trugurpala](https://x.com/trugurpala)



---

## Source: examples\README.md

# Examples — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: Tüm örnekler TradingView Pine Script v6 ile yazılmıştır. Copy-paste hazır.
EN: All examples are written for TradingView Pine Script v6. Copy-paste ready.

---

## 📊 Indicators / İndikatörler

| Dosya | Açıklama / Description |
|-------|------------------------|
| `indicators/01_ema_cross.pine` | EMA 9/21 Cross + bgcolor + alerts |
| `indicators/02_rsi_ob_os.pine` | RSI 14 — Gradient color + OB/OS |
| `indicators/03_macd_histogram.pine` | MACD 12/26/9 — Colored histogram |
| `indicators/04_bollinger_bands.pine` | Bollinger Bands + Squeeze detection |
| `indicators/05_supertrend.pine` | Supertrend — ATR-based trend |
| `indicators/06_vwap_session.pine` | VWAP + StDev bands |
| `indicators/07_atr_levels.pine` | ATR dynamic S/R levels |
| `indicators/08_pivot_points.pine` | Classic Pivot Points (Daily) |
| `indicators/09_volume_profile.pine` | Volume analysis + OBV |
| `indicators/10_stoch_rsi.pine` | Stochastic RSI K/D |
| `indicators/11_ichimoku.pine` | Ichimoku Cloud — all components |
| `indicators/12_mtf_ema.pine` | Multi-Timeframe EMA D/W/M |

## 🎯 Strategies / Stratejiler

| Dosya | Açıklama / Description |
|-------|------------------------|
| `strategies/01_ema_cross_strategy.pine` | EMA 9/21 Cross — ATR SL/TP |
| `strategies/02_rsi_mean_reversion.pine` | RSI Mean Reversion — OB/OS fade |
| `strategies/03_supertrend_strategy.pine` | Supertrend trend following |
| `strategies/04_bb_breakout.pine` | Bollinger Band Breakout |
| `strategies/05_macd_strategy.pine` | MACD + EMA trend filter |
| `strategies/06_rsi_atr_strategy.pine` | RSI + ATR SL/TP (VIOP optimized) |
| `strategies/07_mtf_trend_strategy.pine` | Multi-Timeframe trend + entry |
| `strategies/08_triple_ema_strategy.pine` | Triple EMA 5/13/34 alignment |
| `strategies/09_stoch_strategy.pine` | Stochastic Cross + EMA filter |
| `strategies/10_adx_trend_strategy.pine` | ADX Trend Strength + EMA |

---

## Nasıl Kullanılır / How to Use

1. TradingView → Pine Editor → Kodu yapıştır → Add to Chart
2. TradingView → Pine Editor → Paste code → Add to Chart

> TR: Bu örnekler eğitim amaçlıdır. Canlı işlemde kendi analizinizi yapın.
> EN: These examples are for educational purposes. Do your own analysis before live trading.



---

## Source: global-markets\README.md

# Global Markets — Pine Script v6 Examples
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: Dünya genelinde en çok işlem gören enstrümanlar için hazır Pine Script v6 örnekleri.
EN: Ready-to-use Pine Script v6 examples for the world's most actively traded instruments.

---

## Enstrüman Haritası / Instrument Map

| Kategori | TradingView Sembol | Dosya |
|----------|-------------------|-------|
| 🇺🇸 S&P 500 Futures | `CME_MINI:ES1!` / `MES1!` | `01_es_sp500.pine` |
| 🇺🇸 Nasdaq-100 Futures | `CME_MINI:NQ1!` / `MNQ1!` | `02_nq_nasdaq.pine` |
| 🥇 Gold Futures | `COMEX:GC1!` / `XAUUSD` | `03_gc_gold.pine` |
| 🛢️ Crude Oil Futures | `NYMEX:CL1!` | `04_cl_crude_oil.pine` |
| 💱 EUR/USD Forex | `FX:EURUSD` | `05_eurusd_forex.pine` |
| 💱 GBP/USD Forex | `FX:GBPUSD` | `06_gbpusd_forex.pine` |
| 💱 USD/JPY Forex | `FX:USDJPY` | `07_usdjpy_forex.pine` |
| 🪙 Bitcoin | `BINANCE:BTCUSDT` | `08_btc_crypto.pine` |
| 🪙 Ethereum | `BINANCE:ETHUSDT` | `09_eth_crypto.pine` |
| 🇩🇪 DAX (Germany) | `XETR:DAX` / `EUREX:FDAX1!` | `10_dax_germany.pine` |
| 🇯🇵 Nikkei 225 | `TVC:NI225` | `11_nikkei_japan.pine` |
| 🌍 Universal | `syminfo.tickerid` | `12_universal_strategy.pine` |

---

## Her Dosyada Ne Var / What's In Each File

- Market-specific session filters (doğru seans saatleri)
- Market-specific commission settings (gerçek komisyon oranları)
- Market-specific ATR multipliers (volatiliteye göre SL/TP)
- Market-specific notes (sembol, kontrat büyüklüğü, seans)
- TR/EN açıklamalar

---

> TR: Bu örnekler eğitim amaçlıdır. Canlı işlemde kendi analizinizi yapın.
> EN: These examples are for educational purposes. Do your own analysis.



---

## Source: global-markets\STRATEGIES_README.md

# Global Market Strategies — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com
> TradingView: https://tr.tradingview.com/u/trugurpala/
> X: https://x.com/trugurpala
> GitHub: https://github.com/trugurpala/pinescriptv6

TR: Her strateji gerçek piyasa koşullarına göre optimize edilmiştir.
    Doğru seans saatleri, komisyon ve slippage ayarları dahildir.
EN: Each strategy is optimised for real market conditions.
    Correct session times, commission and slippage settings included.

---

## Stratejiler / Strategies

| # | Dosya | Piyasa / Market | Özellik / Feature |
|---|-------|-----------------|-------------------|
| 13 | `13_btc_trend_pullback.pine` | 🪙 BTC/USDT | EMA trend + RSI pullback entry |
| 14 | `14_eth_momentum.pine` | 🪙 ETH/USDT | Momentum breakout + volume confirm |
| 15 | `15_es_opening_range.pine` | 🇺🇸 ES S&P500 | Opening Range Breakout (ORB) |
| 16 | `16_nq_vwap_reversion.pine` | 🇺🇸 NQ Nasdaq | VWAP mean reversion |
| 17 | `17_gc_gold_trend.pine` | 🥇 Gold XAUUSD | Triple EMA trend following |
| 18 | `18_cl_crude_momentum.pine` | 🛢️ Crude Oil | ATR momentum + session filter |
| 19 | `19_eurusd_london_breakout.pine` | 💱 EUR/USD | London session breakout |
| 20 | `20_gbpusd_structure.pine` | 💱 GBP/USD | Market structure + EMA filter |
| 21 | `21_usdjpy_carry_trend.pine` | 💱 USD/JPY | Carry trade trend following |
| 22 | `22_dax_gap_fade.pine` | 🇩🇪 DAX | Gap fade + Xetra session |

---

## Nasıl Kullanılır / How to Use

1. TradingView → Pine Editor → kodu yapıştır → **Add to chart**
2. Strategy Tester ile backtest yap
3. Parametreleri sembolünüze göre ayarlayın

> TR: Eğitim amaçlıdır. Canlı işlemde risk yönetimi yapın.
> EN: Educational purposes only. Apply risk management in live trading.



---

## Source: LESSONS_LEARNED.md

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

---

### barstate.islast Strategy'de Uyarı Verir → barstate.isconfirmed Kullan
- **Uyarı / Warning:** `Strategies without "calc_on_every_tick = true" only calculate on confirmed chart bars. In this case, "barstate.islast" may not initially return "true" on realtime bars`
- **Sebep / Cause:** `barstate.islast` realtime (açık) barda ilk tick'te `true` dönmeyebilir. Strategy bar kapanışında hesapladığı için uyarı verir.
- **Çözüm / Fix:** Table/label güncellemesi için `barstate.isconfirmed` kullan — sadece kapanmış barlarda `true` döner, uyarı vermez.

```pine
//@version=6
// ❌ Strategy'de uyarı verir
// if barstate.islast
//     table.cell(...)

// ✅ Uyarısız — sadece kapanmış barlarda güncellenir
if barstate.isconfirmed
    table.cell(...)
```



---

## Source: LLM_MANIFEST.md

# LLM Manifest — Pine Script v6
# Repo: github.com/trugurpala/pinescriptv6
# Maintainer: Ugur Pala · mail@ugurpala.com

TR: Bu dosya AI'ın hangi soruda hangi referans dosyasını okuyacağını belirler.
EN: This file tells the AI which reference file to read for each type of query.

---

## Protokol / Protocol

1. TR: LESSONS_LEARNED.md'yi kontrol et — bilinen hataları tekrarlama
   EN: Check LESSONS_LEARNED.md — never repeat a known error

2. TR: Aşağıdaki tablodan ilgili dosyayı bul ve ONU oku
   EN: Find the relevant file below and read ONLY that file

3. TR: Kodu yaz, hata olursa LESSONS_LEARNED.md'yi güncelle
   EN: Write code; on error update LESSONS_LEARNED.md

---

## 1. Kavramlar / Concepts

| Anahtar Kelimeler / Keywords | Dosya / File |
|---|---|
| barstate, var, varip, history, realtime | `concepts/execution_model.md` |
| max_bars_back, series string, undeclared | `concepts/common_errors.md` |
| request.security, repainting, HTF, MTF | `concepts/timeframes.md` |
| color.new, from_gradient, bgcolor | `concepts/colors_and_display.md` |
| method, user-defined method | `concepts/methods.md` |
| type, UDT, object, field | `concepts/objects.md` |

## 2. Referans / Reference

| Anahtar Kelimeler / Keywords | Dosya / File |
|---|---|
| open, close, high, low, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.triangle, plot.style_line | `reference/constants.md` |
| int, float, bool, series, simple | `reference/types.md` |
| if, for, while, var, varip, switch | `reference/keywords.md` |
| @version, @param, @returns, @type | `reference/annotations.md` |

## 3. Fonksiyonlar / Functions

| İhtiyaç / Need | Dosya / File |
|---|---|
| ta.rsi, ta.ema, ta.macd, ta.atr, ta.crossover, ta.pivot | `reference/functions/ta.md` |
| strategy.entry, strategy.exit, strategy.close | `reference/functions/strategy.md` |
| plot, line.new, box.new, label.new, table | `reference/functions/drawing.md` |
| request.security, request.financial | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert, timestamp | `reference/functions/general.md` |

## 4. Kod Yazma / Writing

| İhtiyaç / Need | Dosya / File |
|---|---|
| İsimlendirme, sıralama / Naming, ordering | `writing_scripts/style_guide.md` |
| Pine Logs, debug | `writing_scripts/debugging.md` |
| Performans / Performance | `writing_scripts/profiling_and_optimization.md` |
| Limitler / Limits | `writing_scripts/limitations.md` |

---

## Örnekler / Examples

| Görev / Task | Oku / Read |
|---|---|
| RSI indikatörü yaz | `reference/functions/ta.md` + `reference/functions/drawing.md` |
| EMA strateji yaz | `reference/functions/ta.md` + `reference/functions/strategy.md` |
| Çoklu TF (MTF) | `reference/functions/request.md` + `concepts/timeframes.md` |
| Hata alıyorum | `concepts/common_errors.md` + `LESSONS_LEARNED.md` |
| Değişkenim neden sıfırlanıyor | `concepts/execution_model.md` |



---

## Source: README.md

# Pine Script v6 — AI Reference with Error Memory

<div align="center">

![Pine Script v6](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![AI Ready](https://img.shields.io/badge/AI%20Ready-9%20Editors-7C3AED?style=for-the-badge)
![Examples](https://img.shields.io/badge/Examples-55%2B-22C55E?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/trugurpala/pinescriptv6?style=for-the-badge&color=yellow)
![TR | EN](https://img.shields.io/badge/TR%20%7C%20EN-Bilingual-8B5CF6?style=for-the-badge)

### TR: AI editörünüz artık Pine Script v6'yı doğru yazar — ve hatalarını unutmaz.
### EN: Your AI editor now writes Pine Script v6 correctly — and never forgets its mistakes.

[Ugur Pala](https://github.com/trugurpala) · [TradingView](https://tr.tradingview.com/u/trugurpala/) · [X / Twitter](https://x.com/trugurpala) · mail@ugurpala.com

---

**[🚀 Hızlı Başlangıç](#-hızlı-başlangıç--quick-start)** · **[💡 Neden?](#-neden-var--why-this-exists)** · **[⚙️ Nasıl Çalışır?](#️-nasıl-çalışır--how-it-works)** · **[🤖 Claude](#-claude--claude-code)** · **[⌨️ Cursor](#️-cursor)** · **[🌊 Windsurf](#-windsurf)** · **[🐙 Copilot](#-github-copilot)** · **[🔧 Cline/Roo](#-cline--roo--aider)** · **[📦 Örnekler](#-örnekler--examples)** · **[🌍 Global Markets](#-global-markets-22)** · **[🔔 Webhook](#-webhook-templates-7)** · **[🔄 v5→v6](#-v5--v6-migration-10)**

</div>

---

## 💡 Neden Var / Why This Exists

> **TR: Çünkü AI editörler Pine Script v6 çıktıktan sonra bile v5 yazmaya devam etti.**
> **EN: Because AI editors kept writing v5 code even after Pine Script v6 launched.**

### TR | Türkçe — Gerçek Problem

TradingView Pine Script v6'yı yayınladığında her şey değişti. Ama AI editörler bunu bilmiyordu:

```pine
// ❌ AI'ın v6'da yazdığı — TradingView'da hata verir
//@version=6
study("My Indicator", overlay=true)           // study() v6'da YOK
htf = security(syminfo.tickerid, "D", close)  // security() v6'da YOK
len = input(14, type=input.integer)           // eski input() v6'da YOK
```

```pine
// ✅ Bu repo bağlıyken AI'ın yazdığı — ilk seferde çalışır
//@version=6
indicator("My Indicator", overlay=true)
htf = request.security(syminfo.tickerid, "D", close[1], lookahead=barmerge.lookahead_on)
int len = input.int(14, "Length")
```

**Bu repo üç sorunu çözdü:**

| # | Sorun | Çözüm | Nasıl? |
|---|-------|-------|--------|
| 1 | **AI'ın hafızası yok** — her oturumda sıfırdan başlar, aynı hataları tekrarlar | `LESSONS_LEARNED.md` | Çözülen her hata kalıcı kaydedilir, AI bir sonraki oturumda okur |
| 2 | **v6 referansı çok büyük** — tüm doküman context'e sığmaz | `LLM_MANIFEST.md` | AI sadece o göreve gereken dosyayı okur, token israfı olmaz |
| 3 | **Her editör farklı format bekler** — Claude, Cursor, Windsurf hepsi ayrı | 9 kural dosyası | `CLAUDE.md`, `.cursor/rules/`, `.windsurfrules`, `.clinerules`... hepsi hazır |

---

### EN | English — The Real Problem

When TradingView launched Pine Script v6, everything changed. But AI editors didn't know this.

**Three problems existed. This repo solved all three:**

| # | Problem | Solution | How? |
|---|---------|----------|------|
| 1 | **AI has no memory** — starts from zero each session, repeats mistakes | `LESSONS_LEARNED.md` | Every solved error saved permanently, AI reads it next session |
| 2 | **v6 reference is too large** — full docs won't fit in context | `LLM_MANIFEST.md` | AI reads only the file needed for that task |
| 3 | **Every editor expects different format** — Claude, Cursor, Windsurf all differ | 9 rule files | `CLAUDE.md`, `.cursor/rules/`, `.windsurfrules`, `.clinerules`... all ready |

---

## ⚙️ Nasıl Çalışır / How It Works

> **TR: Repo bağlandıktan sonra arka planda tam olarak neler oluyor — adım adım, gerçek örneklerle.**
> **EN: Exactly what happens under the hood after connecting — step by step, with real examples.**

---

### TR | Türkçe — 5 Adım, Gerçek Örneklerle

---

#### Adım 1 — Sen bir şey istersin. AI önce `LESSONS_LEARNED.md`'yi okur.

Bağlantısız bir AI'ya "XU030 için strateji yaz" dersen ne olur?

```
❌ Bağlantısız AI:
//@version=6
study("Strategy")               ← hata! study() v6'da yok
htf = security(...)             ← hata! security() v6'da yok
[k, d] = ta.stoch(...)          ← hata! v6'da tuple döndürmez
```

Aynı isteği bu repo bağlıyken yapınca ne olur?

```
✅ Bu repo bağlıyken AI:
"LESSONS_LEARNED.md okudum. Bilinen hatalar:
  ⚠  study() yok → indicator() kullan
  ⚠  security() yok → request.security() kullan
  ⚠  ta.stoch() tuple döndürmez → sadece K döner
  ⚠  math.avg() yok → (a+b)/2 kullan
  ⚠  Hacim onayı olmadan EMA cross = muhtemelen fakeout
Şimdi yazıyorum..."
```

**Fark:** Birinci AI "neyin yanlış olduğunu" bilmeden başlıyor. İkinci AI **daha koda başlamadan** tuzakları biliyor.

> 📄 `LESSONS_LEARNED.md` — bu repo kullanıldıkça büyür. Her yeni hata çözülünce otomatik eklenir. Repo zamanla daha akıllı hale gelir.

---

#### Adım 2 — `LLM_MANIFEST.md` doğru referans dosyasını yönlendirir.

Tüm v6 dokümanını AI'a vermek imkânsız — çok büyük, context'e sığmaz.
Bu repo sorunu şöyle çözdü: **Her görev için sadece 1-2 dosya okunur.**

```
Sen: "EMA cross stratejisi yaz"

AI: "LLM_MANIFEST.md'ye baktım:
     → Bu görev için: reference/functions/ta.md + reference/functions/strategy.md
     İki dosyayı okuyorum... hazır. Şimdi yazıyorum."
```

```
Sen: "request.security neden repainting yapıyor?"

AI: "LLM_MANIFEST.md'ye baktım:
     → Bu soru için: concepts/timeframes.md
     Dosyayı okuyorum... sorunun cevabı şu..."
```

**Sonuç:** AI gereksiz dosya okumaz → context korunur → cevap kalitesi artar → hata azalır.

> 📄 `LLM_MANIFEST.md` — 40+ referans dosyasını hangi soruda hangi dosyanın okunacağına göre eşleştirir.

---

#### Adım 3 — Temiz, çalışan v6 kodu yazılır. İlk seferde.

Repo olmadan `ta.stoch()` hatası, `security()` hatası, seans filtresi eksikliği normaldir.
Bu repo bağlıyken aynı isteğe gelen yanıt:

```pine
//@version=6
// XU030 (BIST30 Futures) — EMA Cross Strategy
// github.com/trugurpala/pinescriptv6 — Ugur Pala
strategy("EMA Cross [trugurpala]",
    overlay           = true,
    initial_capital   = 100000,
    default_qty_type  = strategy.percent_of_equity,
    default_qty_value = 10,
    commission_type   = strategy.commission.percent,
    commission_value  = 0.03,   // VİOP komisyon oranı
    slippage          = 2)

// ── Inputs ───────────────────────────────────────────────────────────────────
int   fastLen = input.int(9,   "Fast EMA", minval=1)
int   slowLen = input.int(21,  "Slow EMA", minval=1)
float slMult  = input.float(2.0, "SL Mult", step=0.1)
float tpMult  = input.float(3.0, "TP Mult", step=0.1)

// ── Calculations ─────────────────────────────────────────────────────────────
float fast   = ta.ema(close, fastLen)
float slow   = ta.ema(close, slowLen)
float atrVal = ta.atr(14)
float volAvg = ta.sma(volume, 20)

// VİOP seans filtresi: 09:30–18:15 UTC+3
bool  inSes  = not na(time(timeframe.period, "0930-1815", "UTC+3"))
// Hacim onayı — fakeout filtresi
bool  volOK  = volume > volAvg * 1.5

// ── Entries ──────────────────────────────────────────────────────────────────
if ta.crossover(fast, slow) and inSes and volOK
    strategy.entry("Long", strategy.long)
    strategy.exit("LE", "Long",
        stop  = close - slMult * atrVal,
        limit = close + tpMult * atrVal)

if ta.crossunder(fast, slow) and inSes
    strategy.close("Long", comment="Cross Down")

// ── Visuals ──────────────────────────────────────────────────────────────────
plot(fast, "Fast EMA", fast > slow ? color.green : color.red,    linewidth=2)
plot(slow, "Slow EMA", fast > slow ? color.lime  : color.orange, linewidth=2)
bgcolor(not inSes ? color.new(color.gray, 95) : na, title="Seans Dışı")
```

**Bu kodda neler var ki bağlantısız AI yazmıyor?**

| ✅ Bu Repo Bağlıyken | ❌ Bağlantısız AI |
|---------------------|------------------|
| `strategy()` — doğru seçim yapıldı | `study()` — hata |
| `input.int()` / `input.float()` | eski `input()` — hata |
| `ta.ema()` — fonksiyon kullanıldı | manuel EMA hesabı |
| VİOP seans filtresi | seans filtresi yok |
| Hacim onayı — fakeout azalıyor | her sinyale giriyor |
| ATR tabanlı SL/TP — adaptif | sabit puan SL/TP |
| Komisyon + slippage ayarlı | gerçekçi olmayan backtest |
| Kod yorumunda kaynak var | kaynak yok |

---

#### Adım 4 — Hata alınırsa: çözülür ve `LESSONS_LEARNED.md`'ye eklenir. Bir daha sorulmaz.

TradingView'da hata mesajı geldi:

```
Cannot call 'ta.stoch' with these arguments
```

```
Sen: "Bu hatanın sebebi ne?"

AI: "ta.stoch() Pine Script v6'da tuple döndürmüyor.
     v5'te [k, d] = ta.stoch(...) çalışırdı, v6'da çalışmaz.

     ✅ Doğru kullanım v6'da:
     float rawK = ta.stoch(high, low, close, 14)  // sadece K döner
     float k    = ta.sma(rawK, 3)                  // K smoothing
     float d    = ta.sma(k, 3)                     // D = SMA of K

     Bu hatayı LESSONS_LEARNED.md'ye ekliyorum
     ki bir daha sorman gerekmesin."
```

`LESSONS_LEARNED.md` otomatik güncellendi. **Bir daha o hatayı açıklamak zorunda kalmayacaksın.**

---

#### Adım 5 — Bir sonraki oturumda: geçmiş tamamen hatırlanır.

Dün ta.stoch hatasını çözdün. Bugün yeni bir oturum, farklı bir strateji istiyorsun.

```
Sen: "Stochastic + EMA stratejisi yaz"

AI: "LESSONS_LEARNED.md okudum.
     NOT: ta.stoch() v6'da sadece K döndürür, tuple değil.
     Bu bilgiyle yazmaya başlıyorum — hata almayacaksın."
```

Bir ay sonra, elli farklı strateji sonra:

```
AI: "LESSONS_LEARNED.md okudum. Bilinen 12 hata:
     [1] ta.stoch() tuple yok
     [2] math.avg() yok
     [3] Hacim onaysız EMA = fakeout
     [4] repainting için [1]+lookahead_on şart
     ... 8 hata daha
     Bunların hiçbirini yapmadan yazıyorum."
```

> **Bir kez öğrenildi. Sonsuza kadar hatırlandı.**
> Bu sistem zamanla büyüyen, kendini düzelten bir geliştirme ortamı kurar.
> Repo ne kadar çok kullanılırsa, o kadar akıllı olur.

---

### Kullandığını Nasıl Anlarsın? / How Do You Know It's Working?

| ✅ Repo Aktif — Bunları görürsün | ❌ Repo Bağlı Değil — Bunları görürsün |
|---------------------------------|----------------------------------------|
| AI "LESSONS_LEARNED.md okudum" diyor | AI direkt koda atlıyor |
| Kod `//@version=6` ile başlıyor | `study()` veya `security()` var |
| `indicator()` + `request.security()` + `input.int()` | v5 syntax hataları |
| Seans filtresi, ATR SL/TP, komisyon ayarı var | Basit, filtresiz, eksik kod |
| Hata alınınca "LESSONS_LEARNED.md'ye ekliyorum" | Aynı hata bir hafta sonra tekrar |
| Yorumda `// github.com/trugurpala/pinescriptv6` | Kaynak yok |

---

### EN | English — 5 Steps, With Real Examples

---

#### Step 1 — You make a request. AI reads `LESSONS_LEARNED.md` first.

Without this repo connected, asking "write a strategy for ES futures" gives:

```
❌ Unconnected AI:
study("Strategy")          ← error! study() doesn't exist in v6
htf = security(...)        ← error! security() doesn't exist in v6
[k, d] = ta.stoch(...)     ← error! doesn't return a tuple in v6
```

Same request with this repo connected:

```
✅ With this repo:
"Read LESSONS_LEARNED.md. Known issues:
  ⚠  study() gone → use indicator()
  ⚠  security() gone → use request.security()
  ⚠  ta.stoch() returns only K, not a tuple
  ⚠  math.avg() removed — use (a+b)/2
  ⚠  EMA cross without volume = likely fakeout
Now writing..."
```

**The difference:** The first AI starts not knowing what's wrong. The second AI **knows the traps before writing a single line.**

> 📄 `LESSONS_LEARNED.md` — grows as the repo is used. Every new solved error added automatically. The repo gets smarter over time.

---

#### Step 2 — `LLM_MANIFEST.md` routes to the correct reference file.

Giving AI the entire v6 docs is impossible — too large, won't fit in context.
This repo solved the problem: **Only 1-2 files are read per task.**

```
You: "Write an EMA cross strategy"
AI:  "Checked LLM_MANIFEST.md:
      → For this task: reference/functions/ta.md + reference/functions/strategy.md
      Reading two files... ready. Writing now."
```

```
You: "Why does request.security cause repainting?"
AI:  "Checked LLM_MANIFEST.md:
      → For this question: concepts/timeframes.md
      Reading... here's the answer..."
```

**Result:** AI doesn't read unnecessary files → context preserved → answer quality higher → fewer errors.

> 📄 `LLM_MANIFEST.md` — maps 40+ reference files to the right question type.

---

#### Step 3 — Clean, working v6 code. First time.

Without the repo: `ta.stoch()` error, `security()` error, missing session filter.
With this repo connected — the same request produces code that works immediately:

| ✅ With This Repo | ❌ Unconnected AI |
|------------------|-----------------|
| `strategy()` — correct choice made | `study()` — error |
| `input.int()` / `input.float()` | old `input()` — error |
| `ta.ema()` — built-in used | manual EMA calculation |
| Session filter included | no session filter |
| Volume confirmation — fewer fakeouts | enters every signal |
| ATR-based SL/TP — adaptive | fixed-point SL/TP |
| Commission + slippage set | unrealistic backtest |
| Source comment in code | no attribution |

---

#### Step 4 — On error: solved and saved to `LESSONS_LEARNED.md`. Never asked again.

```
You: "What does this error mean?"
AI:  "ta.stoch() doesn't return a tuple in v6.
     In v5 [k, d] = ta.stoch(...) worked. In v6 it doesn't.

     ✅ Correct v6 usage:
     float rawK = ta.stoch(high, low, close, 14)  // only K returned
     float k    = ta.sma(rawK, 3)
     float d    = ta.sma(k, 3)

     Adding this to LESSONS_LEARNED.md
     so you never have to ask again."
```

`LESSONS_LEARNED.md` updated automatically. **You'll never need to explain that error again.**

---

#### Step 5 — Next session: full history remembered.

One month later, after fifty different strategies:

```
AI: "Read LESSONS_LEARNED.md. 12 known issues:
     [1] ta.stoch() no tuple
     [2] math.avg() removed
     [3] EMA without volume = fakeout
     [4] repainting needs [1]+lookahead_on
     ... 8 more
     Writing without any of these mistakes."
```

> **Learned once. Remembered forever.**
> This system builds a self-correcting development environment that improves over time.
> The more the repo is used, the smarter it gets.

---

## 🚀 Hızlı Başlangıç / Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

Hangi editörü kullanıyorsun? / Which editor are you using?
→ Aşağıdaki ilgili bölüme git / Jump to the relevant section below.

---

## 🤖 Claude / Claude Code

> **TR: En derin entegrasyon — `CLAUDE.md` aracılığıyla tüm kurallar ve hata hafızası otomatik yüklenir.**
> **EN: Deepest integration — all rules and error memory auto-loaded via `CLAUDE.md`.**

### TR | Türkçe

**Seçenek A — Claude Projects (tarayıcı, önerilen)**

1. [claude.ai/projects](https://claude.ai/projects) adresine git
2. **+ New project** veya mevcut projeyi aç
3. Sağ panel: **Files** → **+** → **GitHub**
4. URL kutusuna:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
5. **pinescriptv6** checkbox → **Add files**
6. Proje sohbetinde artık doğrudan yaz:
   ```
   XU030 için EMA cross stratejisi yaz
   ```

Claude otomatik olarak `LESSONS_LEARNED.md` → `LLM_MANIFEST.md` → referans dosyası sırasını takip eder.

**Seçenek B — Claude Code (terminal)**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```

`CLAUDE.md` otomatik okunur. Artık her istekte Claude hata hafızasını bilir, v5 yazmaz.

---

### EN | English

**Option A — Claude Projects (browser, recommended)**

1. Go to [claude.ai/projects](https://claude.ai/projects)
2. **+ New project** or open existing
3. Right panel: **Files** → **+** → **GitHub**
4. Paste:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
5. **pinescriptv6** checkbox → **Add files**
6. Just chat:
   ```
   Write an EMA cross strategy for ES futures
   ```

**Option B — Claude Code (terminal)**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```

`CLAUDE.md` is read automatically. Claude now knows error memory, never writes v5.

---

## ⌨️ Cursor

> **TR: `.cursor/rules/pinescriptv6.mdc` (v0.44+) veya `.cursorrules` (eski) otomatik yüklenir.**
> **EN: `.cursor/rules/pinescriptv6.mdc` (v0.44+) or `.cursorrules` (older) loads automatically.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
cursor .
```

**TR** — Klasör açılınca kurallar devreye girer. Chat'te `@` ile dosyaları etiketle:

```
@LESSONS_LEARNED.md EMA cross stratejisi yaz, XU030 için
@reference/functions/ta.md RSI divergence indikatörü nasıl yazılır?
@concepts/common_errors.md Bu Pine Script v6 hatasının sebebi ne?
@concepts/signal_quality.md Fakeout filtrelemeli bir strateji yaz
```

**EN** — Rules activate on folder open. Tag files with `@` in chat:

```
@LESSONS_LEARNED.md write an EMA cross strategy for XU030
@reference/functions/ta.md how to write an RSI divergence indicator?
@concepts/common_errors.md what causes this Pine Script v6 error?
@concepts/signal_quality.md write a strategy with fakeout filtering
```

---

## 🌊 Windsurf

> **TR: `.windsurfrules` Windsurf / Cascade tarafından otomatik okunur — sıfır kurulum.**
> **EN: `.windsurfrules` is read automatically by Windsurf / Cascade — zero setup.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
windsurf .
```

**TR** — Cascade chat'te:

```
@LESSONS_LEARNED.md Supertrend + hacim filtreli strateji yaz
@reference/functions/strategy.md ATR tabanlı SL/TP nasıl yazılır?
@concepts/signal_quality.md Fakeout nedir, nasıl filtrerim?
```

**EN** — In Cascade chat:

```
@LESSONS_LEARNED.md write a Supertrend strategy with volume filter
@reference/functions/strategy.md how to write ATR-based SL/TP?
@concepts/signal_quality.md what is a fakeout and how do I filter it?
```

---

## 🐙 GitHub Copilot

> **TR: `.github/copilot-instructions.md` VS Code, JetBrains ve tüm Copilot destekli editörlerde otomatik devreye girer.**
> **EN: `.github/copilot-instructions.md` activates in VS Code, JetBrains, and all Copilot-enabled editors.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
code pinescriptv6
```

**TR** — Copilot Chat'te:

```
LESSONS_LEARNED.md dosyasını önce kontrol et, sonra RSI mean reversion stratejisi yaz.
reference/functions/ta.md dosyasına göre ta.pivothigh() fonksiyonunun imzası nedir?
Bu Pine Script v6 hatasını açıkla: "Cannot use 'series' type as argument"
concepts/signal_quality.md'ye göre hacim onaylı bir EMA cross stratejisi yaz.
```

**EN** — In Copilot Chat:

```
Check LESSONS_LEARNED.md first, then write an RSI mean reversion strategy.
According to reference/functions/ta.md, what is the ta.pivothigh() signature?
Explain this Pine Script v6 error: "Cannot use 'series' type as argument"
According to concepts/signal_quality.md, write a volume-confirmed EMA cross strategy.
```

---

## 🔧 Cline / Roo / Aider

> **TR: `.clinerules` Cline, Roo, Continue ve Aider tarafından otomatik okunur.**
> **EN: `.clinerules` is read automatically by Cline, Roo, Continue, and Aider.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
# Cline veya Roo ile VS Code'dan aç / Open with Cline or Roo from VS Code
```

`.clinerules` otomatik yüklenir. / `.clinerules` loads automatically.

**Aider için / For Aider:**
```bash
aider --read LESSONS_LEARNED.md --read LLM_MANIFEST.md
```

---

## 🤗 Custom GPT / Diğer LLM'ler / Other LLMs

ZIP: [main.zip](https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip)

**TR** — Minimum yükleme + sistem promptu:

```
Bu proje Pine Script v6 geliştirme için optimize edilmiş bir bilgi tabanıdır.
Kod yazmadan önce her zaman LESSONS_LEARNED.md içeriğini kontrol et.
Hangi dosyayı okuyacağını belirlemek için LLM_MANIFEST.md'ye başvur.
Tüm scriptler //@version=6 ile başlamalıdır.
v5 syntax kullanma: study(), security(), bare input() yasak.
Hata alınca LESSONS_LEARNED.md formatında kaydet.
```

**EN** — Minimum upload + system prompt:

```
This project is a knowledge base optimised for Pine Script v6 development.
Always check LESSONS_LEARNED.md before writing any code.
Consult LLM_MANIFEST.md to determine which file to read for each task.
All scripts must start with //@version=6.
Never use v5 syntax: study(), security(), bare input() are forbidden.
On error: save in LESSONS_LEARNED.md format.
```

---

## 📦 Örnekler / Examples

**TR: 55+ hazır Pine Script v6 örneği — TradingView'da test edilmiş, copy-paste hazır.**
**EN: 55+ ready-to-use Pine Script v6 examples — tested in TradingView, copy-paste ready.**

### 📊 İndikatörler / Indicators (18)

| # | Dosya | Açıklama / Description |
|---|-------|------------------------|
| 01 | [`01_ema_cross.pine`](examples/indicators/01_ema_cross.pine) | EMA 9/21 Cross + bgcolor + alerts |
| 02 | [`02_rsi_ob_os.pine`](examples/indicators/02_rsi_ob_os.pine) | RSI 14 Gradient — OB/OS zones |
| 03 | [`03_macd_histogram.pine`](examples/indicators/03_macd_histogram.pine) | MACD 12/26/9 — colored histogram |
| 04 | [`04_bollinger_bands.pine`](examples/indicators/04_bollinger_bands.pine) | Bollinger Bands + squeeze |
| 05 | [`05_supertrend.pine`](examples/indicators/05_supertrend.pine) | Supertrend ATR-based |
| 06 | [`06_vwap_session.pine`](examples/indicators/06_vwap_session.pine) | VWAP + StDev bands |
| 07 | [`07_atr_levels.pine`](examples/indicators/07_atr_levels.pine) | ATR dynamic S/R levels |
| 08 | [`08_pivot_points.pine`](examples/indicators/08_pivot_points.pine) | Classic Pivot Points (Daily) |
| 09 | [`09_volume_profile.pine`](examples/indicators/09_volume_profile.pine) | Volume analysis + OBV |
| 10 | [`10_stoch_rsi.pine`](examples/indicators/10_stoch_rsi.pine) | Stochastic RSI K/D |
| 11 | [`11_ichimoku.pine`](examples/indicators/11_ichimoku.pine) | Ichimoku Cloud — all components |
| 12 | [`12_mtf_ema.pine`](examples/indicators/12_mtf_ema.pine) | Multi-Timeframe EMA D/W/M |
| 13 | [`13_session_highlight.pine`](examples/indicators/13_session_highlight.pine) | Session highlight (VIOP/BIST30) |
| 14 | [`14_rsi_divergence.pine`](examples/indicators/14_rsi_divergence.pine) | RSI Divergence detector |
| 15 | [`15_ema_ribbon.pine`](examples/indicators/15_ema_ribbon.pine) | EMA Ribbon 8/13/21/34/55/89/144/233 |
| 16 | [`16_chandelier_exit.pine`](examples/indicators/16_chandelier_exit.pine) | Chandelier Exit trailing stop |
| 17 | [`17_squeeze_momentum.pine`](examples/indicators/17_squeeze_momentum.pine) | Squeeze Momentum |
| 18 | [`18_fakeout_filter.pine`](examples/indicators/18_fakeout_filter.pine) | **Fakeout Filter — 4-Layer Signal Quality** |

### 🎯 Stratejiler / Strategies (13)

| # | Dosya | Açıklama / Description |
|---|-------|------------------------|
| 01 | [`01_ema_cross_strategy.pine`](examples/strategies/01_ema_cross_strategy.pine) | EMA Cross — ATR SL/TP |
| 02 | [`02_rsi_mean_reversion.pine`](examples/strategies/02_rsi_mean_reversion.pine) | RSI Mean Reversion |
| 03 | [`03_supertrend_strategy.pine`](examples/strategies/03_supertrend_strategy.pine) | Supertrend trend following |
| 04 | [`04_bb_breakout.pine`](examples/strategies/04_bb_breakout.pine) | Bollinger Band Breakout |
| 05 | [`05_macd_strategy.pine`](examples/strategies/05_macd_strategy.pine) | MACD + EMA trend filter |
| 06 | [`06_rsi_atr_strategy.pine`](examples/strategies/06_rsi_atr_strategy.pine) | RSI + ATR — **VIOP/BIST30 optimized** |
| 07 | [`07_mtf_trend_strategy.pine`](examples/strategies/07_mtf_trend_strategy.pine) | Multi-Timeframe trend |
| 08 | [`08_triple_ema_strategy.pine`](examples/strategies/08_triple_ema_strategy.pine) | Triple EMA 5/13/34 |
| 09 | [`09_stoch_strategy.pine`](examples/strategies/09_stoch_strategy.pine) | Stochastic + EMA filter |
| 10 | [`10_adx_trend_strategy.pine`](examples/strategies/10_adx_trend_strategy.pine) | ADX Trend Strength |
| 11 | [`11_viop_session_strategy.pine`](examples/strategies/11_viop_session_strategy.pine) | VIOP Session — seans bazlı |
| 12 | [`12_chandelier_strategy.pine`](examples/strategies/12_chandelier_strategy.pine) | Chandelier Exit Strategy |
| 13 | [`13_fakeout_confirmed_strategy.pine`](examples/strategies/13_fakeout_confirmed_strategy.pine) | **Fakeout-Confirmed — Hacim+HTF+ATR+Bar** |

---

## 🌍 Global Markets (22)

**TR: Dünyanın en çok işlem gören enstrümanları. Her dosyada doğru seans saati, komisyon ve slippage dahil.**
**EN: World's most actively traded instruments. Correct session times, commission and slippage in every file.**

### Temel Stratejiler / Base Strategies (12)

| # | Enstrüman | Sembol | Dosya |
|---|-----------|--------|-------|
| 01 | 🇺🇸 S&P 500 Futures | `CME_MINI:ES1!` / `MES1!` | [`01_es_sp500.pine`](global-markets/01_es_sp500.pine) |
| 02 | 🇺🇸 Nasdaq-100 Futures | `CME_MINI:NQ1!` / `MNQ1!` | [`02_nq_nasdaq.pine`](global-markets/02_nq_nasdaq.pine) |
| 03 | 🥇 Gold Futures | `COMEX:GC1!` / `XAUUSD` | [`03_gc_gold.pine`](global-markets/03_gc_gold.pine) |
| 04 | 🛢️ Crude Oil | `NYMEX:CL1!` | [`04_cl_crude_oil.pine`](global-markets/04_cl_crude_oil.pine) |
| 05 | 💱 EUR/USD | `FX:EURUSD` | [`05_eurusd_forex.pine`](global-markets/05_eurusd_forex.pine) |
| 06 | 💱 GBP/USD | `FX:GBPUSD` | [`06_gbpusd_forex.pine`](global-markets/06_gbpusd_forex.pine) |
| 07 | 💱 USD/JPY | `FX:USDJPY` | [`07_usdjpy_forex.pine`](global-markets/07_usdjpy_forex.pine) |
| 08 | 🪙 Bitcoin | `BINANCE:BTCUSDT` | [`08_btc_crypto.pine`](global-markets/08_btc_crypto.pine) |
| 09 | 🪙 Ethereum | `BINANCE:ETHUSDT` | [`09_eth_crypto.pine`](global-markets/09_eth_crypto.pine) |
| 10 | 🇩🇪 DAX Germany | `XETR:DAX` | [`10_dax_germany.pine`](global-markets/10_dax_germany.pine) |
| 11 | 🇯🇵 Nikkei 225 | `TVC:NI225` | [`11_nikkei_japan.pine`](global-markets/11_nikkei_japan.pine) |
| 12 | 🌍 Universal | `syminfo.tickerid` | [`12_universal_strategy.pine`](global-markets/12_universal_strategy.pine) |

### Gelişmiş Stratejiler / Advanced Strategies (10)

| # | Enstrüman | Strateji | Dosya |
|---|-----------|----------|-------|
| 13 | 🪙 BTC | EMA Trend + RSI Pullback Entry | [`13_btc_trend_pullback.pine`](global-markets/13_btc_trend_pullback.pine) |
| 14 | 🪙 ETH | Volume-Confirmed Momentum Breakout | [`14_eth_momentum.pine`](global-markets/14_eth_momentum.pine) |
| 15 | 🇺🇸 ES | Opening Range Breakout (ORB) | [`15_es_opening_range.pine`](global-markets/15_es_opening_range.pine) |
| 16 | 🇺🇸 NQ | VWAP Mean Reversion | [`16_nq_vwap_reversion.pine`](global-markets/16_nq_vwap_reversion.pine) |
| 17 | 🥇 Gold | Triple EMA + ADX Trend | [`17_gc_gold_trend.pine`](global-markets/17_gc_gold_trend.pine) |
| 18 | 🛢️ CL | ATR Momentum + EIA Filter | [`18_cl_crude_momentum.pine`](global-markets/18_cl_crude_momentum.pine) |
| 19 | 💱 EURUSD | London Session Breakout | [`19_eurusd_london_breakout.pine`](global-markets/19_eurusd_london_breakout.pine) |
| 20 | 💱 GBPUSD | Market Structure + EMA Filter | [`20_gbpusd_structure.pine`](global-markets/20_gbpusd_structure.pine) |
| 21 | 💱 USDJPY | Carry Trade Trend Following | [`21_usdjpy_carry_trend.pine`](global-markets/21_usdjpy_carry_trend.pine) |
| 22 | 🇩🇪 DAX | Gap Fade + Xetra Session | [`22_dax_gap_fade.pine`](global-markets/22_dax_gap_fade.pine) |

---

## 🔔 Webhook Templates (7)

**TR: TradingView alertlerini Telegram, Discord ve broker API'lerine iletmek için hazır şablonlar.**
**EN: Ready templates for forwarding TradingView alerts to Telegram, Discord, and broker APIs.**

| Dosya | Açıklama / Description |
|-------|------------------------|
| [`01_alert_message_templates.md`](webhook-templates/01_alert_message_templates.md) | `{{ticker}}`, `{{close}}`, `{{strategy.order.action}}` — tüm dinamik değişkenler |
| [`02_pine_alert_conditions.pine`](webhook-templates/02_pine_alert_conditions.pine) | `alertcondition()` + `alert()` — tam çalışan örnekler |
| [`03_telegram_webhook.md`](webhook-templates/03_telegram_webhook.md) | Telegram Bot + Python server — adım adım kurulum |
| [`04_discord_webhook.md`](webhook-templates/04_discord_webhook.md) | Discord webhook + embed mesajlar |
| [`05_json_payload_templates.md`](webhook-templates/05_json_payload_templates.md) | Broker API JSON — buy/sell/position şablonları |
| [`06_viop_bist30_alerts.pine`](webhook-templates/06_viop_bist30_alerts.pine) | VİOP / BIST30 — seans filtreli, komisyon ayarlı |

---

## 🔄 v5 → v6 Migration (10)

**TR: v5 kodlarını v6'ya taşırken en sık karşılaşılan değişiklikler.**
**EN: Most common changes when migrating v5 code to v6.**

| Dosya | Konu / Topic |
|-------|-------------|
| [`01_study_to_indicator.md`](v5-to-v6-migration/01_study_to_indicator.md) | `study()` → `indicator()` — en yaygın hata |
| [`02_security_to_request.md`](v5-to-v6-migration/02_security_to_request.md) | `security()` → `request.security()` |
| [`03_strategy_syntax.md`](v5-to-v6-migration/03_strategy_syntax.md) | Strategy declaration değişiklikleri |
| [`04_type_system.md`](v5-to-v6-migration/04_type_system.md) | Explicit type — `int`, `float`, `bool` |
| [`05_arrays_and_collections.md`](v5-to-v6-migration/05_arrays_and_collections.md) | `array.new_float()` → `array.new<float>()` |
| [`06_input_functions.md`](v5-to-v6-migration/06_input_functions.md) | `input()` → `input.int()`, `input.float()`... |
| [`07_drawing_objects.md`](v5-to-v6-migration/07_drawing_objects.md) | `line`, `label`, `box` — `chart.point` yeniliği |
| [`08_pine_logs.md`](v5-to-v6-migration/08_pine_logs.md) | Yeni: `log.info()`, `log.warning()`, `log.error()` |
| [`09_methods_and_udt.md`](v5-to-v6-migration/09_methods_and_udt.md) | Yeni: User-defined types + methods |
| [`10_common_migration_errors.md`](v5-to-v6-migration/10_common_migration_errors.md) | 7 yaygın geçiş hatası ve çözümleri |

---

## 📁 Dosya Yapısı / File Structure

```
pinescriptv6/
│
├── CLAUDE.md                    → Claude Code + Claude Projects
├── AGENTS.md                    → Devin, OpenAI Codex, autonomous agents
├── LESSONS_LEARNED.md           Hata hafızası / Error memory (AI auto-updates)
├── LLM_MANIFEST.md              Sorgu yönlendirme / Query routing map
├── SKILL.md                     AI yazma protokolü / AI writing protocol
│
├── assets/
│   ├── demo_chart.png           XU030 live demo screenshot
│   └── lessons_flow.png         System flow diagram
│
├── .cursor/rules/
│   └── pinescriptv6.mdc         → Cursor v0.44+
├── .cursorrules                 → Cursor (legacy fallback)
├── .windsurfrules               → Windsurf / Cascade
├── .clinerules                  → Cline, Roo, Continue, Aider
├── .zed/rules                   → Zed editor
├── .github/
│   └── copilot-instructions.md  → GitHub Copilot
│
├── concepts/
│   ├── execution_model.md       var, varip, barstate — nasıl çalışır
│   ├── common_errors.md         max_bars_back, series type — yaygın hatalar
│   ├── timeframes.md            request.security, repainting — MTF
│   ├── colors_and_display.md    color.new, gradients — renk sistemi
│   ├── methods.md               user-defined methods — metodlar
│   ├── objects.md               UDT, type system — nesneler
│   └── signal_quality.md        Fakeout filters — volume, MTF, ATR, bar confirm
│
├── reference/
│   ├── variables.md             open, close, bar_index, syminfo
│   ├── constants.md             color.*, shape.*, plot.style_*
│   ├── types.md                 series, simple, input, const
│   ├── keywords.md              if, for, var, varip, switch
│   ├── annotations.md           @version, @param, @returns
│   └── functions/
│       ├── ta.md                RSI, EMA, MACD, ATR, crossover, pivot
│       ├── strategy.md          entry, exit, close, position_size
│       ├── drawing.md           plot, line, box, label, table, fill
│       ├── request.md           security, financial, MTF
│       ├── collections.md       array, map, matrix
│       └── general.md           math, str, input, alert, timestamp
│
├── writing_scripts/
│   ├── style_guide.md           Kod stili, isimlendirme, girintileme
│   ├── debugging.md             Pine Logs, debug teknikleri
│   ├── profiling_and_optimization.md  Performans optimizasyonu
│   └── limitations.md           Script limitleri, max_bars_back
│
├── examples/
│   ├── indicators/   (18 — copy-paste ready, tested in TradingView)
│   └── strategies/   (13 — copy-paste ready, tested in TradingView)
│
├── global-markets/   (22 — ES, NQ, BTC, ETH, Gold, Forex, DAX, Nikkei)
├── webhook-templates/ (7 — Telegram, Discord, JSON, VIOP)
└── v5-to-v6-migration/ (10 — full migration guide)
```

---

## 📜 Lisans / License

MIT — [LICENSE](LICENSE) · Copyright © 2025 [Ugur Pala](https://github.com/trugurpala)

**Yazar / Author:**
[TradingView](https://tr.tradingview.com/u/trugurpala/) · [X / Twitter](https://x.com/trugurpala) · mail@ugurpala.com

> TR: TradingView'ın resmi Pine Script v6 dokümantasyonu temel referans materyali olarak kullanılmıştır. TradingView bu projeyle hiçbir resmi bağlantısı veya onayı bulunmamaktadır.
>
> EN: The official TradingView Pine Script v6 documentation was used as primary reference material. TradingView is not affiliated with or endorsing this project.

---

<div align="center">

**TR: Bu repo Pine Script v6 yazarken zaman kazandırdıysa, bir yıldız vermek başkalarının da bulmasını sağlar.**
**EN: If this repo saved you time writing Pine Script v6, starring it helps others find it too.**

⭐ **[Star this repo](https://github.com/trugurpala/pinescriptv6)** ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=trugurpala/pinescriptv6&type=Date)](https://star-history.com/#trugurpala/pinescriptv6&Date)

</div>



---

## Source: reference\annotations.md

# Annotations
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TR: Kod belgelemeleri ve metadata için kullanılan annotation'lar. EN: Annotations for documentation and metadata.

---

## @version
```pine
//@version=6
```

## @description — Library açıklaması
```pine
// @description RSI + EMA kombinasyonu için yardımcı fonksiyonlar.
// @description Helper functions for RSI + EMA combinations.
library("MyLibrary")
```

## @function
```pine
// @function Verilen uzunlukta EMA hesaplar.
// @function Calculates EMA for the given length.
// @param src  (series float) Kaynak seri / Source series
// @param len  (simple int)  Periyod / Period
// @returns    (series float) EMA değeri / EMA value
export myEma(series float src, simple int len) =>
    ta.ema(src, len)
```

## @param
```pine
// @param length (simple int) RSI periyodu. Min: 1, Max: 500
```

## @returns
```pine
// @returns (series bool) Kesişim olduğunda true döner.
// @returns (series bool) Returns true when crossover occurs.
```

## @type ve @field
```pine
// @type Grafik üzerindeki bir pivot noktasını temsil eder.
// @type Represents a pivot point on the chart.
// @field index (int)   Bar indexi / Bar index
// @field price (float) Fiyat seviyesi / Price level
type PivotPoint
    int   index
    float price
```

## @strategy_alert_message
```pine
//@strategy_alert_message {{strategy.order.action}} @ {{close}}
```



---

## Source: reference\constants.md

# Constants
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TR: Fonksiyon argümanlarında kullanılan sabit değerler. EN: Fixed constants used as function arguments.

---

## color.*
```pine
color.red     color.green   color.blue    color.orange  color.yellow
color.white   color.black   color.gray    color.lime    color.aqua
color.fuchsia color.navy    color.olive   color.maroon  color.purple
color.teal    color.silver
```

## shape.* — plotshape için / for plotshape
```pine
shape.circle       shape.cross       shape.diamond     shape.flag
shape.square       shape.triangleup  shape.triangledown
shape.arrowup      shape.arrowdown   shape.xcross
shape.labelup      shape.labeldown
```

## plot.style_*
```pine
plot.style_line      plot.style_linebr    plot.style_stepline
plot.style_area      plot.style_areabr    plot.style_columns
plot.style_histogram plot.style_circles   plot.style_cross
```

## size.*
```pine
size.tiny   size.small   size.normal   size.large   size.huge   size.auto
```

## location.*
```pine
location.abovebar   location.belowbar   location.top
location.bottom     location.absolute
```

## line.style_*
```pine
line.style_solid   line.style_dashed   line.style_dotted   line.style_arrow_right
```

## hline.style_*
```pine
hline.style_solid   hline.style_dashed   hline.style_dotted
```

## label.style_*
```pine
label.style_label_down   label.style_label_up     label.style_label_left
label.style_label_right  label.style_label_center label.style_none
label.style_text_outline label.style_circle       label.style_square
label.style_diamond      label.style_flag         label.style_cross
```

## alert.freq_*
```pine
alert.freq_once_per_bar         // bar başına bir kez
alert.freq_once_per_bar_close   // sadece kapanışta
alert.freq_all                  // her tickte
```

## extend.*
```pine
extend.none   extend.right   extend.left   extend.both
```

## position.*
```pine
position.top_left    position.top_center    position.top_right
position.middle_left position.middle_center position.middle_right
position.bottom_left position.bottom_center position.bottom_right
```

## Örnek / Example
```pine
plotshape(buySignal,
    style    = shape.triangleup,
    location = location.belowbar,
    color    = color.green,
    size     = size.small,
    title    = "Buy")
```



---

## Source: reference\functions\collections.md

# Collections — array / map / matrix
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## array<type>

### Oluşturma / Create
```pine
var arr  = array.new<float>(0)          // boş / empty
var arr2 = array.new<float>(10, 0.0)    // 10 eleman, hepsi 0 / 10 elements, all 0
var arr3 = array.new<int>(5, na)
```

### Eleman İşlemleri / Element Operations
```pine
arr.push(close)              // sona ekle / add to end
arr.unshift(close)           // başa ekle / add to start
arr.insert(2, close)         // index 2'ye ekle / insert at index 2
float last  = arr.pop()      // sondan sil / remove from end
float first = arr.shift()    // baştan sil / remove from start
arr.remove(2)                // index 2'yi sil / remove at index 2
arr.clear()                  // hepsini temizle / clear all
```

### Erişim / Access
```pine
arr.get(0)                   // 0. eleman
arr.set(0, close)            // güncelle / update
arr.size()                   // eleman sayısı / element count
arr.first()                  // ilk / first
arr.last()                   // son / last
```

### Hesaplama / Calculation
```pine
arr.avg()     arr.max()     arr.min()
arr.sum()     arr.stdev()   arr.median()   arr.variance()
```

### Diger / Other
```pine
arr.sort()                        // küçükten büyüğe / ascending
arr.sort(order.descending)        // büyükten küçüğe / descending
arr.reverse()
arr.slice(from, to)               // dilim / slice (yeni array / new array)
arr.copy()
arr.includes(val)                 // var mı? / contains?
arr.indexof(val)                  // ilk index (-1 yoksa)
arr.join(", ")                    // string'e / to string
```

### Sliding Window Örneği / Example
```pine
//@version=6
indicator("Rolling Stats")
var arr = array.new<float>(20, na)
arr.push(close)
arr.shift()    // boyut 20'de sabit / size stays at 20
plot(arr.avg(),   "Ortalama / Avg",  color.blue)
plot(arr.stdev(), "StDev", color.orange)
```

---

## map<keyType, valueType>
```pine
var m = map.new<string, float>()
m.put("rsi", ta.rsi(close, 14))
m.put("atr", ta.atr(14))

float rsiVal = m.get("rsi")    // değer al / get value
m.remove("rsi")                // sil / remove
bool hasKey = m.contains("atr") // var mı?
int  sz     = m.size()
array<string> keys = m.keys()
array<float>  vals = m.values()
```

---

## matrix<type>
```pine
var mat = matrix.new<float>(3, 3, 0.0)  // 3x3, hepsi 0
mat.set(0, 0, close)    // (satır, sütun, değer) / (row, col, value)
float val = mat.get(0, 0)
int rows  = mat.rows()
int cols  = mat.columns()
array<float> row0 = mat.row(0)
matrix.mult(mat1, mat2)          // matris çarpımı / matrix multiplication
mat.transpose()                  // devrik / transpose
```



---

## Source: reference\functions\drawing.md

# Drawing
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## plot()
```pine
plot(close, "Kapanış", color.blue, linewidth=2)
plot(close, style=plot.style_histogram)
plot(na)    // görünmez placeholder
```

## plotshape()
```pine
plotshape(buySignal,
    style    = shape.triangleup,
    location = location.belowbar,
    color    = color.green,
    size     = size.small,
    title    = "Al")

plotshape(sellSignal,
    style    = shape.triangledown,
    location = location.abovebar,
    color    = color.red,
    size     = size.small,
    title    = "Sat")
```

## hline()
```pine
hline(70, "Aşırı Alım", color.red,   linestyle=hline.style_dashed)
hline(30, "Aşırı Satım", color.green, linestyle=hline.style_dashed)
hline(50, "Orta",        color.gray,  linestyle=hline.style_dotted)
```

## bgcolor()
```pine
bgcolor(isSession ? color.new(color.blue, 92) : na)
bgcolor(close > open ? color.new(color.green, 95) : color.new(color.red, 95))
```

## line.new()
```pine
// Sadece son çizgiyi tut / Keep only the last line
var line myLine = na
if barstate.islast
    line.delete(myLine)
    myLine := line.new(
        bar_index - 10, ta.lowest(10),
        bar_index,      ta.highest(10),
        color = color.orange, width = 2,
        style = line.style_dashed)
```

## box.new()
```pine
var box myBox = na
box.delete(myBox[1])
myBox := box.new(
    bar_index - 20, ta.highest(20),
    bar_index,      ta.lowest(20),
    border_color = color.blue,
    bgcolor      = color.new(color.blue, 90))
```

## label.new()
```pine
if ta.pivothigh(high, 5, 5)
    label.new(bar_index[5], high[5],
        "PH: " + str.tostring(high[5], format.mintick),
        style     = label.style_label_down,
        color     = color.red,
        textcolor = color.white)
```

## fill()
```pine
p1 = plot(ta.ema(close, 9),  color=color.green)
p2 = plot(ta.ema(close, 21), color=color.red)
fill(p1, p2, color=color.new(color.blue, 85))
```

## table.new()
```pine
var table infoTable = table.new(
    position.top_right, 2, 3,
    bgcolor      = color.new(color.black, 70),
    border_width = 1)

if barstate.islast
    table.cell(infoTable, 0, 0, "RSI", text_color=color.gray)
    table.cell(infoTable, 1, 0,
        str.tostring(math.round(ta.rsi(close, 14), 1)),
        text_color = color.yellow)
    table.cell(infoTable, 0, 1, "ATR", text_color=color.gray)
    table.cell(infoTable, 1, 1,
        str.tostring(math.round(ta.atr(14), 2)),
        text_color = color.yellow)
```



---

## Source: reference\functions\general.md

# General — math / str / input / alert
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## math.*
```pine
math.abs(x)               // mutlak değer / absolute value
math.round(x)             // en yakın tam sayı / nearest integer
math.round(x, decimals)   // ondalık basamak / decimal places
math.floor(x)             // aşağı yuvarla / floor
math.ceil(x)              // yukarı yuvarla / ceiling
math.max(a, b, c...)      // maksimum
math.min(a, b, c...)      // minimum
math.pow(base, exp)       // üs / power
math.sqrt(x)              // kare kök / square root
math.log(x)               // doğal logaritma / natural log
math.log10(x)             // log base 10
math.sign(x)              // işaret / sign: -1, 0 or 1
math.random(min, max)     // rastgele / random
math.pi                   // 3.14159...
math.phi                  // altın oran / golden ratio
```

## str.* — String
```pine
str.tostring(val)                    // her şey → string / anything to string
str.tostring(3.14, "#.##")           // formatlı / formatted
str.tostring(close, format.mintick)  // mintick formatı
str.tonumber(str)                    // string → float
str.toint(str)                       // string → int
str.length(str)
str.upper(str)                       // büyük harf / uppercase
str.lower(str)                       // küçük harf / lowercase
str.trim(str)                        // boşlukları temizle / trim whitespace
str.contains(str, sub)               // içeriyor mu? / contains?
str.startswith(str, prefix)
str.endswith(str, suffix)
str.replace(str, target, rep)        // ilk bulduğu / first occurrence
str.replace_all(str, target, rep)    // hepsini / all occurrences
str.split(str, sep)                  // array<string> döndürür
str.substring(str, from, to)
str.format("{0} @ {1}", syminfo.ticker, close)
```

## input.*
```pine
input.int(14,    "RSI Periyodu",   minval=1, maxval=500)
input.float(2.0, "ATR Çarpan",    step=0.1)
input.bool(true, "Sinyal Göster")
input.string("D", "Timeframe",    options=["1","5","15","60","D","W","M"])
input.source(close, "Kaynak")
input.color(color.red, "Renk")
input.time(timestamp("2024-01-01"), "Başlangıç")
```

## alert()
```pine
// Dinamik alert — kod içinde tetiklenir
alert("RSI aşağı kesti: " + str.tostring(rsi), alert.freq_once_per_bar)
alert("Fiyat: " + str.tostring(close),         alert.freq_once_per_bar_close)
alert(msg,                                      alert.freq_all)

// Statik alert — kullanıcı TradingView'da tetikler
alertcondition(buySignal,  "Al Sinyali",  "Al: {{close}}")
alertcondition(sellSignal, "Sat Sinyali", "Sat: {{close}}")
```

## Zaman / Time
```pine
timestamp("2024-01-01")
timestamp("UTC+3", 2024, 1, 1, 9, 30, 0)

year(time), month(time), dayofmonth(time)
hour(time), minute(time), second(time)
dayofweek(time)   // 1=Pazar/Sunday ... 7=Cumartesi/Saturday
timenow           // şu anki Unix ms

// Seans kontrolü / Session check
isSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
```



---

## Source: reference\functions\request.md

# request.*
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## request.security() — Temel / Basic
```pine
// Farklı timeframe / Different timeframe
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))

// Farklı sembol / Different symbol
btcClose   = request.security("BINANCE:BTCUSDT", "D", close)
xu030Daily = request.security("BIST:XU030", "D", close)
```

## Repainting Önleme / Prevent Repainting
```pine
// ❌ Canlı bar — repainting yapabilir / Live bar — may repaint
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Kapanmış bar — güvenli / Confirmed bar — safe
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

## Çoklu Değer — Tuple / Multiple Values
```pine
[htfOpen, htfHigh, htfLow, htfClose] =
    request.security(syminfo.tickerid, "D", [open, high, low, close])
```

## Alt Timeframe / Lower Timeframe
```pine
// array<float> döndürür / returns array<float>
lowerCloses = request.security_lower_tf(syminfo.tickerid, "1", close)
```

## request.financial()
```pine
pe  = request.financial(syminfo.tickerid, "P_E",                  "TTM")
eps = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE",    "FQ")
rev = request.financial(syminfo.tickerid, "TOTAL_REVENUE",         "FY")
```

## request.currency_rate()
```pine
usdtry = request.currency_rate("USD", "TRY")
eurusd = request.currency_rate("EUR", "USD")
```

## Limitler / Limits
- TR: Bir scriptte maksimum 40 `request.security()` çağrısı
- EN: Maximum 40 `request.security()` calls per script
- TR: Performans için çağrıları birleştir (tuple kullan)
- EN: Combine calls for performance (use tuple)



---

## Source: reference\functions\strategy.md

# strategy.*
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## Deklarasyon / Declaration
```pine
//@version=6
strategy("Strateji Adı",
    overlay                   = true,
    initial_capital           = 10000,
    default_qty_type          = strategy.percent_of_equity,
    default_qty_value         = 10,
    commission_type           = strategy.commission.percent,
    commission_value          = 0.1,
    slippage                  = 1,
    calc_on_every_tick        = false,
    process_orders_on_close   = false)
```

## Pozisyon Açma / Entry
```pine
strategy.entry("Long",  strategy.long)                // piyasadan / market
strategy.entry("Short", strategy.short)
strategy.entry("Long",  strategy.long,  limit = 1500.0)   // limit emir
strategy.entry("Long",  strategy.long,  stop  = 1600.0)   // stop emir
strategy.entry("Long",  strategy.long,  qty   = 100)      // lot miktarı
```

## Çıkış / Exit
```pine
strategy.close("Long")         // ID ile kapat / close by ID
strategy.close_all()           // hepsini kapat

strategy.exit("Exit", "Long",
    profit       = 100,   // tick cinsinden kâr hedefi
    loss         = 50,    // tick cinsinden zarar durdurucu
    trail_points = 20,    // trailing stop (tick)
    trail_offset = 10)    // trailing offset (tick)
```

## İptal / Cancel
```pine
strategy.cancel("Long")        // bekleyen emri iptal
strategy.cancel_all()
```

## Bilgi Değişkenleri / Info Variables
```pine
strategy.position_size        // + long, - short, 0 yok
strategy.equity               // toplam sermaye
strategy.netprofit            // net kâr
strategy.grossprofit          // brüt kâr
strategy.grossloss            // brüt zarar
strategy.opentrades           // açık işlem sayısı
strategy.closedtrades         // kapanmış işlem
strategy.position_avg_price   // ortalama giriş
strategy.wintrades            // kazanan
strategy.losstrades           // kaybeden
```

## Örnek — ATR Tabanlı Stop/Take-Profit
```pine
//@version=6
strategy("ATR SL/TP", overlay=true)

int   lenInput  = input.int(14,  "ATR Periyodu")
float slMult    = input.float(2.0, "SL Çarpan", step=0.1)
float tpMult    = input.float(3.0, "TP Çarpan", step=0.1)

ema   = ta.ema(close, 50)
atr14 = ta.atr(lenInput)

if ta.crossover(close, ema) and strategy.position_size == 0
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long",
        stop   = close - slMult * atr14,
        limit  = close + tpMult * atr14)

plot(ema, "EMA 50", color.orange)
```



---

## Source: reference\functions\ta.md

# ta.* — Technical Analysis
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## Hareketli Ortalamalar / Moving Averages
```pine
ta.sma(source, length)               // Basit / Simple
ta.ema(source, length)               // Üstel / Exponential
ta.wma(source, length)               // Ağırlıklı / Weighted
ta.rma(source, length)               // RSI MA (alpha = 1/length)
ta.vwma(source, length)              // Hacim ağırlıklı / Volume-weighted
ta.hma(source, length)               // Hull
ta.alma(source, length, offset, sigma) // Arnaud Legoux
ta.swma(source)                      // Symmetric weighted (4 bar)
```

## Osilatörler / Oscillators
```pine
ta.rsi(source, length)
[macd, signal, hist] = ta.macd(source, fastLength, slowLength, signalLength)
ta.cci(source, length)
ta.cmo(source, length)                // Chande Momentum
ta.mfi(source, length)                // Money Flow Index
ta.roc(source, length)                // Rate of Change
[k, d] = ta.stoch(high, low, close, length)
ta.tsi(source, shortLength, longLength)
```

## Volatilite / Volatility
```pine
ta.atr(length)
[upper, basis, lower] = ta.bb(source, length, mult)  // Bollinger Bands
ta.bbw(source, length, mult)          // BB Width
ta.tr(handle_na)                      // True Range
ta.kc(source, length, mult)           // Keltner Channel — returns [upper, basis, lower]
```

## Kesişimler / Crossovers
```pine
ta.crossover(source1, source2)        // source1 yukarı kesti / crossed up
ta.crossunder(source1, source2)       // source1 aşağı kesti / crossed down
ta.cross(source1, source2)            // her yönde / either direction
```

## Min / Max / Pivot
```pine
ta.highest(source, length)            // en yüksek / highest value
ta.lowest(source, length)             // en düşük / lowest value
ta.highestbars(source, length)        // kaç bar önce / bars since highest
ta.lowestbars(source, length)         // kaç bar önce / bars since lowest
ta.pivothigh(source, leftBars, rightBars)  // na döner yoksa / returns na if no pivot
ta.pivotlow(source, leftBars, rightBars)
```

## Yardımcılar / Helpers
```pine
ta.change(source)                     // 1 barlık değişim / 1-bar change
ta.change(source, length)             // n barlık değişim
ta.cum(source)                        // kümülatif toplam / cumulative sum
ta.falling(source, length)            // düşüşte mi? / falling?
ta.rising(source, length)             // yükseliyor mu? / rising?
ta.barssince(condition)               // son koşuldan beri kaç bar / bars since condition
ta.valuewhen(condition, source, occurrence) // n. koşul anındaki değer / value at nth condition
ta.range(source, length)              // max - min
```

## Örnek — BIST30 EMA Cross + RSI Filtresi
```pine
//@version=6
strategy("EMA Cross + RSI Filter — XU030", overlay=false)

ema9  = ta.ema(close, 9)
ema21 = ta.ema(close, 21)
rsi14 = ta.rsi(close, 14)
atr14 = ta.atr(14)

longCond  = ta.crossover(ema9, ema21) and rsi14 > 50
shortCond = ta.crossunder(ema9, ema21) and rsi14 < 50

if longCond
    strategy.entry("Long", strategy.long)
if shortCond
    strategy.entry("Short", strategy.short)

plot(rsi14, "RSI", color.blue)
hline(70, "OB", color.red)
hline(50, "Mid", color.gray)
hline(30, "OS", color.green)
```



---

## Source: reference\keywords.md

# Keywords
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Kontrol Akışı / Control Flow

```pine
// if / else if / else
if close > open
    strategy.entry("Long", strategy.long)
else if close < open
    strategy.entry("Short", strategy.short)
else
    strategy.close_all()

// switch
switch timeframe.period
    "D" => bgcolor(color.new(color.blue, 90))
    "W" => bgcolor(color.new(color.green, 90))
    => bgcolor(na)  // default

// for
for i = 0 to 9
    sum += close[i]

// for..in — array üzerinde
for [i, val] in myArray
    total += val

// while
while condition
    counter += 1
```

### Değişken Bildirimi

```pine
var float cumSum = 0.0    // kalıcı — bir kere başlatılır
varip int ticks = 0       // rollback'e dirençli

// Tip opsiyoneldir — Pine çıkarabilir
myVar = close * 2
```

### Fonksiyon Tanımı

```pine
// Normal fonksiyon
myFunc(float x, int len) =>
    ta.ema(x, len) * 2

// Method
method myMethod(array<float> arr, float val) =>
    arr.push(val)
    arr
```

### import / export — Library

```pine
// Kullanım
import username/libraryName/1 as lib
result = lib.myFunction(close)

// Tanım (library script içinde)
export myFunc(float x) =>
    x * 2
```

---

## EN | English

### Control Flow

```pine
// if / else if / else
if close > open
    strategy.entry("Long", strategy.long)
else if close < open
    strategy.entry("Short", strategy.short)
else
    strategy.close_all()

// switch
switch timeframe.period
    "D" => bgcolor(color.new(color.blue, 90))
    "W" => bgcolor(color.new(color.green, 90))
    => bgcolor(na)  // default

// for
for i = 0 to 9
    sum += close[i]

// for..in — over array
for [i, val] in myArray
    total += val
```

### Variable Declaration

```pine
var float cumSum = 0.0    // persistent — initialized once
varip int ticks = 0       // rollback-resistant

// Type is optional — Pine can infer
myVar = close * 2
```

### Function Definition

```pine
// Regular function
myFunc(float x, int len) =>
    ta.ema(x, len) * 2

// Method
method myMethod(array<float> arr, float val) =>
    arr.push(val)
    arr
```



---

## Source: reference\types.md

# Types
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Temel Tipler
```pine
int     // tam sayı
float   // ondalıklı sayı
bool    // true / false
string  // metin
color   // renk değeri
```

### Özel Tipler
```pine
line      linefill    box       polyline
label     table       chart.point
array<T>  matrix<T>  map<K,V>
```

### Tip Niteleyicileri

| Niteleyici | Anlam |
|------------|-------|
| `const` | Derleme zamanında sabit |
| `simple` | Script başlarken bir kere belirlenir |
| `input` | Kullanıcı tarafından belirlenir |
| `series` | Her barda değişebilir (en esnek) |

Esneklik sırası: `const` → `simple` → `input` → `series`

### Tip Dönüşümü
```pine
int(3.7)                     // 3
float(3)                     // 3.0
str.tostring(3.14)           // "3.14"
str.tostring(3.14, "#.##")   // "3.14"
str.tofloat("3.14")          // 3.14
str.toint("42")              // 42
```

### na Kontrolü
```pine
na(close)          // true ise close na
nz(close, 0.0)     // close na ise 0.0 döndür
not na(myVar)      // na değilse
```

---

## EN | English

### Basic Types
```pine
int     // integer
float   // decimal
bool    // true / false
string  // text
color   // color value
```

### Special Types
```pine
line      linefill    box       polyline
label     table       chart.point
array<T>  matrix<T>  map<K,V>
```

### Type Qualifiers

| Qualifier | Meaning |
|-----------|---------|
| `const` | Fixed at compile time |
| `simple` | Determined once at script start |
| `input` | Determined by user |
| `series` | Can change on every bar (most flexible) |

Flexibility order: `const` → `simple` → `input` → `series`

### Type Conversion
```pine
int(3.7)                     // 3
float(3)                     // 3.0
str.tostring(3.14)           // "3.14"
str.tostring(3.14, "#.##")   // "3.14"
str.tofloat("3.14")          // 3.14
str.toint("42")              // 42
```

### na Check
```pine
na(close)          // true if close is na
nz(close, 0.0)     // return 0.0 if close is na
not na(myVar)      // if not na
```



---

## Source: reference\variables.md

# Variables
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TR: Yerleşik değişkenler. EN: Built-in read-only variables.

---

## Fiyat / Price
```pine
open, high, low, close    // OHLC
volume                    // hacim / volume
vwap                      // gün içi VWAP
hl2                       // (high + low) / 2
hlc3                      // (high + low + close) / 3
ohlc4                     // (open + high + low + close) / 4
hlcc4                     // (high + low + close + close) / 4
```

## Bar & Zaman / Bar & Time
```pine
bar_index    // 0'dan başlar, her yeni barda 1 artar
time         // Unix ms — açılış zamanı
time_close   // Unix ms — kapanış zamanı
timenow      // Unix ms — şu an
```

## Sembol / Symbol
```pine
syminfo.ticker          // "XU030"
syminfo.tickerid        // "BIST:XU030"
syminfo.exchange        // "BIST"
syminfo.description     // tam açıklama
syminfo.type            // "futures", "stock" vb.
syminfo.currency        // "TRY", "USD"
syminfo.mintick         // minimum fiyat adımı
syminfo.pointvalue      // nokta değeri
```

## Timeframe
```pine
timeframe.period        // "1", "D", "W" — mevcut grafik
timeframe.multiplier    // sayısal çarpan
timeframe.isminutes     // true ise dakika bazlı
timeframe.ishours       // true ise saatlik
timeframe.isdaily       // true ise günlük
timeframe.isweekly      // true ise haftalık
timeframe.ismonthly     // true ise aylık
timeframe.in_seconds()  // saniye cinsinden
```

## Strateji / Strategy
```pine
strategy.equity              // toplam sermaye
strategy.position_size       // + long, - short, 0 yok
strategy.position_avg_price  // ortalama giriş fiyatı
strategy.netprofit           // net kâr
strategy.grossprofit         // brüt kâr
strategy.grossloss           // brüt zarar
strategy.opentrades          // açık işlem sayısı
strategy.closedtrades        // kapanmış işlem sayısı
strategy.wintrades           // kazanan işlem
strategy.losstrades          // kaybeden işlem
```

## Örnek / Example
```pine
//@version=6
indicator("Variables demo", overlay=true)
label.new(bar_index, high,
    syminfo.ticker + " | " + str.tostring(close, format.mintick),
    style=label.style_label_down)
```



---

## Source: SKILL.md

---
name: pinescript-v6
description: "Pine Script v6 uzman geliştirici skill'i — doğru v6 kodu yazar, hataları takip eder, LESSONS_LEARNED'i günceller."
maintainer: Ugur Pala · mail@ugurpala.com
repo: github.com/trugurpala/pinescriptv6
tradingview: https://tr.tradingview.com/u/trugurpala/
triggers:
  - Pine Script
  - PineScript
  - indicator
  - strategy
  - TradingView
  - indikatör
  - strateji
  - v6
  - pine
  - VIOP
  - VİOP
  - BIST30
---

# Pine Script v6 — Skill

## Proje Bağlamı / Project Context

Bu skill **trugurpala/pinescriptv6** reposuna aittir.
- **Sahibi:** Ugur Pala · mail@ugurpala.com
- **GitHub:** github.com/trugurpala
- **TradingView:** https://tr.tradingview.com/u/trugurpala/
- **Vitrin:** github.com/trugurpala/awesome-pinescript-v6
- **Hedef:** Türkiye VİOP / BIST30 futures + global piyasalar için Pine Script v6
- **İçerik:** 56 Pine dosyası · 14 strateji · 18 indikatör · 22 global market · 245 commit

---

## Görev

Pine Script v6 ile doğru, optimize edilmiş kod yaz.
Kod yazmadan önce LESSONS_LEARNED.md ve referansları oku.
Hata çözümlerini hemen LESSONS_LEARNED.md'ye kaydet.

---

## Protokol

### 1. Kod Yazmadan Önce
1. **`LESSONS_LEARNED.md` oku** — 11 bilinen hata var, tekrarlama
2. **`LLM_MANIFEST.md`** ile göreve uygun referans dosyasını bul ve oku

### 2. Kod Kuralları
- `//@version=6` — her scriptin ilk satırı, istisnasız
- `ta.*` kullan — manuel hesaplama yazma
- `var` / `varip` — execution model'e göre doğru kullan
- Referansta olmayan fonksiyon adı uydurma

### 3. Hata Olduğunda
- Hatayı çöz
- `LESSONS_LEARNED.md`'ye hemen ekle: başlık + hata + sebep + çözüm + kod örneği

---

## LESSONS_LEARNED Özeti (11 Hata — Detay için dosyayı oku)

| # | Hata | Çözüm |
|---|------|-------|
| 1 | `ta.stoch()` tuple döndürüyor sanmak | `float k = ta.stoch(...)` |
| 2 | `math.avg(a, b)` kullanmak | `(a + b) / 2` |
| 3 | `request.security()` tuple syntax yanlış | Köşeli parantez zorunlu |
| 4 | Futures komisyon tipi yanlış | `strategy.commission.cash_per_contract` |
| 5 | EMA cross + hacim filtresi yok | Fakeout önlemek için şart |
| 6 | `request.security()` repainting | `[1]` + `lookahead_on` kullan |
| 7 | `alertcondition()` strategy'de | `alert()` kullan, `if` bloğu içinde |
| 8 | `barstate.islast` + label strategy'de | `barstate.isconfirmed` kullan |
| 9 | Çok satırlı `and` başta | Tek satır veya `and` satır sonunda |
| 10 | `calc_on_every_tick=true` | Kaldır — backtest bozar, uyarı verir |
| 11 | `barstate.islast` strategy'de | `barstate.isconfirmed` kullan |

---

## v5 → v6 Dönüşüm Tablosu

| ❌ v5 — YAZMA | ✅ v6 — YAZ |
|--------------|------------|
| `study("name")` | `indicator("name")` |
| `security(ticker, tf, expr)` | `request.security(ticker, tf, expr)` |
| `input(14, type=input.integer)` | `input.int(14, "Label")` |
| `array.new_float(0)` | `array.new<float>(0)` |
| `[k, d] = ta.stoch(...)` | `float k = ta.stoch(...)` |
| `math.avg(a, b)` | `(a + b) / 2` |
| `alertcondition()` strategy'de | `if signal\n    alert(...)` |
| `barstate.islast` strategy'de | `barstate.isconfirmed` |
| `calc_on_every_tick = true` | kaldır |
| Çok satırlı `and` başta | tek satır |

---

## VİOP / BIST30 Şablonu

VİOP stratejisi yazarken bu template'i kullan:

```pine
//@version=6
strategy("VİOP Strategy [trugurpala]",
    overlay              = true,
    initial_capital      = 100000,
    default_qty_type     = strategy.fixed,
    default_qty_value    = 1,
    commission_type      = strategy.commission.cash_per_contract,
    commission_value     = 2.0,
    slippage             = 2)

// Seans: 09:30-18:15 UTC+3
bool inSession = not na(time(timeframe.period, "0930-1815", "UTC+3"))

// Seans kapanışında kapat
if not inSession and inSession[1]
    strategy.close_all(comment="Seans sonu")
```

- **Sembol:** `BIST:XU030D1!` veya `F_XU030`
- **Seans:** 09:30–18:15 UTC+3
- **Komisyon:** 2 TL/kontrat (cash_per_contract)
- **Önerilen TF:** 5dk, 15dk, 1sa

---

## Referans Haritası

| İhtiyaç | Dosya |
|---------|-------|
| RSI, EMA, MACD, ATR, crossover, pivot | `reference/functions/ta.md` |
| strategy.entry, exit, close, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| open, close, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.*, style.* | `reference/constants.md` |
| int, float, series, simple | `reference/types.md` |
| if, for, var, varip, switch | `reference/keywords.md` |
| barstate, var, history, realtime | `concepts/execution_model.md` |
| Repainting, HTF, MTF | `concepts/timeframes.md` |
| color.new, gradient | `concepts/colors_and_display.md` |
| Fakeout, sinyal kalitesi | `concepts/signal_quality.md` |
| Bilinen hatalar | `concepts/common_errors.md` |
| **Her zaman önce** | `LESSONS_LEARNED.md` |

---

## Kontrol Listesi

- [ ] `LESSONS_LEARNED.md` okundu (11 hata)
- [ ] `//@version=6` — ilk satır
- [ ] `alertcondition()` yok → `alert()` kullanıldı
- [ ] `calc_on_every_tick` yok
- [ ] `barstate.isconfirmed` (islast değil)
- [ ] Çok satırlı `and` yok — tek satır
- [ ] `request.security()` → `[1]` + `lookahead_on`
- [ ] `ta.*` kullanıldı — manuel hesaplama yok
- [ ] `study()` yok → `indicator()`
- [ ] `security()` yok → `request.security()`



---

## Source: tradingview-publish\README.md

# TradingView Publish Rehberi
> Ugur Pala · github.com/trugurpala/pinescriptv6

## Sıra / Publish Order

| # | Script | Pine Dosyası | Description Dosyası |
|---|--------|-------------|---------------------|
| 1 | Fakeout Filter | `examples/indicators/18_fakeout_filter.pine` | `01_fakeout_filter_description.md` |
| 2 | VIOP Session Strategy | `examples/strategies/11_viop_session_strategy.pine` | `02_viop_session_description.md` |
| 3 | Fakeout-Confirmed Strategy | `examples/strategies/13_fakeout_confirmed_strategy.pine` | `03_fakeout_confirmed_strategy_description.md` |

## Her Script İçin Adımlar / Steps for Each Script

1. **Pine dosyasını aç** — GitHub'dan `.pine` dosyasına tıkla, Raw görünümünü kopyala
2. **TradingView Pine Editor'ü aç** — grafik üzerinde alt panel
3. **Yeni script oluştur** — `New` → `Create new indicator` veya `Create new strategy`
4. **Kodu yapıştır** — `Add to chart` ile test et, hata yoksa devam et
5. **Publish** — `Publish script` → Title + Description kopyala → Tags ekle → `Publish`

## Description'a Mutlaka Eklenecekler

Her description'ın sonunda şu satır mutlaka olmalı:
```
github.com/trugurpala/pinescriptv6
```

Bu satır olmadan repo keşfedilmez.

## Publish Sonrası

Her publish'ten sonra X'te paylaş:
```
Yeni Pine Script v6 script: [BAŞLIK]
TradingView: [URL]
Kaynak: github.com/trugurpala/pinescriptv6
#PineScript #PineScriptV6 #TradingView #AlgoTrading
```



---

## Source: v5-to-v6-migration\01_study_to_indicator.md

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



---

## Source: v5-to-v6-migration\02_security_to_request.md

# security() → request.security()
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'te `security()` doğrudan çağrılırdı. v6'da `request.security()` oldu.

```pine
// ❌ v5
//@version=5
dailyClose = security(syminfo.tickerid, "D", close)

// ✅ v6
//@version=6
dailyClose = request.security(syminfo.tickerid, "D", close)
```

### Repainting — v5 vs v6

```pine
// ❌ v5 — repainting yapabilir
htf = security(syminfo.tickerid, "D", close)

// ✅ v6 — kapanmış bar, güvenli
htf = request.security(syminfo.tickerid, "D", close[1],
                        lookahead=barmerge.lookahead_on)
```

### Çoklu değer — tuple (v6 yeni özellik)

```pine
// ❌ v5 — ayrı ayrı çağrı
dHigh  = security(syminfo.tickerid, "D", high)
dLow   = security(syminfo.tickerid, "D", low)
dClose = security(syminfo.tickerid, "D", close)

// ✅ v6 — tek çağrı, tuple
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
                            [high[1], low[1], close[1]],
                            lookahead=barmerge.lookahead_on)
```

---

## EN | English

In v5, `security()` was called directly. In v6, it became `request.security()`.

```pine
// ❌ v5
dailyClose = security(syminfo.tickerid, "D", close)

// ✅ v6
dailyClose = request.security(syminfo.tickerid, "D", close)
```

### Key change: use tuple for multiple values

```pine
// ✅ v6 — single call, no repainting
[dHigh, dLow, dClose] = request.security(syminfo.tickerid, "D",
                            [high[1], low[1], close[1]],
                            lookahead=barmerge.lookahead_on)
```



---

## Source: v5-to-v6-migration\03_strategy_syntax.md

# Strategy Declaration Changes
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Strategy declaration v6'da aynı kaldı — sadece version değişir.

```pine
// ❌ v5
//@version=5
strategy("My Strategy", overlay=true,
    initial_capital=10000,
    default_qty_type=strategy.percent_of_equity,
    default_qty_value=10)

// ✅ v6
//@version=6
strategy("My Strategy", overlay=true,
    initial_capital=10000,
    default_qty_type=strategy.percent_of_equity,
    default_qty_value=10)
```

### strategy.entry() — değişen yok

```pine
//@version=6
strategy("Demo", overlay=true)
if ta.crossover(ta.ema(close,9), ta.ema(close,21))
    strategy.entry("Long", strategy.long)
if ta.crossunder(ta.ema(close,9), ta.ema(close,21))
    strategy.close("Long")
```

### Yeni v6 özelliği — process_orders_on_close

```pine
//@version=6
strategy("Demo", overlay=true,
    process_orders_on_close=true)  // v6'da eklendi
```

---

## EN | English

Strategy declaration is mostly unchanged — only the version number changes.

### New in v6: process_orders_on_close parameter

```pine
//@version=6
strategy("Demo", overlay=true,
    process_orders_on_close=true)
```



---

## Source: v5-to-v6-migration\04_type_system.md

# Type System & Explicit Declarations
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v6'da tipler artık explicit olarak belirtilmesi **öneriliyor** (zorunlu değil ama iyi pratik).

```pine
// v5 — tip belirtmek opsiyoneldi
//@version=5
length = input(14, "Length")
myVar  = close * 2

// v6 — explicit tip önerilen pratik
//@version=6
int   length = input.int(14, "Length")
float myVar  = close * 2
```

### input() → input.*

```pine
// ❌ v5
length = input(14, "Length", type=input.integer)
src    = input(close, "Source", type=input.source)
tf     = input("D", "Timeframe", type=input.resolution)
col    = input(color.red, "Color", type=input.color)

// ✅ v6
int    length = input.int(14,    "Length")
float  src    = input.source(close, "Source")
string tf     = input.string("D",  "Timeframe")
color  col    = input.color(color.red, "Color")
```

### var ve varip — değişen yok, ama artık typed

```pine
//@version=6
var float   cumSum = 0.0     // tip explicit — önerilen
var int     barCount = 0
varip float tickSum = 0.0
```

---

## EN | English

In v6, explicit type declarations are **recommended** (not required, but good practice).

### input() → input.* functions

```pine
// ❌ v5
length = input(14, "Length", type=input.integer)

// ✅ v6
int length = input.int(14, "Length")
```



---

## Source: v5-to-v6-migration\05_arrays_and_collections.md

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



---

## Source: v5-to-v6-migration\06_input_functions.md

# input() → input.* Functions
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'teki tek `input()` fonksiyonu v6'da namespace'e ayrıldı.

### Tam dönüşüm tablosu

| v5 | v6 |
|----|-----|
| `input(14, type=input.integer)` | `input.int(14)` |
| `input(2.0, type=input.float)` | `input.float(2.0)` |
| `input(true, type=input.bool)` | `input.bool(true)` |
| `input("D", type=input.resolution)` | `input.string("D")` |
| `input(close, type=input.source)` | `input.source(close)` |
| `input(color.red, type=input.color)` | `input.color(color.red)` |
| `input(timestamp("2024-01-01"), type=input.time)` | `input.time(timestamp("2024-01-01"))` |
| `input("Label", type=input.session)` | `input.session("0930-1730")` |
| `input("AAPL", type=input.symbol)` | `input.symbol("AAPL")` |

### Gerçek örnek

```pine
// ❌ v5
//@version=5
length = input(14, title="RSI Length", type=input.integer, minval=1, maxval=500)
src    = input(close, title="Source", type=input.source)
tf     = input("D", title="Timeframe", type=input.resolution)

// ✅ v6
//@version=6
int    length = input.int(14,    "RSI Length", minval=1, maxval=500)
float  src    = input.source(close, "Source")
string tf     = input.string("D",  "Timeframe",
                    options=["1","5","15","60","D","W","M"])
```

---

## EN | English

The single v5 `input()` function was split into namespaced functions in v6.

```pine
// ❌ v5
length = input(14, type=input.integer)

// ✅ v6
int length = input.int(14, "Length")
```



---

## Source: v5-to-v6-migration\07_drawing_objects.md

# Drawing Objects — line / label / box
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Drawing API v6'da büyük ölçüde aynı kaldı — sadece `chart.point` eklendi.

### line.new() — değişen yok

```pine
//@version=6
var line myLine = na
if barstate.islast
    line.delete(myLine)
    myLine := line.new(bar_index - 10, ta.lowest(10),
                       bar_index,      ta.highest(10),
                       color=color.orange, width=2)
```

### label.new() — değişen yok

```pine
//@version=6
if ta.pivothigh(high, 5, 5)
    label.new(bar_index[5], high[5],
        str.tostring(high[5], format.mintick),
        style=label.style_label_down,
        color=color.red, textcolor=color.white)
```

### Yeni v6: chart.point

```pine
//@version=6
indicator("chart.point demo", overlay=true)
// chart.point koordinat sistemi — line.new için de kullanılabilir
cp = chart.point.now(high)
line.new(chart.point.from_index(bar_index - 5, low[5]), cp)
```

### Limit artırma — v5 ile aynı

```pine
//@version=6
indicator("Demo",
    max_lines_count  = 500,
    max_labels_count = 500,
    max_boxes_count  = 500)
```

---

## EN | English

Drawing API is mostly unchanged. The main addition in v6 is `chart.point`.

```pine
//@version=6
// New: chart.point coordinate system
cp = chart.point.now(high)
line.new(chart.point.from_index(bar_index - 5, low[5]), cp)
```



---

## Source: v5-to-v6-migration\08_pine_logs.md

# Pine Logs — New in v6
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'te runtime logging yoktu. v6'da `log.*` namespace'i eklendi.

### Temel kullanım

```pine
//@version=6
indicator("Pine Logs Demo")

rsi = ta.rsi(close, 14)
atr = ta.atr(14)

// Her son barda log yaz
if barstate.islast
    log.info("Bar: {0} | Close: {1} | RSI: {2}",
        bar_index,
        str.tostring(close, format.mintick),
        str.tostring(math.round(rsi, 2)))

// Koşullu uyarı
if rsi > 70
    log.warning("RSI aşırı alım: {0}", math.round(rsi, 1))

// Hata logla
if close < 0
    log.error("Geçersiz fiyat: {0}", close)
```

### Log seviyeleri

| Fonksiyon | Seviye | Renk |
|-----------|--------|------|
| `log.info()` | Bilgi | Mavi |
| `log.warning()` | Uyarı | Sarı |
| `log.error()` | Hata | Kırmızı |

### Pine Editor'da nasıl açılır

TradingView → Pine Editor → sağ alttaki **Pine Logs** paneli

### Format string kullanımı

```pine
//@version=6
indicator("Format demo")
log.info("Sembol: {0} | TF: {1} | Bar: {2}",
    syminfo.ticker,
    timeframe.period,
    bar_index)
```

---

## EN | English

v5 had no runtime logging. v6 added the `log.*` namespace.

```pine
//@version=6
indicator("Pine Logs Demo")
if barstate.islast
    log.info("Bar: {0} | RSI: {1}", bar_index, math.round(ta.rsi(close,14), 2))
    log.warning("ATR: {0}", math.round(ta.atr(14), 4))
```

### How to open Pine Logs

TradingView → Pine Editor → **Pine Logs** panel (bottom right)



---

## Source: v5-to-v6-migration\09_methods_and_udt.md

# Methods & User-Defined Types — New in v6
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'te UDT (User-Defined Type) ve user-defined method yoktu. v6'da eklendi.

### User-Defined Type (UDT)

```pine
//@version=6
indicator("UDT demo", overlay=true)

// Tip tanımla
type PivotPoint
    int   index
    float price
    bool  isHigh

// Instance oluştur
var PivotPoint lastPivot = na

if not na(ta.pivothigh(high, 5, 5))
    lastPivot := PivotPoint.new(
        index  = bar_index[5],
        price  = high[5],
        isHigh = true)
    label.new(lastPivot.index, lastPivot.price, "PH",
        style=label.style_label_down, color=color.red)
```

### User-Defined Methods

```pine
//@version=6
indicator("Method demo")

// Array üzerine method tanımla
method addAndTrim(array<float> arr, float val, int maxSize) =>
    arr.push(val)
    if arr.size() > maxSize
        arr.shift()
    arr

var queue = array.new<float>(0)
queue.addAndTrim(close, 20)  // method syntax ile çağır
plot(queue.avg(), "Rolling Avg")
```

### v5 ile karşılaştırma

```pine
// v5 — UDT yok, her şey ayrı değişken
//@version=5
var int   pivotIdx   = na
var float pivotPrice = na
var bool  pivotIsHigh = na

// v6 — UDT ile temiz
//@version=6
type PivotPoint
    int   index
    float price
    bool  isHigh
var PivotPoint pivot = na
```

---

## EN | English

UDT and user-defined methods are new in v6.

```pine
//@version=6
// Define a type
type Trade
    float entry
    float stop
    float target

// Create and use
var Trade myTrade = na
if longSignal
    myTrade := Trade.new(
        entry  = close,
        stop   = close - 2 * ta.atr(14),
        target = close + 3 * ta.atr(14))
```



---

## Source: v5-to-v6-migration\10_common_migration_errors.md

# Common Migration Errors — v5 → v6
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Bu hatalar v5 kodunu v6'ya taşırken en sık karşılaşılan sorunlardır.

---

### 1. "Undeclared identifier 'study'"

```pine
// ❌ Hata
//@version=6
study("My Indicator", overlay=true)  // study() v6'da yok

// ✅ Düzeltme
//@version=6
indicator("My Indicator", overlay=true)
```

---

### 2. "Undeclared identifier 'security'"

```pine
// ❌ Hata
//@version=6
htf = security(syminfo.tickerid, "D", close)  // security() v6'da yok

// ✅ Düzeltme
//@version=6
htf = request.security(syminfo.tickerid, "D", close)
```

---

### 3. "Cannot call 'input' with these arguments"

```pine
// ❌ Hata
//@version=6
length = input(14, type=input.integer)  // eski syntax

// ✅ Düzeltme
//@version=6
int length = input.int(14, "Length")
```

---

### 4. "array.new_float is not defined"

```pine
// ❌ Hata
//@version=6
arr = array.new_float(0)  // v5 syntax

// ✅ Düzeltme
//@version=6
var arr = array.new<float>(0)
```

---

### 5. "Cannot use 'series string' as argument"

```pine
// ❌ Hata — timeframe değişken olamaz
//@version=6
string tf = close > open ? "D" : "W"  // series string
htf = request.security(syminfo.tickerid, tf, close)  // HATA

// ✅ Düzeltme — input ile sabit yap
//@version=6
string tfInput = input.string("D", "TF", options=["D","W","M"])
htf = request.security(syminfo.tickerid, tfInput, close)
```

---

### 6. "Pine Script v6 requires //@version=6"

```pine
// ❌ Hata — version eksik
indicator("Demo")

// ✅ Düzeltme
//@version=6
indicator("Demo")
```

---

### 7. plot() içinde series string kullanımı

```pine
// ❌ Hata
//@version=6
title_str = close > open ? "Bull" : "Bear"
plot(close, title=title_str)  // title series olamaz

// ✅ Düzeltme — sabit string kullan
//@version=6
plot(close, title="Price")
```

---

## EN | English

These are the most common errors when migrating v5 code to v6.

| Error | Cause | Fix |
|-------|-------|-----|
| `'study' undefined` | `study()` removed | Use `indicator()` |
| `'security' undefined` | `security()` removed | Use `request.security()` |
| `input()` argument error | Old syntax | Use `input.int()`, `input.float()` etc. |
| `array.new_float` undefined | Old syntax | Use `array.new<float>()` |
| Series string error | Dynamic string in function | Use `input.string()` |



---

## Source: v5-to-v6-migration\README.md

# Pine Script v5 → v6 Migration Guide
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: En yaygın v5 → v6 dönüşüm örnekleri. Eski kodlarınızı kopyalayıp yapıştırın.
EN: Most common v5 → v6 migration examples. Copy-paste your old code and update.

---

## Dosyalar / Files

| Dosya | Konu |
|-------|------|
| `01_study_to_indicator.md` | `study()` → `indicator()` |
| `02_security_to_request.md` | `security()` → `request.security()` |
| `03_strategy_syntax.md` | Strategy declaration changes |
| `04_type_system.md` | Type system & explicit declarations |
| `05_arrays_and_collections.md` | Array/map/matrix updates |
| `06_input_functions.md` | `input()` → `input.*` |
| `07_drawing_objects.md` | line/label/box updates |
| `08_pine_logs.md` | New: `log.info()` / `log.warning()` |
| `09_methods_and_udt.md` | New: User-defined methods & types |
| `10_common_migration_errors.md` | Errors you'll hit during migration |

---

TR: Tüm dosyalar LESSONS_LEARNED.md ile entegre çalışır — hata bulunca otomatik kaydedilir.
EN: All files integrate with LESSONS_LEARNED.md — errors auto-saved when found.



---

## Source: webhook-templates\01_alert_message_templates.md

# Alert Message Templates
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

TradingView alert mesajlarında kullanılabilecek dinamik değişkenler ve hazır şablonlar.

### TradingView Dinamik Değişkenler

| Değişken | Açıklama |
|----------|----------|
| `{{ticker}}` | Sembol adı (ör. XU030) |
| `{{exchange}}` | Borsa (ör. BIST) |
| `{{close}}` | Kapanış fiyatı |
| `{{open}}` | Açılış fiyatı |
| `{{high}}` | Yüksek |
| `{{low}}` | Düşük |
| `{{volume}}` | Hacim |
| `{{time}}` | Bar zamanı |
| `{{timenow}}` | Şu anki zaman |
| `{{interval}}` | Grafik zaman dilimi |
| `{{strategy.order.action}}` | `buy` veya `sell` |
| `{{strategy.order.price}}` | Emir fiyatı |
| `{{strategy.order.contracts}}` | Lot sayısı |
| `{{strategy.position_size}}` | Pozisyon büyüklüğü |

---

### Hazır Şablonlar

**Basit fiyat alarmı:**
```
{{ticker}} | {{interval}} | Fiyat: {{close}} | {{timenow}}
```

**EMA Cross sinyali:**
```
🚨 EMA CROSS | {{ticker}}
Yön: {{strategy.order.action}}
Fiyat: {{close}}
Zaman: {{timenow}}
```

**VİOP / BIST30 stratejisi:**
```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "qty":      {{strategy.order.contracts}},
  "interval": "{{interval}}",
  "time":     "{{timenow}}"
}
```

**Telegram için:**
```
📊 *{{ticker}}* | {{interval}}
🎯 Sinyal: {{strategy.order.action}}
💰 Fiyat: {{close}}
📦 Lot: {{strategy.order.contracts}}
🕐 {{timenow}}
```

**Discord Embed için:**
```json
{
  "embeds": [{
    "title": "{{ticker}} — {{strategy.order.action}}",
    "color": 3066993,
    "fields": [
      {"name": "Fiyat", "value": "{{close}}", "inline": true},
      {"name": "Zaman", "value": "{{timenow}}", "inline": true}
    ]
  }]
}
```

---

## EN | English

### Dynamic Variables

Same variables work in English — see table above.

### Ready Templates

**Simple price alert:**
```
{{ticker}} | {{interval}} | Price: {{close}} | {{timenow}}
```

**Strategy signal:**
```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "qty":      {{strategy.order.contracts}},
  "interval": "{{interval}}",
  "time":     "{{timenow}}"
}
```

**Telegram format:**
```
📊 *{{ticker}}* | {{interval}}
🎯 Signal: {{strategy.order.action}}
💰 Price: {{close}}
📦 Qty: {{strategy.order.contracts}}
🕐 {{timenow}}
```



---

## Source: webhook-templates\03_telegram_webhook.md

# Telegram Webhook Integration
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

TradingView alertlerini Telegram'a iletmek için hazır şablon.

### Adım 1 — Telegram Bot Oluştur

1. Telegram'da `@BotFather` ile konuş
2. `/newbot` yaz → bot adı ve kullanıcı adı belirle
3. **Bot Token** al: `7123456789:AAF...`
4. Botla bir konuşma başlat
5. Chat ID al: `https://api.telegram.org/bot{TOKEN}/getUpdates`

---

### Adım 2 — Python Webhook Server

```python
# webhook_server.py
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7123456789:AAF..."  # BotFather'dan aldığın token
CHAT_ID   = "123456789"          # Telegram chat ID

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    msg  = data.get("message", str(data))
    url  = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Adım 3 — TradingView Alert Kurulumu

**Alert Message:**
```
📊 *{{ticker}}* | {{interval}}
🎯 Sinyal: EMA Cross
💰 Fiyat: {{close}}
🕐 {{timenow}}
```

**Webhook URL:**
```
http://SUNUCU_IP:5000/webhook
```

---

### Adım 4 — Pine Script'ten JSON Gönder

```pine
//@version=6
strategy("Telegram Strategy", overlay=true)
// ...strateji kodu...

// Alert mesajı TradingView → Alert → Message kutusuna:
// {"symbol":"{{ticker}}","action":"{{strategy.order.action}}","price":{{close}}}
```

---

## EN | English

### Step 1 — Create a Telegram Bot

1. Chat with `@BotFather` on Telegram
2. Type `/newbot` → set name and username
3. Get your **Bot Token**: `7123456789:AAF...`
4. Start a conversation with your bot
5. Get Chat ID: `https://api.telegram.org/bot{TOKEN}/getUpdates`

### Step 2 — Python Webhook Server

```python
from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = "YOUR_TOKEN"
CHAT_ID   = "YOUR_CHAT_ID"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    msg  = data.get("message", str(data))
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return "ok", 200

app.run(host="0.0.0.0", port=5000)
```

### Step 3 — TradingView Alert Message

```
📊 *{{ticker}}* | {{interval}}
🎯 Signal: EMA Cross
💰 Price: {{close}}
🕐 {{timenow}}
```



---

## Source: webhook-templates\04_discord_webhook.md

# Discord Webhook Integration
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

TradingView alertlerini Discord kanalına iletmek için hazır şablon.

### Adım 1 — Discord Webhook URL Al

1. Discord sunucunda kanal seç
2. Kanal ayarları → **Integrations** → **Webhooks** → **New Webhook**
3. Webhook URL kopyala:
   `https://discord.com/api/webhooks/1234567890/abc...`

---

### Adım 2 — Direkt Discord'a Gönder (Python)

```python
# discord_webhook.py
from flask import Flask, request
import requests

app = Flask(__name__)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"

@app.route("/webhook", methods=["POST"])
def webhook():
    data    = request.get_json()
    symbol  = data.get("symbol", "?")
    action  = data.get("action", "?")
    price   = data.get("price",  "?")

    payload = {
        "embeds": [{
            "title":       f"{symbol} — {action.upper()}",
            "color":       3066993 if action == "buy" else 15158332,
            "description": f"💰 Fiyat: **{price}**",
            "fields": [
                {"name": "Sembol",   "value": symbol, "inline": True},
                {"name": "İşlem",    "value": action, "inline": True},
                {"name": "Fiyat",    "value": str(price), "inline": True}
            ],
            "footer": {"text": "Pine Script v6 — trugurpala/pinescriptv6"}
        }]
    }
    requests.post(DISCORD_WEBHOOK, json=payload)
    return "ok", 200

app.run(host="0.0.0.0", port=5000)
```

---

### Adım 3 — TradingView Alert JSON Mesajı

```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "interval": "{{interval}}",
  "time":     "{{timenow}}"
}
```

---

### Adım 4 — Webhook URL

TradingView Alert → **Webhook URL** kutusuna:
```
http://SUNUCU_IP:5000/webhook
```

---

## EN | English

### Step 1 — Get Discord Webhook URL

1. Pick a channel in your Discord server
2. Channel settings → **Integrations** → **Webhooks** → **New Webhook**
3. Copy the URL: `https://discord.com/api/webhooks/...`

### Step 2 — Python Handler

```python
from flask import Flask, request
import requests

app = Flask(__name__)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    requests.post(DISCORD_WEBHOOK, json={
        "embeds": [{
            "title": f"{data.get('symbol')} — {data.get('action', '').upper()}",
            "color": 3066993,
            "description": f"Price: {data.get('price')}"
        }]
    })
    return "ok", 200
```

### Step 3 — TradingView Alert JSON

```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "interval": "{{interval}}"
}
```



---

## Source: webhook-templates\05_json_payload_templates.md

# JSON Payload Templates
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Farklı broker API'leri ve sistemler için hazır JSON payload şablonları.
TradingView Alert → Message kutusuna yapıştır.

---

### Basit Buy/Sell

```json
{
  "action":   "{{strategy.order.action}}",
  "symbol":   "{{ticker}}",
  "price":    {{close}},
  "time":     "{{timenow}}"
}
```

---

### Strateji Detaylı

```json
{
  "symbol":        "{{ticker}}",
  "exchange":      "{{exchange}}",
  "interval":      "{{interval}}",
  "action":        "{{strategy.order.action}}",
  "price":         {{close}},
  "qty":           {{strategy.order.contracts}},
  "position_size": {{strategy.position_size}},
  "order_price":   {{strategy.order.price}},
  "time":          "{{timenow}}"
}
```

---

### VİOP / BIST30 Spesifik

```json
{
  "market":    "VIOP",
  "symbol":    "F_XU030",
  "action":    "{{strategy.order.action}}",
  "price":     {{close}},
  "lot":       {{strategy.order.contracts}},
  "interval":  "{{interval}}",
  "signal_id": "{{ticker}}_{{timenow}}"
}
```

---

### Risk Yönetimi Dahil

```json
{
  "symbol":     "{{ticker}}",
  "action":     "{{strategy.order.action}}",
  "price":      {{close}},
  "sl_price":   {{strategy.order.price}},
  "position":   {{strategy.position_size}},
  "equity":     {{strategy.equity}},
  "interval":   "{{interval}}",
  "time":       "{{timenow}}"
}
```

---

### Çoklu Sinyal (indikatör için)

```json
{
  "symbol":    "{{ticker}}",
  "signal":    "ema_cross_bull",
  "price":     {{close}},
  "interval":  "{{interval}}",
  "time":      "{{timenow}}"
}
```

---

## EN | English

### Simple Buy/Sell

```json
{
  "action":  "{{strategy.order.action}}",
  "symbol":  "{{ticker}}",
  "price":   {{close}},
  "time":    "{{timenow}}"
}
```

### Full Strategy Payload

```json
{
  "symbol":        "{{ticker}}",
  "exchange":      "{{exchange}}",
  "interval":      "{{interval}}",
  "action":        "{{strategy.order.action}}",
  "price":         {{close}},
  "qty":           {{strategy.order.contracts}},
  "position_size": {{strategy.position_size}},
  "time":          "{{timenow}}"
}
```



---

## Source: webhook-templates\README.md

# Webhook Templates — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: TradingView alert'lerini dış sistemlere iletmek için hazır webhook şablonları.
EN: Ready-to-use webhook templates for forwarding TradingView alerts to external systems.

---

## Dosyalar / Files

| Dosya | Açıklama / Description |
|-------|------------------------|
| `01_alert_message_templates.md` | TradingView alert mesaj şablonları |
| `02_pine_alert_conditions.pine` | `alertcondition()` ve `alert()` örnekleri |
| `03_telegram_webhook.md` | Telegram bot entegrasyonu |
| `04_discord_webhook.md` | Discord webhook entegrasyonu |
| `05_json_payload_templates.md` | JSON payload şablonları (broker API'leri için) |
| `06_viop_bist30_alerts.pine` | VİOP / BIST30 spesifik alert örnekleri |

---

## Nasıl Çalışır / How It Works

```
TradingView Alert
      │
      ▼
Webhook URL ──► Telegram Bot
             ├─► Discord Channel
             ├─► Custom Server (Python/Node.js)
             └─► Broker API
```

TR: TradingView Premium veya üzeri gereklidir.
EN: TradingView Premium or higher required for webhook alerts.

