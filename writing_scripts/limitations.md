# Script Limitleri - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## Hesaplama Limitleri
- max_bars_back varsayilan: 300
- max_bars_back maksimum: 5000
- Maksimum degisken: 1000 per fonksiyon
- Maksimum ic ice fonksiyon derinligi: 500

## Drawing Limitleri

| Tur | Varsayilan Limit | Maksimum |
|-----|-----------------|----------|
| line | 50 | 500 |
| label | 50 | 500 |
| box | 50 | 500 |
| polyline | 100 | 100 |

Artirmak icin:
```pine
indicator("Demo",
          max_lines_count=500,
          max_labels_count=500,
          max_boxes_count=500)
```

## request.* Limitleri
- request.security(): max 40 per script
- request.security_lower_tf(): max 40
- request.financial(): max 40

## Koleksiyon Limitleri
- Max eleman per koleksiyon: 100,000
- Max koleksiyon sayisi: 1,000 per script

## Input Limitleri
- Max 500 input degiskeni

## Hata Yonetimi
```pine
// Ozel runtime hatasi
if length < 1
    runtime.error("Length en az 1 olmali: " + str.tostring(length))

// na kontrolu ile guvenli erisim
safeVal = na(myArr.get(0)) ? 0.0 : myArr.get(0)
```

## Plan Bazinda Farklar
- Historical bar sayisi plana gore degisir
- Intraday data: Ucretsiz hesaplarda sinirli gecmis
- Premium hesaplarda daha fazla gecmis veri
