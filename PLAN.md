# Plan: bir bölüm nasıl çıkar

```
script (sen yazarsın ya da skill ile yazdırırsın)
   │  script onayın
   ▼
YÖNETMEN ── bölümün girdi dosyasını yazar: stil, referanslar, önceki bölümün sonu ──► uretim/E0N/girdi.md
   │
   ▼
ÜRETİCİ, aşama "plan" ── Higgsfield /short-drama ── plan + fiyat (ücretsiz) ──► plan.json, plan-ekrani.md
   │
   ▼
YAPIMCI ── fiyat tavanın altında mı? üretim onayın var mı? yoksa DURUR
   │  üretim onayın (kendi cümlen)
   ▼
ÜRETİCİ, aşama "uret" ── /short-drama ── klipler → ölç → birleştir → kurgu
   │
   ▼
DENETÇİ ── kare dizileri + ses dökümü ↔ script ──► uretim/E0N/denetim.md
   │
   ▼
YAPIMCI ── durumu ve notları günceller, sana raporlar
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
| 3 | Girdi dosyası | Yönetmen | Hayır |
| 4 | Plan ve fiyat (`/short-drama`) | Üretici, aşama `plan` | Hayır |
| 5 | Üretim onayı | Sen | Hayır |
| 6 | Üretim (`/short-drama`) | Üretici, aşama `uret` | Evet |
| 7 | Denetim | Denetçi | Hayır |
| 8 | Kayıt ve rapor | Yapımcı | Hayır |

## İki yöntem
- `short-drama` (varsayılan): üretimi Higgsfield'ın kendi `/short-drama` komutu yürütür. Klipleri, birleştirmeyi ve kurguyu komut yapar.
- `dogrudan` (yedek): komut kullanılmaz; yönetmen klip isteklerini yazar, `arac/kontrol.py` denetler, üretici klipleri tek tek gönderir. `dizi/dizi.json` → `uretim.yontem` ile seçilir.

## Neden üç ayrı ajan
- **Yönetmenin Higgsfield'a erişimi yok.** Planlayan, kredi harcayamaz.
- **Üretici isteği değiştiremez.** Gönderen, yaratıcı karar veremez; başarılı klibi yeniden gönderemez.
- **Denetçi dosya değiştiremez.** Denetleyen, kendi bulduğunu düzeltip üstünü örtemez.

## Ölçülen değerler (17 Kas 2026, ilk bölüm)
- 60 saniyelik bölüm = 5 klip × 12 saniye, 480p: 180 kredi.
- Beş klip aynı anda üretildi; hepsi yaklaşık 6 dakikada bitti.
- Karakter, mekân ve nesne görselleri: tanesi 2,5 kredi.

## Durum (17 Kas 2026)
- `dogrudan` yöntemiyle ilk bölüm üretildi (yukarıdaki ölçümler).
- `short-drama` yönteminin plan aşaması elle denendi: 4 klip, 720p, toplam 441 kredi fiyat teklifi; hazır referans görselleri kabul edildi. Ücretli aşaması ve ajanların uçtan uca koşusu henüz DENENMEDİ.
