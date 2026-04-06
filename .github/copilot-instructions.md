# Pine Script v6 Reference — GitHub Copilot Instructions
# Author: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
# TradingView: https://tr.tradingview.com/u/trugurpala/
# X: https://x.com/trugurpala

## Bu Repo Neden Var? / Why This Repo Exists?

TR: TradingView Pine Script v6 çıktığında tüm AI editörler v5 kodu yazmaya devam etti.
    Bu repo Copilot'a doğru v6 referansı ve kalıcı hata hafızası verir.

EN: When Pine Script v6 launched, all AI editors kept writing v5 code.
    This repo gives Copilot correct v6 reference and permanent error memory.

## Kullandığını Nasıl Anlarsın? / How to Verify It's Working?

TR: Bu talimatlar aktifse Copilot şunları yapmalı:
    ✅ LESSONS_LEARNED.md okuduğunu belirtmeli
    ✅ //@version=6 ile başlamalı
    ✅ ta.* kullanmalı, v5 syntax yazmamalı
    ❌ v5 syntax görüyorsan talimatlar aktif değil

EN: If these instructions are active, Copilot should:
    ✅ Mention reading LESSONS_LEARNED.md
    ✅ Start with //@version=6
    ✅ Use ta.*, never write v5 syntax
    ❌ If you see v5 syntax, instructions are not active

## Protokol / Protocol

1. LESSONS_LEARNED.md oku / read — bilinen hatalar
2. LLM_MANIFEST.md ile doğru referans dosyasını bul / find correct file
3. O dosyayı oku / read it
4. Kodu yaz — //@version=6 ile / write starting with //@version=6
5. Hata olunca: çöz + LESSONS_LEARNED.md'ye ekle / solve + append

## Kod Kuralları / Code Rules

- //@version=6 — her scriptin ilk satırı / first line always
- ta.* kullan — asla manuel hesaplama / use ta.*, never reimplement
- input.int(), input.float() — asla bare input() / never bare input()
- request.security() — asla security() / never security()
- indicator() — asla study() / never study()

## v5 → v6

| ❌ v5 | ✅ v6 |
|-------|-------|
| study() | indicator() |
| security() | request.security() |
| input(14, type=input.integer) | input.int(14) |
| array.new_float() | array.new<float>() |

## Referans / Reference

| İhtiyaç / Need | Dosya / File |
|----------------|-------------|
| RSI, EMA, MACD, ATR | reference/functions/ta.md |
| strategy.entry, exit | reference/functions/strategy.md |
| plot, line, label | reference/functions/drawing.md |
| request.security | reference/functions/request.md |
| Bilinen hatalar / Known errors | concepts/common_errors.md |
| **Her zaman önce / Always first** | LESSONS_LEARNED.md |

## Copilot Chat Örnekleri / Chat Examples

TR:
  LESSONS_LEARNED.md dosyasını kontrol et, sonra EMA cross stratejisi yaz.
  reference/functions/ta.md dosyasına göre ta.pivothigh() imzası nedir?
  Bu Pine Script v6 hatasını açıkla ve düzelt.

EN:
  Check LESSONS_LEARNED.md, then write an EMA cross strategy.
  According to reference/functions/ta.md, what is the ta.pivothigh() signature?
  Explain and fix this Pine Script v6 error.
