#!/usr/bin/env python3
"""
generate_loading_screens.py
Generates 15 loading screen DDS images for the SPQR mod using Google Imagen 4.
Uses the same API as generate_ai_portraits.py.

Requirements:
    pip install Pillow

Usage:
    export GOOGLE_API_KEY="your_api_key_here"
    python3 tools/generate_loading_screens.py
    python3 tools/generate_loading_screens.py --overwrite   # re-generate existing
    python3 tools/generate_loading_screens.py --dry-run     # print prompts only

Output:
    gfx/loadingscreens/load_spqr_1.dds  ...  load_spqr_15.dds       (1920x1440)
    gfx/loadingscreens/load_spqr_1_small.dds  ...  load_spqr_15_small.dds  (192x144)
    gfx/loadingscreens/png/load_spqr_N.png   (PNG backups, not used by the game)
"""

import argparse
import base64
import json
import os
import struct
import sys
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow is required.  Run:  pip install Pillow")
    sys.exit(1)

# ─── paths ───────────────────────────────────────────────────────────────────

MOD     = Path(__file__).resolve().parent.parent
OUT_DIR = MOD / "gfx" / "loadingscreens"
PNG_DIR = OUT_DIR / "png"

FULL_W,  FULL_H  = 1920, 1440
SMALL_W, SMALL_H = 192,  144

# ─── API ─────────────────────────────────────────────────────────────────────

IMAGEN_URL = (
    "https://generativelanguage.googleapis.com/v1beta"
    "/models/imagen-4.0-generate-001:predict"
)
REQUEST_DELAY = 3.0  # seconds between calls

# ─── style suffix ────────────────────────────────────────────────────────────

STYLE = (
    "epic historical painting style, cinematic wide composition, "
    "rich dramatic lighting, highly detailed ancient Mediterranean world, "
    "264 BC Punic Wars era, oil painting on canvas, no text or lettering"
)

# ─── 15 screens ──────────────────────────────────────────────────────────────

SCREENS = [
    (
        "load_spqr_1",
        "Hannibal Barca's war elephants crossing the snow-covered Alps in winter, "
        "Carthaginian soldiers and horses struggling through icy mountain passes, "
        "towering peaks draped in snow, storm clouds gathering, desperate and heroic "
        "atmosphere, wide panoramic landscape view. " + STYLE,
    ),
    (
        "load_spqr_2",
        "Ancient Roman quinqueremes and Carthaginian warships in massive naval battle "
        "during the First Punic War, bright Mediterranean sea, bronze rams splintering "
        "enemy hulls, marines fighting on deck, burning ships listing in the water, "
        "dramatic golden afternoon light. " + STYLE,
    ),
    (
        "load_spqr_3",
        "Battle of Cannae 216 BC, Hannibal's Carthaginian cavalry and infantry "
        "encircling Roman legions in a devastating double envelopment, wide aerial "
        "view of the Italian plain battlefield, dust clouds rising over thousands of "
        "soldiers, chaos and desperation. " + STYLE,
    ),
    (
        "load_spqr_4",
        "Ancient Roman legions and war galleys crossing the Strait of Messina to "
        "Sicily at dawn, troop transports escorted by quinqueremes, golden first light "
        "shimmering on the water, Mount Etna visible in the distance, majestic and "
        "epic beginning of the First Punic War. " + STYLE,
    ),
    (
        "load_spqr_5",
        "Battle of Zama 202 BC, Scipio Africanus commanding Roman legions against "
        "Hannibal's war elephants in the North African desert, elephants charging "
        "toward Roman lines while soldiers open lanes to let the great beasts through, "
        "heat and dust, decisive moment of ancient history. " + STYLE,
    ),
    (
        "load_spqr_6",
        "Battle of Ecnomus 256 BC, hundreds of Roman and Carthaginian warships "
        "clashing across the Mediterranean Sea in the largest naval battle of "
        "antiquity, Roman ships in wedge formation breaking the Carthaginian line, "
        "smoke, fire, and carnage on a breathtaking scale. " + STYLE,
    ),
    (
        "load_spqr_7",
        "Siege of Syracuse, Archimedes' giant iron claw war machines lifting Roman "
        "warships out of the harbour and dropping them into the sea, Greek city of "
        "Syracuse on Sicilian cliffs in the background, Roman fleet in disarray, "
        "sunset light over the ancient wonder of engineering. " + STYLE,
    ),
    (
        "load_spqr_8",
        "Hannibal Barca leading Carthaginian war elephants across the wide Rhone "
        "river on makeshift rafts, terrified elephants in the water, Gallic warriors "
        "watching from the far bank, autumn forest colours, river mist, dramatic "
        "and tense ancient river crossing. " + STYLE,
    ),
    (
        "load_spqr_9",
        "Macedonian phalanx in perfect battle formation, thousands of soldiers "
        "levelling their long sarissa spears in unison, mountain valley landscape of "
        "ancient Macedonia, golden armour and bronze shields gleaming in afternoon "
        "sunlight, dust rising from their advance. " + STYLE,
    ),
    (
        "load_spqr_10",
        "Battle of Raphia 217 BC, Ptolemaic Egyptian and Seleucid war elephants "
        "clashing in fierce combat, African forest elephants against Indian war "
        "elephants, desert landscape of the Sinai, thousands of soldiers fighting "
        "around the great beasts, dust and fury. " + STYLE,
    ),
    (
        "load_spqr_11",
        "Ancient harbour of Carthage at golden sunset, the circular Cothon military "
        "harbour with Phoenician warships arranged in perfect order, merchant vessels "
        "in the outer harbour, the great city rising on the hill, North African "
        "coast glowing in warm Mediterranean light. " + STYLE,
    ),
    (
        "load_spqr_12",
        "Greek trireme fleet sailing at dawn through the Aegean Sea past rocky "
        "islands, classical Greek warships with bronze rams and painted eyes on the "
        "prows, morning mist rising off the water, oarsmen pulling in perfect "
        "rhythm, beautiful and serene ancient seascape. " + STYLE,
    ),
    (
        "load_spqr_13",
        "Battle of Heraclea 280 BC, Pyrrhus of Epirus leading towering war elephants "
        "against Roman legions in the green hills of southern Italy, Roman soldiers "
        "breaking formation in terror before the great beasts, Epirote and Greek "
        "infantry following behind, dramatic ancient battle. " + STYLE,
    ),
    (
        "load_spqr_14",
        "Roman legionaries constructing a fortified military castra camp at dusk, "
        "perfectly organised square earthwork with rows of tents inside, soldiers "
        "digging ditches and raising palisades with methodical precision, campfires "
        "being lit, Italian countryside bathed in golden hour light. " + STYLE,
    ),
    (
        "load_spqr_15",
        "The great Lighthouse of Alexandria blazing with fire at night over the "
        "harbour, Ptolemaic warships and merchant vessels filling the water below, "
        "magnificent city of Alexandria glowing on the Egyptian coast, moonlit "
        "Mediterranean sea, the most spectacular wonder of the ancient world. " + STYLE,
    ),
]

# ─── DDS writer (uncompressed 32-bit ARGB, readable by HoI4) ─────────────────

def write_dds(path: Path, image: Image.Image) -> None:
    img = image.convert("RGBA")
    w, h = img.size

    DDSD_CAPS        = 0x00000001
    DDSD_HEIGHT      = 0x00000002
    DDSD_WIDTH       = 0x00000004
    DDSD_PITCH       = 0x00000008
    DDSD_PIXELFORMAT = 0x00001000
    DDPF_ALPHAPIXELS = 0x00000001
    DDPF_RGB         = 0x00000040
    DDSCAPS_TEXTURE  = 0x00001000

    flags = DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PITCH | DDSD_PIXELFORMAT

    with open(path, "wb") as f:
        f.write(b"DDS ")
        f.write(struct.pack("<I",   124))
        f.write(struct.pack("<I",   flags))
        f.write(struct.pack("<I",   h))
        f.write(struct.pack("<I",   w))
        f.write(struct.pack("<I",   w * 4))               # pitch
        f.write(struct.pack("<I",   0))                   # depth
        f.write(struct.pack("<I",   0))                   # mip count
        f.write(struct.pack("<11I", *([0] * 11)))         # reserved
        # pixel format
        f.write(struct.pack("<I",   32))
        f.write(struct.pack("<I",   DDPF_ALPHAPIXELS | DDPF_RGB))
        f.write(struct.pack("<I",   0))                   # fourCC (uncompressed)
        f.write(struct.pack("<I",   32))                  # bits per pixel
        f.write(struct.pack("<I",   0x00FF0000))          # R mask
        f.write(struct.pack("<I",   0x0000FF00))          # G mask
        f.write(struct.pack("<I",   0x000000FF))          # B mask
        f.write(struct.pack("<I",   0xFF000000))          # A mask
        # caps
        f.write(struct.pack("<I",   DDSCAPS_TEXTURE))
        f.write(struct.pack("<4I",  0, 0, 0, 0))
        # pixel data — DDS expects BGRA byte order
        f.write(img.tobytes("raw", "BGRA"))

# ─── API call (identical pattern to generate_ai_portraits.py) ────────────────

def call_imagen(prompt: str, api_key: str) -> bytes:
    payload = json.dumps({
        "instances":  [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "4:3",   # 1920x1440 = 4:3
        },
    }).encode()
    req = urllib.request.Request(
        f"{IMAGEN_URL}?key={api_key}",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    b64 = data["predictions"][0]["bytesBase64Encoded"]
    return base64.b64decode(b64)

# ─── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate SPQR loading screen DDS images via Google Imagen 4"
    )
    parser.add_argument("--overwrite", action="store_true",
                        help="Re-generate even if DDS already exists")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print prompts and paths without calling the API")
    args = parser.parse_args()

    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key and not args.dry_run:
        print("ERROR: export GOOGLE_API_KEY=<your key> before running.")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)

    total = len(SCREENS)
    done  = 0

    print(f"Generating {total} loading screens via Imagen 4...\n")

    for idx, (name, prompt) in enumerate(SCREENS, 1):
        full_dds  = OUT_DIR / f"{name}.dds"
        small_dds = OUT_DIR / f"{name}_small.dds"
        png_path  = PNG_DIR / f"{name}.png"

        print(f"[{idx}/{total}] {name}")

        if args.dry_run:
            print(f"  -> {full_dds.relative_to(MOD)}")
            print(f"  PROMPT: {prompt[:120]}...\n")
            done += 1
            continue

        if full_dds.exists() and small_dds.exists() and not args.overwrite:
            print(f"  SKIP (exists) — use --overwrite to regenerate\n")
            done += 1
            continue

        try:
            img_bytes = call_imagen(prompt, api_key)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode(errors="replace")
            print(f"  HTTP {exc.code} ERROR: {body}\n")
            continue
        except Exception as exc:
            print(f"  ERROR: {exc}\n")
            continue

        img = Image.open(BytesIO(img_bytes))

        # PNG backup
        img.save(png_path)

        # Full-size DDS (1920x1440)
        full_img = img.resize((FULL_W, FULL_H), Image.LANCZOS)
        write_dds(full_dds, full_img)

        # Thumbnail DDS (192x144)
        small_img = img.resize((SMALL_W, SMALL_H), Image.LANCZOS)
        write_dds(small_dds, small_img)

        kb = full_dds.stat().st_size // 1024
        print(f"  -> {name}.dds ({kb} KB)  +  {name}_small.dds  +  png backup")
        done += 1

        if idx < total:
            time.sleep(REQUEST_DELAY)

    print(f"\nDone. {done}/{total} screens generated.")
    if done == total:
        print(
            "\nNext step: remove the vanilla fallback lines (load_1..load_5) from\n"
            "  common/frontend/backgrounds/spqr_backgrounds.txt"
        )


if __name__ == "__main__":
    main()
