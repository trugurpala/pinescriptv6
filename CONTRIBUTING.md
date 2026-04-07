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
