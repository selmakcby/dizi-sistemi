#!/usr/bin/env python3
"""Bir üretim koşusunu kayit/kosular.jsonl dosyasına ekler.

Kullanım: python3 arac/kayit.py <bolum_no> <kredi> <dakika> <kalite> [not]
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    try:
        kayit = {
            "zaman": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "bolum": int(sys.argv[1]),
            "kredi": float(sys.argv[2]),
            "dakika": float(sys.argv[3]),
            "kalite": sys.argv[4],
            "not": " ".join(sys.argv[5:]),
        }
    except ValueError as hata:
        print(f"Geçersiz değer: {hata}")
        return 2
    yol = KOK / "kayit" / "kosular.jsonl"
    yol.parent.mkdir(exist_ok=True)
    with yol.open("a") as dosya:
        dosya.write(json.dumps(kayit, ensure_ascii=False) + "\n")
    print(f"Kaydedildi: bölüm {kayit['bolum']}, {kayit['kredi']:.0f} kredi, {kayit['dakika']:.0f} dk")
    return 0


if __name__ == "__main__":
    sys.exit(main())
