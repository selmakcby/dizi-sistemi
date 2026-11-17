#!/bin/bash
# Bir bölümün indirilen kliplerini ölçer: ölçü, süre, kare dizisi, ses dökümü. Kredi harcamaz.
# Kullanım: bash arac/olc.sh <bolum_no>
set -euo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
NO="$(printf '%02d' "${1:?bölüm no gerekli}")"
CIKTI="$KOK/uretim/E$NO/cikti"
[ -d "$CIKTI" ] || { echo "Klasör yok: $CIKTI" >&2; exit 1; }
cd "$CIKTI"
echo "[" > olcum.json
ILK=1
for KLIP in klip-?.mp4; do
  [ -f "$KLIP" ] || { echo "İndirilmiş klip yok" >&2; exit 1; }
  AD="${KLIP%.mp4}"
  OLCU="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$KLIP")"
  SURE="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$KLIP")"
  SES="$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$KLIP" || true)"
  G="${OLCU%,*}"; Y="${OLCU#*,}"
  DIKEY=false; [ "$G" -lt "$Y" ] && DIKEY=true
  ffmpeg -v error -y -i "$KLIP" -vf "fps=1,scale=240:-1,tile=6x2" -frames:v 1 "$AD-kareler.jpg"
  ffmpeg -v error -y -i "$KLIP" -ac 1 -ar 16000 "$AD.wav"
  mlx_whisper "$AD.wav" --model mlx-community/whisper-large-v3-turbo --language en --output-dir . --output-format txt >/dev/null 2>&1 || echo "(döküm alınamadı)" > "$AD.txt"
  rm -f "$AD.wav"
  [ "$ILK" = 1 ] || echo "," >> olcum.json
  ILK=0
  printf '  {"klip": "%s", "genislik": %s, "yukseklik": %s, "dikey": %s, "sure": %s, "ses": "%s"}' "$AD" "$G" "$Y" "$DIKEY" "$SURE" "${SES:-yok}" >> olcum.json
  echo "$AD: ${G}x${Y} dikey=$DIKEY ${SURE}s ses=${SES:-yok}"
done
echo "" >> olcum.json
echo "]" >> olcum.json
