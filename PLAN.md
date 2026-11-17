# Plan: bir bölüm nasıl çıkar

```
script (sen yazarsın ya da skill ile yazdırırsın)
   │  onayın
   ▼
YÖNETMEN ── script'i 5 klip isteğine çevirir ──► uretim/E0N/klip-K.prompt.txt
   │
   ▼
KONTROL (arac/kontrol.py) ── replikler kelimesi kelimesine mi, referanslar tam mı, bütçe tutuyor mu
   │  TAMAM
   ▼
ÜRETİCİ ── Higgsfield MCP ── fiyat sor → gönder → bekle → indir → ölç → birleştir
   │
   ▼
DENETÇİ ── kare dizileri + ses dökümü ↔ script ──► uretim/E0N/denetim.md
   │
   ▼
YAPIMCI (ana oturum) ── durumu ve notları günceller, sana raporlar
   │  hükmün
   ▼
sıradaki bölüm
```

## Adımlar ve kim yapar
| # | Adım | Kim | Kredi harcar mı |
|---|---|---|---|
| 0 | Diziyi kur (`/yeni-dizi`): stil, karakter, mekân, nesne görselleri | Yapımcı | Evet, onayınla (görsel başına yaklaşık 2,5) |
| 1 | Script | Sen, ya da `short-drama-studio-script` skill'i | Hayır |
| 2 | Script onayı | Sen | Hayır |
| 3 | Klip planı | Yönetmen | Hayır |
| 4 | Kontrol | `arac/kontrol.py` | Hayır |
| 5 | Üretim | Üretici | Evet (480p'de saniyesi yaklaşık 3) |
| 6 | Denetim | Denetçi | Hayır |
| 7 | Kayıt ve rapor | Yapımcı | Hayır |

## Neden üç ayrı ajan
- **Yönetmenin Higgsfield'a erişimi yok.** Planlayan, kredi harcayamaz.
- **Üretici isteği değiştiremez.** Gönderen, yaratıcı karar veremez; başarılı klibi yeniden gönderemez.
- **Denetçi dosya değiştiremez.** Denetleyen, kendi bulduğunu düzeltip üstünü örtemez.

## Ölçülen değerler (17 Kas 2026, ilk bölüm)
- 60 saniyelik bölüm = 5 klip × 12 saniye, 480p: 180 kredi.
- Beş klip aynı anda üretildi; hepsi yaklaşık 6 dakikada bitti.
- Karakter, mekân ve nesne görselleri: tanesi 2,5 kredi.
