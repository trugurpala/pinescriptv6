# Types
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Temel Tipler
```pine
int     // tam sayı
float   // ondalıklı sayı
bool    // true / false
string  // metin
color   // renk değeri
```

### Özel Tipler
```pine
line      linefill    box       polyline
label     table       chart.point
array<T>  matrix<T>  map<K,V>
```

### Tip Niteleyicileri

| Niteleyici | Anlam |
|------------|-------|
| `const` | Derleme zamanında sabit |
| `simple` | Script başlarken bir kere belirlenir |
| `input` | Kullanıcı tarafından belirlenir |
| `series` | Her barda değişebilir (en esnek) |

Esneklik sırası: `const` → `simple` → `input` → `series`

### Tip Dönüşümü
```pine
int(3.7)                     // 3
float(3)                     // 3.0
str.tostring(3.14)           // "3.14"
str.tostring(3.14, "#.##")   // "3.14"
str.tofloat("3.14")          // 3.14
str.toint("42")              // 42
```

### na Kontrolü
```pine
na(close)          // true ise close na
nz(close, 0.0)     // close na ise 0.0 döndür
not na(myVar)      // na değilse
```

---

## EN | English

### Basic Types
```pine
int     // integer
float   // decimal
bool    // true / false
string  // text
color   // color value
```

### Special Types
```pine
line      linefill    box       polyline
label     table       chart.point
array<T>  matrix<T>  map<K,V>
```

### Type Qualifiers

| Qualifier | Meaning |
|-----------|---------|
| `const` | Fixed at compile time |
| `simple` | Determined once at script start |
| `input` | Determined by user |
| `series` | Can change on every bar (most flexible) |

Flexibility order: `const` → `simple` → `input` → `series`

### Type Conversion
```pine
int(3.7)                     // 3
float(3)                     // 3.0
str.tostring(3.14)           // "3.14"
str.tostring(3.14, "#.##")   // "3.14"
str.tofloat("3.14")          // 3.14
str.toint("42")              // 42
```

### na Check
```pine
na(close)          // true if close is na
nz(close, 0.0)     // return 0.0 if close is na
not na(myVar)      // if not na
```
