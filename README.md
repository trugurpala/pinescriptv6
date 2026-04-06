# Pine Script v6 Reference

<div align="center">

![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Compatible-131722?style=for-the-badge&logo=tradingview)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Author](https://img.shields.io/badge/Yapımcı-Uğur%20Pala-F59E0B?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Katkı-Bekleniyor-8B5CF6?style=for-the-badge)

**TradingView Pine Script v6 için AI destekli geliştirme ortamı.**  
Tasarlayan ve geliştiren: [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com

[Hızlı Başlangıç](#hızlı-başlangıç) · [Cursor / Windsurf](#cursor--windsurf--copilot-ile-kullanım) · [Claude](#claude-projects-ile-kullanım) · [Dosya Yapısı](#dosya-yapısı) · [Katkı Sağla](#katkı-sağla)

</div>

---

## Bu Repo Ne?

Bu proje, TradingView'ın resmi Pine Script v6 dokümantasyonunu temel kaynak olarak alıp
**yapay zeka destekli geliştirme için baştan tasarlanmış** bir bilgi tabanına dönüştürür.

Temel kaynak olan TradingView dokümantasyonuna, bu repoda tamamen özgün bir sistem eklenmiştir:

- **LESSONS_LEARNED.md** — AI her hata çözümünde buraya yazar. Bir sonraki oturumda önce bunu okur, aynı hatayı bir daha yapmaz. *(Bu fikir ve sistem Uğur Pala tarafından tasarlanmıştır.)*
- **LLM_MANIFEST.md** — AI'ın hangi sorud a hangi dosyayı okuyacağını belirten yönlendirme haritası. Tüm repoyu bağlam penceresine yüklemek yerine sadece ilgili dosyayı çeker.
- **SKILL.md** — AI'ın bu repodaki yazma protokolü: önce hataları kontrol et, doğru referansı bul, temiz v6 kodu yaz.
- **Claude / Cursor / Windsurf / Copilot entegrasyonu** — kutu açılır açılmaz hazır.

> **Not:** Bu reponun yapısı, içeriği ve sistemi bütünüyle Uğur Pala tarafından tasarlanmış ve üretilmiştir.
> Temel referans materyali olarak TradingView'ın resmi Pine Script v6 dokümantasyonundan yararlanılmıştır.
> TradingView bu repoyla herhangi bir bağlantısı veya onayı bulunmamaktadır.

---

## Hızlı Başlangıç

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

## Claude Projects ile Kullanım

1. [Claude.ai](https://claude.ai) → Projects → projeniz
2. Files → **+** → GitHub → yapıştır:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
3. Tüm dosyaları seç → **Add files**
4. Sohbette `/pinescript-v6` yazarak skill'i aktifleştir

---

## Cursor / Windsurf / Copilot ile Kullanım

Repoyu klonlayın — `.cursorrules` ve `.github/copilot-instructions.md` otomatik olarak devreye girer.

Ya da dosyaları doğrudan referans olarak kullanın:

| Görev | Referans Dosyası |
|-------|-----------------|
| İndikatör yazıyorum | `@reference/functions/ta.md` + `@reference/functions/drawing.md` |
| Strateji yazıyorum | `@reference/functions/strategy.md` |
| Çoklu zaman dilimi | `@reference/functions/request.md` |
| Hata alıyorum | `@concepts/common_errors.md` |
| **Her şeyden önce** | `@LESSONS_LEARNED.md` — daima ilk okunacak dosya |

---

## Custom GPT veya Diğer LLM'ler ile Kullanım

1. Repoyu ZIP olarak indirin
2. Custom GPT Knowledge veya RAG sisteminize yükleyin
3. Önerilen minimum yükleme: `LLM_MANIFEST.md` + `LESSONS_LEARNED.md` + `reference/functions/` klasörü

---

## Dosya Yapısı

```
pinescriptv6/
│
├── LESSONS_LEARNED.md          ← Hata hafızası (AI her çözümde buraya yazar)
├── SKILL.md                    ← AI yazma protokolü
├── LLM_MANIFEST.md             ← Sorgu yönlendirme haritası
│
├── concepts/
│   ├── execution_model.md      ← Bar-by-bar model, var/varip, barstate
│   ├── common_errors.md        ← max_bars_back, series type, repainting hataları
│   ├── timeframes.md           ← Çoklu zaman dilimi, request.security
│   ├── colors_and_display.md   ← color.new, from_gradient, bgcolor
│   ├── methods.md              ← Kullanıcı tanımlı metodlar
│   └── objects.md              ← UDT, tip sistemi
│
├── reference/
│   ├── variables.md            ← open, close, high, low, bar_index, syminfo.*
│   ├── constants.md            ← color.*, shape.*, plot.style_*, size.*
│   ├── types.md                ← int, float, bool, series, simple, input
│   ├── keywords.md             ← if, for, while, var, varip, switch, export
│   ├── annotations.md          ← @version, @param, @returns, @type
│   └── functions/
│       ├── ta.md               ← RSI, EMA, SMA, MACD, ATR, BB, crossover, pivot
│       ├── strategy.md         ← entry, exit, close, position_size, equity
│       ├── drawing.md          ← plot, line, box, label, table, fill
│       ├── request.md          ← request.security, financial, currency_rate
│       ├── collections.md      ← array, map, matrix
│       └── general.md          ← math, str, input, alert, timestamp
│
└── writing_scripts/
    ├── style_guide.md          ← İsimlendirme, sıralama, yorum standartları
    ├── debugging.md            ← Pine Logs, plot debug, tablo panelleri
    ├── profiling_and_optimization.md
    └── limitations.md          ← Çizim limitleri, istek limitleri, buffer limitleri
```

---

## LESSONS_LEARNED Nasıl Çalışır?

Bu reponun özgün ve en değerli özelliği.

Bu repoyu kullanan bir AI Pine Script v6 hatası alıp çözdüğünde:

1. Hata, sebebi ve çözümü belgelenir
2. **`LESSONS_LEARNED.md` bu repoda otomatik olarak güncellenir**
3. Sonraki oturumda AI, kod yazmadan önce bu dosyayı okur
4. Aynı hata bir daha yapılmaz

Zaman içinde bu dosya, gerçek dünya Pine Script v6 hatalarından oluşan canlı, büyüyen bir bilgi tabanına dönüşür.

---

## Katkı Sağla

Katkılarınızı bekliyoruz! Detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

---

## Lisans

MIT — detaylar için [LICENSE](LICENSE) dosyasına bakın.  
Telif Hakkı © 2025 [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com

> Bu repo MIT lisansı ile dağıtılmaktadır. Kullanabilir, kopyalayabilir, değiştirebilir ve
> dağıtabilirsiniz — tek şart telif hakkı bildiriminin korunmasıdır.
