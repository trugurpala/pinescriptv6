## Ne değişti? / What changed?

<!-- TR: Kısaca açıkla. EN: Brief description. -->

## Kullanıcı etkisi / User impact

<!-- TR: Son kullanıcı veya katkı veren için ne değişiyor? EN: What changes for an end user or contributor? -->

## Tür / Type

- [ ] `docs` — referans veya belge güncelleme / reference or documentation update
- [ ] `fix` — yanlış bilgi veya davranış düzeltme / incorrect information or behavior fix
- [ ] `lesson` — LESSONS_LEARNED.md girdisi / LESSONS_LEARNED.md entry
- [ ] `feat` — yeni kural, örnek veya bölüm / new rule, example, or section

## Kaynak ve kanıt / Source and evidence

<!-- İlgili PSAK kimliklerini, resmî kaynakları ve doğrulama sınırını yazın. List relevant PSAK IDs, official sources, and verification boundary. -->

## Çalıştırılan kontroller / Checks run

```text
python -m unittest discover -s tests -v
python tools/psak.py validate
python tools/psak.py render --check
python tools/psak.py check
```

## Kontrol listesi / Checklist

- [ ] Kod örnekleri `//@version=6` ile başlıyor / Code examples start with `//@version=6`
- [ ] Yukarıdaki ilgili yerel kontroller başarılı / Relevant local checks above pass
- [ ] Yerel kontroller `structural-only` olarak raporlandı / Local checks are reported as `structural-only`
- [ ] Yeni veya değişen kural [kural katkı şablonunu](https://github.com/trugurpala/pinescriptv6/blob/main/docs/rule-contribution-template.md) izliyor / A new or changed rule follows the [rule contribution template](https://github.com/trugurpala/pinescriptv6/blob/main/docs/rule-contribution-template.md)
- [ ] TradingView iddiası varsa `examples/manifest.json` hash'i `verification/tradingview.json` kaydıyla eşleşiyor / If claiming TradingView evidence, the manifest hash matches a record in `verification/tradingview.json`
- [ ] v5 syntax yok / No v5 syntax
- [ ] Özel Pine kodu, kişisel veri veya gerçek secret yok / No private Pine code, personal data, or real secret
- [ ] Kullanıcıya dönük davranış değiştiyse ilgili belge güncellendi / User-facing behavior changes are documented
