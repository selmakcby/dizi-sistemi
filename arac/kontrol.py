#!/usr/bin/env python3
"""Bir bölümün klip isteklerini script'e ve dizi.json'a karşı denetler. Kredi harcamaz.

Kullanım: python3 arac/kontrol.py <bolum_no> [kalite]
"""
import glob
import json
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
REPLIK = re.compile(r"^[A-Z][A-Z .]+: ")
SES = re.compile(r'^S\d+ \((\d+\.\d)-(\d+\.\d)s\) .*?: "(.*)"$')
CEKIM = re.compile(r"^S\d+ (\d+\.\d)-(\d+\.\d)s ")
EN_HIZLI = 3.5
ISTEK_SINIRI = 20000


def sade(metin: str) -> str:
    return re.sub(r"\s+", " ", metin.replace("’", "'")).strip()


def script_replikleri(yol: Path) -> list[str]:
    govde = yol.read_text().split("SCENE 1.", 1)[1]
    return [sade(s.split(": ", 1)[1]) for s in govde.split("\n") if REPLIK.match(s)]


def klibi_denetle(n: int, klasor: Path, dizi: dict) -> tuple[list[str], list[str], float]:
    sorun: list[str] = []
    istek = (klasor / f"klip-{n}.prompt.txt").read_text()
    refs = [r for r in (klasor / f"klip-{n}.refs.txt").read_text().split("\n") if r.strip()]
    satirlar = istek.split("\n")

    if len(istek) > ISTEK_SINIRI:
        sorun.append(f"klip {n}: istek {len(istek)} karakter, sınır {ISTEK_SINIRI}")
    bilinen = {**dizi["mekanlar"], **dizi["karakterler"], **dizi["nesneler"]}
    for r in refs:
        if r not in bilinen:
            sorun.append(f"klip {n}: bilinmeyen referans '{r}'")
        elif not bilinen[r].get("is"):
            sorun.append(f"klip {n}: '{r}' için referans görseli yok")
    ref_satiri = [s for s in satirlar if s.startswith("Image reference ")]
    if len(ref_satiri) != len(refs):
        sorun.append(f"klip {n}: {len(refs)} referans var, istekte {len(ref_satiri)} referans satırı")
    if not satirlar[0].startswith("STRICT RULE:"):
        sorun.append(f"klip {n}: ilk satır ses kuralı değil")
    if dizi["stil_cumlesi"] not in istek:
        sorun.append(f"klip {n}: stil cümlesi dizi.json ile aynı değil")
    for yasak in ("video_extension", "@", "<<<", "[["):
        if yasak in istek:
            sorun.append(f"klip {n}: istekte yasak ifade '{yasak}'")

    bitisler = [float(m.group(2)) for s in satirlar if (m := CEKIM.match(s))]
    sure = max(bitisler) if bitisler else 0.0
    if sure != int(sure) or not 4 <= sure <= 30:
        sorun.append(f"klip {n}: süre {sure} sn; 4-30 arası tam sayı olmalı")

    sozler: list[str] = []
    for s in satirlar:
        m = SES.match(s)
        if not m:
            continue
        bas, son, soz = float(m.group(1)), float(m.group(2)), sade(m.group(3))
        hiz = len(soz.split()) / max(son - bas, 0.1)
        if hiz > EN_HIZLI:
            sorun.append(f"klip {n}: '{soz}' {hiz:.1f} kelime/sn, sınır {EN_HIZLI}")
        if son > sure:
            sorun.append(f"klip {n}: '{soz}' klip bittikten sonra bitiyor")
        sozler.append(soz)
    return sorun, sozler, sure


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Kullanım: python3 arac/kontrol.py <bolum_no> [kalite]")
        return 2
    no = int(sys.argv[1])
    dizi = json.loads((KOK / "dizi" / "dizi.json").read_text())
    kalite = sys.argv[2] if len(sys.argv) > 2 else dizi["butce"]["varsayilan_kalite"]
    oran = dizi["fiyat"].get(f"kredi_saniye_{kalite}")
    if oran is None:
        print(f"SORUN: '{kalite}' için fiyat dizi.json içinde yok")
        return 1
    klasor = KOK / "uretim" / f"E{no:02d}"
    script = KOK / "dizi" / "bolumler" / f"E{no:02d}.txt"
    if not script.exists():
        print(f"SORUN: script yok: {script}")
        return 1
    klipler = sorted(int(re.search(r"klip-(\d+)", y).group(1)) for y in glob.glob(str(klasor / "klip-*.prompt.txt")))
    if not klipler:
        print(f"SORUN: {klasor} içinde klip isteği yok")
        return 1

    sorunlar: list[str] = []
    butun_sozler: list[str] = []
    toplam = 0.0
    for n in klipler:
        sorun, sozler, sure = klibi_denetle(n, klasor, dizi)
        sorunlar += sorun
        butun_sozler += sozler
        toplam += sure

    beklenen = " ".join(script_replikleri(script))
    bulunan = " ".join(butun_sozler)
    if beklenen != bulunan:
        b, f = beklenen.split(), bulunan.split()
        i = next((k for k, (x, y) in enumerate(zip(b, f)) if x != y), min(len(b), len(f)))
        sorunlar.append(
            "replikler script'le aynı değil; ilk fark: script '"
            + " ".join(b[max(0, i - 3): i + 4]) + "' / istek '" + " ".join(f[max(0, i - 3): i + 4]) + "'"
        )

    kredi = toplam * oran
    tavan = dizi["butce"]["bolum_tavani_kredi"]
    print(f"Bölüm {no}: {len(klipler)} klip, {toplam:.0f} sn, {kalite}, tahmini {kredi:.0f} kredi (tavan {tavan})")
    if kredi > tavan:
        sorunlar.append(f"tahmini {kredi:.0f} kredi bölüm tavanını ({tavan}) aşıyor")
    for s in sorunlar:
        print("SORUN:", s)
    print("TAMAM" if not sorunlar else f"{len(sorunlar)} sorun var")
    return 0 if not sorunlar else 1


if __name__ == "__main__":
    sys.exit(main())
