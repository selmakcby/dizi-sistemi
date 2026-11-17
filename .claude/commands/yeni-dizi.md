---
description: Kendi script'lerinle yeni bir dizi kurar (stil, karakterler, mekânlar, referans görselleri)
argument-hint: "[stil tarifi]"
---

Kullanıcı kendi dizisini kurmak istiyor. Script'leri o verir; sen yazmazsın. Stil tarifi: $ARGUMENTS

1. **Script'leri bul.** `dizi/bolumler/` içindeki `E01.txt`, `E02.txt`… dosyalarını oku. Yoksa DUR: "Bölüm script'lerini `dizi/bolumler/E01.txt` biçiminde koy. Biçim için `.claude/skills/short-drama-studio-script` ya da `ornek/bolumler/` klasörüne bak." Script'te eksik varsa (yaşı olmayan karakter, yazılmamış giriş çıkış, okunması gereken yazı) listele; düzeltmeyi kullanıcı yapar.
2. **Mevcut diziyi koru.** `dizi/dizi.json` doluysa ve adı farklıysa DUR, kullanıcıya sor: üzerine yazılsın mı, yoksa `ornek/` altına mı taşınsın.
3. **Oku ve çıkar.** Bütün bölümlerden: karakterler (ad, yaş, görünüm satırı kelimesi kelimesine), mekânlar, hikâyenin döndüğü önemli nesneler (bölüm başına en çok 4).
4. **Stil.** Kullanıcı stil verdiyse onu kullan; vermediyse üç seçenek öner ve sor. Stili tek cümleye çevir: bir kez video için (`stil_cumlesi`), bir kez görsel için (`gorsel_stil_acilisi`).
5. **Yaz.** `sablon/dizi.json` kalıbından `dizi/dizi.json`; `dizi/durum.json` (her bölüm `script_onayi: null`); `dizi/notlar.md`.
6. **Referans listesi ve fiyat.** Gereken görselleri say (karakter başına bir sayfa, mekân başına bir görünüm, önemli nesne başına bir görsel), toplam krediyi söyle ve ONAY İSTE. Onaysız görsel üretme.
7. **Onaydan sonra** görselleri üret (`generate_image_batch`, model `dizi.json` → `model.gorsel`, 16:9, 2k), iş kimliklerini `dizi.json` içine yaz, görselleri `referans/` klasörüne indir ve kullanıcıya göster.
8. **Bitir.** "Bölümleri onaylamak için `dizi/durum.json` içinde `script_onayi` alanını doldur ya da bana 'E01 onaylı' de. Sonra `/siradaki-bolum`."
