#!/bin/bash
# Bir bölümün dikey kliplerini numara sırasıyla uç uca ekler. Yatay klip atlanır ve söylenir.
# Kullanım: bash arac/birlestir.sh <bolum_no> [kalite_etiketi]
set -euo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
NO="$(printf '%02d' "${1:?bölüm no gerekli}")"
ETIKET="${2:-480p}"
CIKTI="$KOK/uretim/E$NO/cikti"
cd "$CIKTI"
GIRDI=(); SUZGEC=""; SAY=0
for KLIP in klip-?.mp4; do
  OLCU="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$KLIP")"
  if [ "${OLCU%,*}" -ge "${OLCU#*,}" ]; then echo "ATLANDI (yatay): $KLIP" >&2; continue; fi
  GIRDI+=(-i "$KLIP")
  SUZGEC+="[$SAY:v]fps=24,scale=-2:${OLCU#*,},setsar=1[v$SAY];[$SAY:a]aresample=44100[a$SAY];"
  SAY=$((SAY+1))
done
[ "$SAY" -gt 0 ] || { echo "Birleştirilecek dikey klip yok" >&2; exit 1; }
ZINCIR=""; for i in $(seq 0 $((SAY-1))); do ZINCIR+="[v$i][a$i]"; done
HEDEF="bolum-$NO-$ETIKET.mp4"
ffmpeg -v error -y "${GIRDI[@]}" -filter_complex "${SUZGEC}${ZINCIR}concat=n=$SAY:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -c:a aac "$HEDEF"
echo "$CIKTI/$HEDEF ($SAY klip, $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$HEDEF") sn)"
