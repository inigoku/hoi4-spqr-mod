#!/bin/zsh
setopt errexit

MOD="/Users/inigobarrerabarcelo/Documents/Paradox Interactive/Hearts of Iron IV/mod/spqr"

make_portrait() {
  local tag="$1"
  local filename="$2"
  local bg="$3"
  local dir="$MOD/gfx/leaders/$tag"
  local tmp_png

  mkdir -p "$dir"
  tmp_png="$(mktemp -t "${tag}_portrait").png"

  ffmpeg -loglevel error -y \
    -f lavfi -i "color=c=${bg}:s=156x212:d=1" \
    -frames:v 1 \
    -vf "drawbox=x=8:y=8:w=140:h=196:t=3:color=white@0.35,drawbox=x=46:y=34:w=64:h=64:t=fill:color=0xDCC7A7,drawbox=x=32:y=96:w=92:h=72:t=fill:color=0x4A3526,drawbox=x=12:y=150:w=132:h=46:t=fill:color=black@0.18,drawbox=x=56:y=24:w=44:h=12:t=fill:color=black@0.22" \
    "$tmp_png"

  sips -s format tga "$tmp_png" --out "$dir/$filename" >/dev/null
  rm -f "$tmp_png"
}

make_portrait "SBN" "Portrait_Alexander_II.tga" "0x2E6A2E"
make_portrait "ETR" "Portrait_Zelalsen.tga" "0x8E5A32"
make_portrait "SMN" "Portrait_Egnatius.tga" "0x789650"
make_portrait "SYC" "Portrait_Gelon.tga" "0xB89C58"
make_portrait "GRC" "Portrait_Solon.tga" "0x466EA8"
make_portrait "LAC" "Portrait_Leonidas.tga" "0xA13A3A"
make_portrait "MCD" "Portrait_Alexander.tga" "0x4D6FA8"
make_portrait "CRG" "Portrait_Hanno.tga" "0x8A4A26"
make_portrait "PHN" "Portrait_Baga.tga" "0x7D347D"
make_portrait "KMT" "Portrait_Psamtik.tga" "0xC9A24C"
make_portrait "ASS" "Portrait_Ashurbanipal.tga" "0x6E4E2A"
make_portrait "IBR" "Portrait_Indibilis.tga" "0x4C9C68"
make_portrait "GLN" "Portrait_Aristarchos.tga" "0x5C9C5C"
make_portrait "ILL" "Portrait_Bardylis.tga" "0x6B8CA0"
make_portrait "THR" "Portrait_Teres.tga" "0x8C6A42"
make_portrait "LYD" "Portrait_Croesus.tga" "0xC2A04A"

find "$MOD/gfx/leaders" -maxdepth 2 -type f | sort
