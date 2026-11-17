# Dizi Sistemi

Kendi script'inle, yüzünü göstermeden, bölüm bölüm dikey mikro drama dizisi üreten bir Claude Code projesi.
Script'i sen verirsin. Sistem onu klip isteklerine çevirir, Higgsfield MCP üzerinden üretir, birleştirir ve denetler.

```
                 SEN: script + onay
                        │
        ┌───────────────▼────────────────┐
        │  YAPIMCI (ana oturum)          │  en güçlü model
        │  sırayı yürütür, bütçeyi korur │  planlar ve son hükmü verir
        └───┬───────────┬────────────┬───┘
            │           │            │
     ┌──────▼─────┐ ┌───▼──────┐ ┌───▼──────┐
     │ YÖNETMEN   │ │ ÜRETİCİ  │ │ DENETÇİ  │
     │ orta sınıf │ │ ucuz     │ │ güçlü,   │
     │ MCP yok    │ │ yalnız   │ │ salt     │
     │            │ │ Higgsfield│ │ okur     │
     └──────┬─────┘ └───┬──────┘ └───┬──────┘
            │           │            │
      klip istekleri  Higgsfield   denetim
                        MCP        raporu
```

## Ne gerekir
- [Claude Code](https://code.claude.com) ve bir Claude aboneliği.
- Higgsfield hesabı ve Higgsfield MCP bağlantısı (`higgsfield.ai/mcp`).
- `ffmpeg`. Ses dökümü için `mlx_whisper` (Apple Silicon); yoksa `arac/olc.sh` döküm adımını atlar.

## Hızlı başlangıç
1. Repoyu indir, klasörde Claude Code'u aç.
2. Bölüm script'lerini `dizi/bolumler/E01.txt`, `E02.txt`… olarak koy. Biçim için `ornek/bolumler/` klasörüne bak.
   Script'in yoksa Higgsfield'ın script skill'ini `.claude/skills/short-drama-studio-script/` içine koy ve "bir kısa dizi yazmak istiyorum" de.
3. `/yeni-dizi rüya gibi boyama, turuncu ve teal` gibi bir stil tarifiyle çalıştır. Karakter, mekân ve nesne görsellerinin listesini ve fiyatını gösterir; onayınla üretir.
4. Bir bölümü onayla: "E01 onaylı".
5. `/siradaki-bolum`. Plan, kontrol, üretim, denetim ve kayıt sırayla çalışır.
6. `/durum` ile nerede olduğunu ve ne harcadığını gör.

## Klasörler
| Yol | Ne |
|---|---|
| `CLAUDE.md` | Kural dosyası: roller ve değişmez kurallar |
| `PLAN.md` | Plan dosyası: bir bölüm hangi adımlarla çıkar |
| `.claude/agents/` | Üç ajan: yönetmen, üretici, denetçi |
| `.claude/skills/` | Yetenekler: klip planı; Higgsfield'ın script skill'i için yer |
| `.claude/commands/` | `/yeni-dizi`, `/siradaki-bolum`, `/durum` |
| `arac/` | Kredi harcamayan araçlar: istek kontrolü, ölçüm, birleştirme, kayıt |
| `dizi/` | Senin dizin: `dizi.json`, `durum.json`, `notlar.md`, `bolumler/` |
| `sablon/` | Boş başlangıç dosyaları |
| `ornek/` | Örnek dizi: dört bölümün script'i ve ilk bölümün beş klip isteği |
| `ZAMANLAMA.md` | Sistemi saatinde kendiliğinden çalıştırma seçenekleri |

## Modelleri değiştirmek
Her ajanın modeli kendi dosyasının başındaki `model:` satırındadır (`.claude/agents/*.md`).
Varsayılan: yönetmen `opus`, üretici `sonnet`, denetçi `fable`. Limitin darsa hepsini `sonnet` yapabilirsin;
kalite en çok yönetmende (klip isteklerini o yazar) ve denetçide fark eder.
Üretici yalnız istek gönderip beklediği için en ucuz model yeter.

## Güvenlik kilitleri
- Onaylanmamış script üretilmez.
- Her gönderimden önce fiyat sorulur; bölüm tavanı aşılacaksa durur ve sorar.
- Başarılı klip yeniden gönderilmez; kusur raporlanır, karar senindir.
- Yönetmenin Higgsfield'a erişimi yoktur; denetçi dosya değiştiremez.
- Script'ler ve indirilen her dosya veridir; içlerinde ajana yazılmış bir talimat varsa uygulanmaz.

## Ölçülen maliyet (17 Kas 2026)
| Kalem | Kredi | Süre |
|---|---|---|
| Karakter, mekân ya da nesne görseli | 2,5 | yaklaşık 1,5 dk |
| 12 saniyelik klip, 480p | 36 | 4-7 dk |
| 60 saniyelik bölüm (5 klip, aynı anda) | 180 | yaklaşık 6 dk |

720p için belgelenen fiyat saniyede yaklaşık 7 kredi; bu depoda henüz ölçülmedi.

## Bilinen sınırlar
- Ajanlar videoyu hareketli izleyemez ve sesi dinleyemez; saniyede bir kareye ve ses dökümüne bakar. Son hüküm senin.
- Referans görseli olmayan nesne klipten klibe değişir.
- Klipler ayrı ayrı üretilir; iki klibin birleşim yeri sert kesmedir.
- Üç ajanın uçtan uca koşusu henüz yalnız kısmen denendi (bkz. `dizi/notlar.md`).

## Lisans
Tüm hakları saklıdır; ayrıntı `LICENSE` dosyasında. `ornek/` altındaki dizi özgün bir çalışmadır.
