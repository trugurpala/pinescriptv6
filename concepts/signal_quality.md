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
