# Style Guide
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Script İskeleti — Sıralama

```pine
//@version=6
indicator("İsim", overlay=true/false)

// 1. Sabitler
int   MAX_BARS = 500
float ATR_MULT = 1.5

// 2. Inputlar
int   lengthInput = input.int(14, "RSI Periyodu", minval=1)
float multInput   = input.float(2.0, "ATR Çarpan",  step=0.1)
bool  showLabels  = input.bool(true, "Etiket Göster")

// 3. Hesaplamalar
float rsi = ta.rsi(close, lengthInput)
float atr = ta.atr(lengthInput)

// 4. Strateji / Alert mantığı

// 5. Görseller
plot(rsi, "RSI", color.blue)
```

### İsimlendirme

| Tür | Format | Örnek |
|-----|--------|-------|
| Değişken | camelCase | `fastEma`, `isLong` |
| Sabit | UPPER_SNAKE | `MAX_BARS`, `DEFAULT_LEN` |
| Fonksiyon | camelCase | `calcRsi()`, `drawLabel()` |
| UDT | PascalCase | `PivotPoint`, `TradeInfo` |
| Input | camelCase + `Input` | `lengthInput`, `sourceInput` |

### Yorum Standardı

```pine
//@variable RSI değeri, 0-100 arasında.
float myRsi = ta.rsi(close, 14)

//@function ATR tabanlı stop fiyatı hesaplar.
//@param entry  (float) Giriş fiyatı
//@param mult   (float) ATR çarpanı
//@returns      (float) Stop fiyatı
calcStop(float entry, float mult) =>
    entry - mult * ta.atr(14)
```

### Kurallar
- 4 boşluk girintileme (tab değil)
- Her blok için girintile
- `plot()` çağrıları her zaman en sonda

---

## EN | English

### Script Skeleton — Order

```pine
//@version=6
indicator("Name", overlay=true/false)

// 1. Constants
// 2. Inputs
// 3. Calculations
// 4. Strategy / Alert logic
// 5. Visuals — plot() calls always last
```

### Naming

| Type | Format | Example |
|------|--------|---------|
| Variable | camelCase | `fastEma`, `isLong` |
| Constant | UPPER_SNAKE | `MAX_BARS`, `DEFAULT_LEN` |
| Function | camelCase | `calcRsi()`, `drawLabel()` |
| UDT | PascalCase | `PivotPoint`, `TradeInfo` |
| Input | camelCase + `Input` | `lengthInput`, `sourceInput` |

### Comment Standard

```pine
//@variable RSI value, range 0-100.
float myRsi = ta.rsi(close, 14)

//@function Calculates ATR-based stop price.
//@param entry  (float) Entry price
//@param mult   (float) ATR multiplier
//@returns      (float) Stop price
calcStop(float entry, float mult) =>
    entry - mult * ta.atr(14)
```

### Rules
- 4-space indentation (not tabs)
- Indent every block
- `plot()` calls always at the end
