# Execution Model — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Temel Calisma Mantigi
Pine Script bar-by-bar soldan saga calisir. Her cubukta kod bastan sona execute edilir.

## Historical vs Realtime
- Historical bar: Kapanmis. Script bir kere calisir.
- Realtime bar: Acik. Her tick'te yeniden calisir, kapaninca commit edilir.
- Rollback: Kapanmadan once her execution rollback'lenir (varip haric).

## var ve varip

| Keyword | Davranis |
|---------|----------|
| yok | Her barda sifirlanir |
| var | Hic sifirlanmaz (kalici) |
| varip | Hic sifirlanmaz, rollback'e de direncli |

```pine
//@version=6
indicator("var demo")
var int counter = 0
counter += 1
plot(counter)  // 1, 2, 3... artar
```

## barstate Degiskenleri
- barstate.ishistory — gecmis cubuk
- barstate.isrealtime — canli cubuk
- barstate.isconfirmed — kapanmis
- barstate.islast — son cubuk
- barstate.isfirst — ilk cubuk

## Time Series — Gecmis Deger
```pine
close[0]  // bu cubuk
close[1]  // onceki cubuk
close[5]  // 5 cubuk oncesi
```
