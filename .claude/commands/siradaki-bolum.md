---
description: Sıradaki onaylı bölümü baştan sona üretir (plan, kontrol, üretim, denetim, kayıt)
argument-hint: "[480p|720p]"
---

Sıradaki bölümü üret. Kalite: $ARGUMENTS (boşsa `dizi/dizi.json` → `butce.varsayilan_kalite`).

1. **Seç.** `dizi/durum.json` oku. `uretim` alanı boş olan ilk bölümü al. Onun `script_onayi` boşsa DUR ve şunu söyle: "E0N script'i Selma'nın onayını bekliyor." Başka hiçbir şey yapma.
2. **Planla.** `yonetmen` alt-ajanına bölüm numarasını ver. Raporunda eksik referans varsa DUR, listeyi ve görsel başına fiyatı (`dizi.json` → `fiyat.kredi_gorsel`) göster, onay iste.
3. **Kontrol.** `python3 arac/kontrol.py N` çalıştır. `TAMAM` değilse yönetmene geri gönder (en çok iki tur).
4. **Bütçe.** Kontrolün yazdığı tahmini krediyi bölüm tavanıyla karşılaştır. Aşıyorsa DUR ve sor.
5. **Üret.** `uretici` alt-ajanına bölüm numarasını, kaliteyi ve tavanı ver.
6. **Denetle.** `denetci` alt-ajanına bölüm numarasını ver. Raporu `uretim/E0N/denetim.md`.
7. **Kaydet.** `dizi/durum.json` içinde bölümün `uretim`, `cikti`, `kredi`, `dakika` alanlarını doldur; `selma_hukmu: "bekliyor"`. `dizi/notlar.md` dosyasında "kim neyi biliyor" ve "nesneler nerede" bölümlerini bu bölümün sonuna göre güncelle.
8. **Raporla.** Bölümün yolu, süre, kredi, denetçinin hükmü ve en önemli üç bulgu. Kusurlu klip için yeniden üretim ÖNERME dışında bir şey yapma; karar Selma'nın.
