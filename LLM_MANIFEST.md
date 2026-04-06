# Pine Script v6 — LLM Manifest
> Maintainer: Ugur Pala — mail@ugurpala.com
> Bu dosya Claude'un hangi sorun için hangi referans dosyasına bakacagini belirler.

## Protokol
1. Kullanicinin niyetini belirle
2. Asagidaki tablodan ilgili dosyayi bul
3. SADECE o dosyayi oku (context penceresi icin)

## 1. Syntax ve Temel Kavramlar

| Anahtar Kelimeler | Dosya |
|---|---|
| barstate, history, realtime, var, varip, calc_on_every_tick | concepts/execution_model.md |
| request.security, timeframe.period, repainting, HTF | concepts/timeframes.md |
| color.new, color.from_gradient, bgcolor | concepts/colors_and_display.md |
| Series string, Undeclared identifier, max_bars_back | concepts/common_errors.md |
| method, user-defined method | concepts/methods.md |
| type, UDT, object, field | concepts/objects.md |

## 2. API Referans

| Anahtar Kelimeler | Dosya |
|---|---|
| open, high, low, close, volume, time, bar_index, syminfo | reference/variables.md |
| color.red, shape.triangle, plot.style_line, size.small | reference/constants.md |
| int, float, bool, string, series, simple, input type | reference/types.md |
| if, else, for, while, switch, var, varip, export | reference/keywords.md |
| @version, @description, @param, @returns | reference/annotations.md |

## 3. Fonksiyon Referansi

| Ihtiyac | Dosya |
|---|---|
| ta.rsi, ta.ema, ta.sma, ta.macd, ta.crossover, ta.pivot | reference/functions/ta.md |
| strategy.entry, strategy.exit, strategy.close, position | reference/functions/strategy.md |
| request.security, request.financial, request.seed | reference/functions/request.md |
| plot, plotshape, line.new, box.new, label.new, fill | reference/functions/drawing.md |
| array.new, array.push, matrix, map | reference/functions/collections.md |
| math.abs, str.tostring, input.int, alert() | reference/functions/general.md |

## 4. Kod Yazma

| Ihtiyac | Dosya |
|---|---|
| Stil, isimlendirme, girintileme | writing_scripts/style_guide.md |
| log.info, Pine Logs, hata ayiklama | writing_scripts/debugging.md |
| Performans, optimizasyon | writing_scripts/profiling_and_optimization.md |
| Script limitleri, max bars | writing_scripts/limitations.md |

## Yonlendirme Ornekleri

- RSI indikatoru yaz → reference/functions/ta.md + reference/functions/drawing.md
- Strateji backtesti → reference/functions/strategy.md + reference/functions/ta.md
- Degiskenim neden sifirlaniyor → concepts/execution_model.md
- max_bars_back hatasi → concepts/common_errors.md
- Hata var mi diye bak → LESSONS_LEARNED.md (HER ZAMAN ONCE BU)
