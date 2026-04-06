# Style Guide - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## Script Iskelet Sirasi
1. //@version=6
2. indicator() / strategy() / library()
3. import ifadeleri
4. Sabitler (UPPER_SNAKE_CASE)
5. input.* degiskenleri
6. Fonksiyon tanimlari
7. Hesaplamalar
8. Strateji / Alert mantigi
9. Gorseller: plot, bgcolor, label, table

## Isimlendirme Kurallari
- Degiskenler: camelCase     -> fastEma, rsiValue, isLong
- Sabitler: UPPER_SNAKE_CASE -> MAX_BARS, DEFAULT_LENGTH
- Fonksiyonlar: camelCase    -> calcRsi(), drawLabel()
- UDT Tipleri: PascalCase    -> PivotPoint, TradeInfo
- Input degiskenleri: camelCase + "Input" -> lengthInput, sourceInput

## Girintileme
- 4 bosluk kullan (tab degil)
- Her if/for/while blogu icin girintile

## Yorum Standardi
```pine
//@version=6
// Tek satirlik aciklama

//@variable Degiskenin ne yaptigini aciklar.
float myRsi = ta.rsi(close, 14)

//@function Fonksiyonun amacini aciklar.
//@param src (series float) Kaynak seri.
//@param len (simple int) Period.
//@returns (series float) EMA degeri.
myEma(float src, int len) =>
    ta.ema(src, len)
```

## Iyi Girintileme Ornegi
```pine
//@version=6
indicator("Style Demo", overlay=true)

// --- Sabitler ---
int   DEFAULT_LEN = 14
float ATR_MULT    = 1.5

// --- Inputlar ---
int   lengthInput = input.int(DEFAULT_LEN, "RSI Periyodu", minval=1)
float multInput   = input.float(ATR_MULT,  "ATR Carpan",   step=0.1)
bool  showLabels  = input.bool(true,       "Etiket Goster")

// --- Hesaplamalar ---
float rsi = ta.rsi(close, lengthInput)
float atr = ta.atr(lengthInput)

// --- Gorseller ---
plot(rsi, "RSI", color.blue)
hline(70)
hline(30)
```
