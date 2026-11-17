---
description: Sıradaki onaylı bölümü baştan sona üretir (girdi, plan ve fiyat, onay, üretim, denetim, kayıt)
argument-hint: "[480p|720p]"
---

Sıradaki bölümü üret. Kalite: $ARGUMENTS (boşsa `dizi/dizi.json` → `butce.varsayilan_kalite`). Yöntem: `dizi/dizi.json` → `uretim.yontem`.

1. **Seç.** `dizi/durum.json` oku. `uretim` alanı boş olan ilk bölümü al. Onun `script_onayi` boşsa DUR ve şunu söyle: "E0N script'i Selma'nın onayını bekliyor." Başka hiçbir şey yapma.
2. **Hazırla.** `yonetmen` alt-ajanına bölüm numarasını ve yöntemi ver. Raporunda eksik referans varsa DUR, listeyi ve görsel başına fiyatı (`dizi.json` → `fiyat.kredi_gorsel`) göster, onay iste.
3. **Planla ve fiyat al (ücretsiz).**
   - `short-drama`: `uretici` alt-ajanına bölüm numarasını, kaliteyi ve `plan` aşamasını ver. Dönüşte `uretim/E0N/plan-ekrani.md` ve toplam fiyat hazır olmalı.
   - `dogrudan`: `python3 arac/kontrol.py N` çalıştır. `TAMAM` değilse yönetmene geri gönder (en çok iki tur).
4. **Bütçe.** Toplam fiyatı bölüm tavanıyla (`butce.bolum_tavani_kredi`) karşılaştır. Aşıyorsa DUR ve sor.
5. **Üretim onayı.** `durum.json` içinde bölümün `uretim_onayi` alanı boşsa DUR: plan ekranını ve fiyatı göster, "E0N üretim onayı bekliyor" de. Onay cümlesini kullanıcı kendi sözüyle yazar; sen yazmazsın.
6. **Üret.** `uretici` alt-ajanına bölüm numarasını, kaliteyi, tavanı ve `uret` aşamasını ver.
7. **Denetle.** `denetci` alt-ajanına bölüm numarasını ver. Raporu `uretim/E0N/denetim.md`.
8. **Kaydet.** `dizi/durum.json` içinde bölümün `uretim`, `cikti`, `kredi`, `dakika` alanlarını doldur; `selma_hukmu: "bekliyor"`. `dizi/notlar.md` dosyasında "kim neyi biliyor" ve "nesneler nerede" bölümlerini bu bölümün sonuna göre güncelle.
9. **Raporla.** Bölümün yolu, süre, kredi, denetçinin hükmü ve en önemli üç bulgu. Kusurlu klip için yeniden üretim ÖNERME dışında bir şey yapma; karar kullanıcının.
