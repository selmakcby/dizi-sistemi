# Dizi sistemi

Bu klasör, özgün bir dikey mikro drama dizisini bölüm bölüm üreten bir Claude Code projesidir.
Üretim Higgsfield MCP üzerinden yapılır. Ana oturum yönetir ve denetler; işi alt-ajanlar yapar.

## Roller
| Rol | Kim | Model | İş |
|---|---|---|---|
| Yapımcı | ana oturum | en güçlü model | Sırayı yürütür, bütçeyi korur, son hükmü verir |
| Yönetmen | `.claude/agents/yonetmen.md` | orta sınıf | Onaylı script'i üretime hazırlar (girdi dosyası) |
| Üretici | `.claude/agents/uretici.md` | ucuz sınıf | Higgsfield'ın `/short-drama` komutunu çalıştırır: önce plan ve fiyat, onaydan sonra üretim |
| Denetçi | `.claude/agents/denetci.md` | en güçlü model, ayrı bağlam | Sonucu script'le karşılaştırır, kusur arar |

Script'i kullanıcı verir (`dizi/bolumler/E0N.txt`). İsterse Higgsfield'ın `short-drama-studio-script` skill'iyle yazdırır; sistem kendiliğinden script yazmaz. Üretim varsayılan olarak Higgsfield'ın `/short-drama` komutuyla yapılır (`dizi.json` → `uretim.yontem: "short-drama"`). Komutsuz, klip klip yol (`dogrudan`) yedektir; onda klip planı `klip-plani` skill'ine göre yapılır. Yeni bir dizi `/yeni-dizi` ile kurulur.

## Değişmez kurallar
1. **Onaysız üretim yok.** `dizi/durum.json` içinde `script_onayi` boş olan bölüm planlanmaz; `uretim_onayi` boş olan bölüm için ücretli hiçbir istek gönderilmez. İki onay da yalnız kullanıcının kendi cümlesidir; ajan onay cümlesi yazmaz, tamamlamaz.
2. **Bütçe.** Bölüm tavanı `dizi/dizi.json` → `butce.bolum_tavani_kredi`. Her gönderimden önce fiyat sorulur (ücretsiz fiyat sorgusu). Tavan aşılacaksa gönderilmez, Selma'ya sorulur.
3. **Başarılı klip yeniden gönderilmez.** Kusurlu bile olsa. Kusur raporlanır, kararı Selma verir. Başarısız iş (iade edilir) en çok bir kez yeniden gönderilir.
4. **Biçim.** Her klip `9:16`, `draft: false`. `short-drama` yönteminde klipler arası bağı komut kurar; her klip indirilince ölçülür, yatay gelen olursa sonraki gönderilmez. `dogrudan` yönteminde her klip `omni_reference`, `video_extension` kullanılmaz.
5. **Tutarlılık.** Her klibe o sahnedeki mekân, karakter ve önemli nesnelerin referans işleri eklenir (`dizi/dizi.json`). Stil cümlesi ve mekânın ışık cümlesi her klipte kelimesi kelimesine aynıdır.
6. **Özgünlük.** Var olan film, dizi, oyun, karakter, marka ya da gerçek kişi adı hiçbir script'e ya da isteğe girmez. Kalıp alınır, konu alınmaz.
7. **Dürüst rapor.** Ajanlar videoyu hareketli izleyemez ve sesi dinleyemez; yalnız saniyede bir kare ve ses dökümü görür. Raporda görülmeyen şey "gördüm" diye yazılmaz.
8. **Kayıt.** Her koşu `kayit/kosular.jsonl` dosyasına süre ve krediyle yazılır. Bölüm bitince `dizi/durum.json` ve `dizi/notlar.md` güncellenir.

## Klasörler
- `dizi/dizi.json`: stil, model ayarları, fiyat, bütçe, referans işleri.
- `dizi/bolumler/E0N.txt`: bölüm script'leri (skill biçimi).
- `dizi/durum.json`: hangi bölüm nerede.
- `dizi/notlar.md`: kim neyi biliyor, nesneler nerede, öğrenilenler.
- `uretim/E0N/`: `girdi.md`, `plan.json`, `plan-ekrani.md` (short-drama); klip istekleri (dogrudan); `cikti/`, `denetim.md`.
- `arac/`: `kontrol.py` (istekleri script'e karşı denetler), `olc.sh`, `birlestir.sh`, `kayit.py`.
- `kayit/kosular.jsonl`: koşu günlüğü.
- `sablon/`: boş başlangıç dosyaları. `ornek/`: örnek dizi (script'ler ve ilk bölümün istekleri).
- `PLAN.md`: adım adım akış. `ZAMANLAMA.md`: zamanlama seçenekleri.

## Komutlar
- `/yeni-dizi`: kullanıcının script'lerinden yeni bir dizi kurar (stil, referans görselleri).
- `/siradaki-bolum`: sıradaki onaylı bölümü baştan sona üretir.
- `/durum`: dizinin durumunu ve harcamayı özetler.
