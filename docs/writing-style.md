# Kamusal yazım ilkeleri

Bu belge README, katkı rehberi, destek metni ve GitHub açıklamaları için kalıcı yazım ölçütüdür. Amaç, teknik doğruluğu korurken insan gibi konuşmaktır.

## İnsan önce, sistem sonra

Okura önce ne yapabileceğini ve hangi sonucu alacağını söyleyin. Dosya adlarını, veri modelini ve iç mimariyi ancak karar vermesine yardım ediyorsa anlatın.

- Doğrudan okura seslenin
- Etken cümle kurun
- Bir cümlede tek ana düşünce taşıyın
- Gerekli teknik terimi ilk kullanımda açıklayın
- Özellik listesinden önce gerçek kullanım yolunu gösterin
- Kanıtlanmayan sonucu vaat etmeyin

## Doğal Türkçe

Türkçe metin birebir çeviri değildir. Aynı gerçeği Türkçede doğal duyulan biçimde anlatır.

- `audit` yerine **denetim**
- `provenance` yerine **kaynak izi** veya **kaynağın nasıl izlendiği**
- `credential` yerine **kimlik bilgisi**
- `telemetry` yerine **kullanım verisi gönderimi**
- `runtime dependency` yerine **çalışma bağımlılığı**
- `build` yerine bağlama göre **üretim**, **paketleme** veya **derleme**
- `script` yerine bağlama göre **Pine kodu**, **gösterge**, **strateji** veya **betik**

Kod içindeki sabit adları çevirmeyin. `structural-only` gibi kayıt değerlerini teknik tabloda koruyun; önce düz Türkçe anlamını verin.

## Cümle ve bölüm düzeni

- Hedef, çoğu cümleyi 20 kelimenin altında tutmaktır
- Bir paragraf iki ile dört cümle arasında kalır
- Üç veya daha fazla eş görevli öğeyi listeye çevirin
- Başlıkta bölümün işini açıkça söyleyin
- Kod bloğundan önce ne yaptığını, ardından beklenen sonucu açıklayın
- Bağlantı metni gideceği yeri adlandırır; “buraya tıklayın” yazmayın

## Kanıt dili

“Hazır”, “test edildi”, “GitHub’a gönderildi”, “release yayımlandı” ve “canlıda doğrulandı” ayrı durumlardır. Yerel denetim, Pine kodunun TradingView’de derlendiğini göstermez. Görsel veya metin, kanıt seviyesini renk dışında bir etiketle de belirtir.

## Kaynaklar

- [Türkçe Yazım Kuralları](https://pdb.hacettepe.edu.tr/baharhizmeticiegitim/TDK_Yazim_Kurallari_200319.pdf)
- [Vercel Writing Guidelines](https://github.com/vercel-labs/writing-guidelines/blob/main/command.md)
- [turkiye-iban README](https://github.com/trugurpala/turkiye-iban/blob/main/README.md)

Bu kaynaklar birbiriyle çatışırsa Türkçe yazımında TDK, teknik doğrulukta proje kanıt kayıtları belirleyicidir. Diğer rehberler okunabilirlik için yardımcı ölçüttür.
