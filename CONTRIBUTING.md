# Contributing

> TR: Katkıda bulunmak için karmaşık bir süreç yok. Üç yol var, en değerlisi birincisi.
> EN: No complex process here. Three ways to contribute — the most valuable is the first.

---

## TR | Türkçe

### 1 — LESSONS_LEARNED.md'ye Hata Ekle

Pine Script v6 yazarken bir hatayla karşılaşıp çözdün mü? Buraya ekle.
Hem sen hem de bu repoyu kullanan herkes aynı hataya bir daha düşmez.

```markdown
### [Hatanın kısa adı]
- **Hata mesajı:** TradingView'dan birebir kopyala
- **Sebep:** Neden oluşuyor?
- **Çözüm:** Nasıl düzeltilir?
```

```pine
//@version=6
// Örnek

// ❌ Yanlış
plot(close[length])  // "length" burada series olamaz

// ✅ Doğru
int len = input.int(14, "Length")
plot(close[len])
```

---

### 2 — Referans Dosyası Geliştir

Eksik fonksiyon, yanlış imza, daha iyi örnek — PR gönder.

```bash
git clone https://github.com/trugurpala/pinescriptv6
# ilgili .md dosyasını düzenle
git checkout -b fix/ta-pivothigh-signature
git commit -m "fix: ta.pivothigh imzası güncellendi"
```

---

### 3 — Commit Mesaj Formatı

```
docs:   ta.wma örneği eklendi
fix:    strategy.exit imzası düzeltildi
lesson: request.security repainting çözümü eklendi
feat:   yeni konsept dosyası eklendi
```

**Kural:** `//@version=6` zorunlu · v5 syntax kabul edilmez · test edilmemiş kod gönderme

---

## EN | English

### 1 — Add to LESSONS_LEARNED.md

Hit a Pine Script v6 error and solved it? Add it here.
Saves everyone using this repo from hitting the same wall twice.

```markdown
### [Short name for the error]
- **Error message:** Copy verbatim from TradingView
- **Cause:** Why does it happen?
- **Fix:** How to resolve it
```

```pine
//@version=6
// Example

// ❌ Wrong
plot(close[length])  // "length" cannot be series here

// ✅ Correct
int len = input.int(14, "Length")
plot(close[len])
```

---

### 2 — Improve a Reference File

Missing function, wrong signature, better example — open a PR.

```bash
git clone https://github.com/trugurpala/pinescriptv6
# edit the relevant .md file
git checkout -b fix/ta-pivothigh-signature
git commit -m "fix: update ta.pivothigh signature"
```

---

### 3 — Commit Message Format

```
docs:   add ta.wma example
fix:    correct strategy.exit signature
lesson: add request.security repainting fix
feat:   add new concept file
```

**Rules:** `//@version=6` required · no v5 syntax · no untested code

---

mail@ugurpala.com · [github.com/trugurpala](https://github.com/trugurpala)
