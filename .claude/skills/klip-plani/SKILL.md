---
name: klip-plani
description: Onaylı bir bölüm script'ini Higgsfield (Seedance) klip isteklerine çevirmenin kuralları ve şablonu. Bir bölümün klip isteklerini yazarken ya da düzeltirken yükle.
---

# Klip planı

Video modeli çift tırnak içindeki her kelimeyi seslendirir, eklenen her görseli çizer ve boş kalan her saniyeyi uydurma sözle doldurur. Sonucu yalnız saniyede bir kare olarak görebiliriz, sesini dinleyemeyiz. Bu yüzden istek gönderilmeden önce doğru olmalı.

## 1. Bölümü kliplere böl
- Bölüm yaklaşık 60 saniye; **beş klip, her biri 12 saniye**. Klip süresi 4-30 saniye arası tam sayı olabilir; 12 saniye bu dizide denendi ve tuttu.
- Bir klip tek mekânda geçer. Her replik tek bir klibin içinde başlar ve biter.
- Klibi tamamlanmış bir repliğin hemen ardından böl; sonraki klip öbür karakterle açılsın.
- Bölümün son klibi: son replikten sonra 3-4 saniye; kararı açık kalan kişinin yüzüne yavaş yaklaşma, cevap gelmeden kesme.
- Her klip kendi başına üretilir (uzatma modu yok). Bu yüzden her klibin **Opening** satırı, önceki klibin son anını kelimelerle yeniden kurar: kim nerede, elinde ne var, kapı açık mı, kapak açık mı.

## 2. Çekimler
- Klip başına 5-6 çekim; çoğu 1,5-2,5 saniye.
- **Bir çekimde tek kişi, tek hareket.** Kalabalık çekim okunmuyor (17 Kas dersi).
- Konuşan yüz yakın çekimde (`close, cut at the collarbones`). Dikey karede iki kişiyi yan yana değil, derinlikte ayır.
- Mekânda en çok bir geniş çekim, replik taşımaz.
- El ya da nesne çekimi (`close on hands`) yalnız olay oysa: destenin cepten çıkması, anahtarın alınması.
- Bakışlar kameraya gelmez: `his look passing right of the lens, level`.
- Her çekim satırı hareketle açılır ve kadrajdaki herkesi adlandırır; kimse yoksa arkada ne olduğunu söyler (`only the shelves of tea glasses behind him`). Adlandırılmayan kadraj uydurma insanla dolar.
- Duygu adı, nefes, iç çekme, gözyaşı, ekranda yazı yok.

## 3. Konuşma zamanlaması
- Replik penceresi = kelime ÷ 3 saniye, en çok 0,5 saniye fazlası. En hızlı 3,5 kelime/saniye.
- İki replik arasında 0,2-0,4 saniye; bir aksiyondan sonra 1-2 saniye.
- Aynı kişinin art arda replikleri tek Audio satırında, tek tırnakta birleşir.
- Her konuşan için bir bütçe cümlesi yaz; hiç konuşmayanları adlandır.
- Ses kartı (`dizi.json` → `karakterler.*.ses`) klipte o kişinin ilk Audio satırında bir kez, kelimesi kelimesine yazılır.
- Teslim notu tek kısa tavır (`quiet and even`); replikteki bir kelimeyi içermez.

## 4. Referanslar
- Sıra: mekân, o klipte görünen karakterler, önemli nesneler. `klip-K.refs.txt` içine `dizi.json` adlarıyla, satır başına bir tane.
- İstekte `Image reference N (kind Name): ... 100% as in the reference.` satırları aynı sırayla.
- Görseli gösteren şeyi kelimeyle yeniden tarif etme (yüz, saç, kıyafet, renk): ikinci bir sürüm çizilir.
- Önemli nesnenin (sandık, çanta) referansı şart; yoksa klipten klibe değişir.
- Yalnız sesi duyulan kişi eklenmez.

## 5. İstek metninin sırası (her satır kendi satırında)
1. `STRICT RULE: Absolutely no music, only diegetic sounds.`
2. Stil cümlesi + mekânın ışık cümlesi (`dizi.json`; her klipte kelimesi kelimesine aynı).
3. Referans satırları.
4. `Continuity:` satırı (her karakter için "clean and unchanged from the reference").
5. `In frame only: ...` kadro ve yerleşim, sonu `Eyelines never at the camera.`
6. `Opening: ...`
7. Konuşma bütçeleri.
8. Niyet cümleleri (karakter başına bir tane; ne istiyor ve hangi itkiyle: grit, willpower, persistence, resilience, tenacity).
9. `Pace: tight and pressing; every shot opens in motion, a beat only where a line lands.`
10. Çekim satırları: `S1 0.0-1.8s · size, camera, height, movement · action`.
11. Dil satırı, sonra Audio satırları: `S3 (3.0-5.2s) Hasan to Kerem, <ses kartı>, <tavır>: "..."`, sonra `No speech in S2, S5.`
12. `Restrictions:` bloğu (örnekteki dört satır + nesne kilidi satırı).

Tam örnekler: `ornek/uretim-E01/klip-1.prompt.txt` … `klip-5.prompt.txt`.

## 6. Riskli kalıplar (göndermeden önce tara)
- Klibin son 2 saniyesine sıkışmış temas (itme, yakalama, düşme): kendi çekimini ver, en az 1,5 saniye.
- Kadraj dışındaki bir elin tuttuğu şey: iki bedeni de kadraja al.
- Bir çekimde ikiden fazla hareket.
- Görünmeden değişen durum (şapkanın çıkması, kapağın kapanması): değişimi gösteren bir çekim şart.
- Küçük ayrıntıya bağlı kanca (cepten görünen kâğıt ucu): büyüt, el çekimi yap.
- Çay evi masasında oyun tahtası gerekiyorsa `a backgammon board` yaz ve "no chess pieces" yazma; model olumsuzu çizer. Tahtayı çekim satırında bir kez adlandır.

## 7. Kontrol
`python3 arac/kontrol.py N` şunları denetler: her script repliği isteklerde kelimesi kelimesine ve sırayla bir kez geçiyor mu; referans adları `dizi.json` içinde var mı ve işi dolu mu; referans satır sayısı uyuyor mu; süre 4-30 saniye mi; konuşma hızı sınırın altında mı; istek 20.000 karakterin altında mı. `TAMAM` yazmadan üretime geçilmez.
