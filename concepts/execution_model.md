# Execution Model
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Pine Script her cubukta soldan sağa, baştan sona çalışır.

### Historical vs Realtime

| Bar türü | Nasıl çalışır? |
|----------|----------------|
| **Historical** | Kapanmış bar. Script bir kere çalışır, sonuç commitlenir. |
| **Realtime** | Açık bar. Her tick'te yeniden çalışır. Kapanınca commit edilir. |
| **Rollback** | Realtime barda kapanış öncesi her execution rollback'lenir (`varip` hariç). |

```pine
//@version=6
indicator("Execution demo")
plot(barstate.ishistory  ? 1 : 0, "isHistory")
plot(barstate.isrealtime ? 1 : 0, "isRealtime")
plot(barstate.isconfirmed ? 1 : 0, "isClosed")
```

### var ve varip

| Keyword | Sıfırlanır mı? | Rollback? | Kullanım |
|---------|---------------|-----------|----------|
| *(yok)* | Her barda | Evet | Normal değişken |
| `var` | Hayır | Evet | Kümülatif sayaç, persistent state |
| `varip` | Hayır | **Hayır** | Realtime tick sayacı |

```pine
//@version=6
indicator("var demo")

// Normal — her barda 1
normalVar = 0
normalVar += 1
plot(normalVar)  // hep 1

// var — kümülatif
var int counter = 0
counter += 1
plot(counter)  // 1, 2, 3 ...
```

### Time Series — Geçmiş Değer

```pine
close[0]  // bu bar
close[1]  // bir önceki bar
close[5]  // 5 bar önce
```

### barstate Değişkenleri

```pine
barstate.ishistory   // geçmiş bar
barstate.isrealtime  // canlı bar
barstate.isconfirmed // kapanmış bar
barstate.islast      // son bar
barstate.isfirst     // ilk bar
barstate.isnew       // bar yeni mi açıldı?
```

---

## EN | English

Pine Script runs left to right, bar by bar, from top to bottom on every bar.

### Historical vs Realtime

| Bar type | How it works |
|----------|-------------|
| **Historical** | Closed bar. Script runs once, result committed. |
| **Realtime** | Open bar. Reruns on every tick. Committed on close. |
| **Rollback** | Before close, each execution is rolled back (`varip` exempt). |

### var and varip

| Keyword | Resets? | Rollback? | Use case |
|---------|---------|-----------|----------|
| *(none)* | Every bar | Yes | Normal variable |
| `var` | Never | Yes | Cumulative counter, persistent state |
| `varip` | Never | **No** | Realtime tick counter |

### Time Series — Historical Values

```pine
close[0]  // current bar
close[1]  // previous bar
close[5]  // 5 bars ago
```
