#!/usr/bin/env python3
"""
generate_loading_screens.py
Generates loading screen DDS images for the SPQR mod using Google Imagen 4.
Uses the same API as generate_ai_portraits.py.

Requirements:
    pip install Pillow

Usage:
    export GOOGLE_API_KEY="your_api_key_here"
    python3 tools/generate_loading_screens.py
    python3 tools/generate_loading_screens.py --overwrite   # re-generate existing
    python3 tools/generate_loading_screens.py --dry-run     # print prompts only
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

MOD     = Path(__file__).resolve().parent.parent
OUT_DIR = MOD / "gfx" / "loadingscreens"
PNG_DIR = OUT_DIR / "png"

FULL_W,  FULL_H  = 1920, 1440
SMALL_W, SMALL_H = 192,  144

IMAGEN_URL = (
    "https://generativelanguage.googleapis.com/v1beta"
    "/models/imagen-4.0-generate-001:predict"
)
REQUEST_DELAY = 3.0

STYLE = (
    "epic historical painting style, cinematic wide composition, "
    "rich dramatic lighting, highly detailed ancient Mediterranean world, "
    "264 BC Punic Wars era, oil painting on canvas, no text or lettering"
)

SCREENS = [
    # Base SPQR Backgrounds (registered in backgrounds.txt)
    ("load_spqr_1", "Hannibal Barca's war elephants crossing the snow-covered Alps in winter, Carthaginian soldiers and horses struggling through icy mountain passes, towering peaks draped in snow, storm clouds gathering, desperate and heroic atmosphere, wide panoramic landscape view. " + STYLE),
    ("load_spqr_2", "Ancient Roman quinqueremes and Carthaginian warships in massive naval battle during the First Punic War, bright Mediterranean sea, bronze rams splintering enemy hulls, marines fighting on deck, burning ships listing in the water, dramatic golden afternoon light. " + STYLE),
    ("load_spqr_3", "Battle of Cannae 216 BC, Hannibal's Carthaginian cavalry and infantry encircling Roman legions in a devastating double envelopment, wide aerial view of the Italian plain battlefield, dust clouds rising over thousands of soldiers, chaos and desperation. " + STYLE),
    ("load_spqr_4", "Ancient Roman legions and war galleys crossing the Strait of Messina to Sicily at dawn, troop transports escorted by quinqueremes, golden first light shimmering on the water, Mount Etna visible in the distance, majestic and epic beginning of the First Punic War. " + STYLE),
    ("load_spqr_5", "Battle of Zama 202 BC, Scipio Africanus commanding Roman legions against Hannibal's war elephants in the North African desert, elephants charging toward Roman lines while soldiers open lanes to let the great beasts through, heat and dust, decisive moment of ancient history. " + STYLE),
    ("load_spqr_6", "Battle of Ecnomus 256 BC, hundreds of Roman and Carthaginian warships clashing across the Mediterranean Sea in the largest naval battle of antiquity, Roman ships in wedge formation breaking the Carthaginian line, smoke, fire, and carnage on a breathtaking scale. " + STYLE),
    ("load_spqr_7", "Siege of Syracuse, Archimedes' giant iron claw war machines lifting Roman warships out of the harbour and dropping them into the sea, Greek city of Syracuse on Sicilian cliffs in the background, Roman fleet in disarray, sunset light over the ancient wonder of engineering. " + STYLE),
    ("load_spqr_8", "Hannibal Barca leading Carthaginian war elephants across the wide Rhone river on makeshift rafts, terrified elephants in the water, Gallic warriors watching from the far bank, autumn forest colours, river mist, dramatic and tense ancient river crossing. " + STYLE),
    ("load_spqr_9", "Macedonian phalanx in perfect battle formation, thousands of soldiers levelling their long sarissa spears in unison, mountain valley landscape of ancient Macedonia, golden armour and bronze shields gleaming in afternoon sunlight, dust rising from their advance. " + STYLE),
    ("load_spqr_10", "Battle of Raphia 217 BC, Ptolemaic Egyptian and Seleucid war elephants clashing in fierce combat, African forest elephants against Indian war elephants, desert landscape of the Sinai, thousands of soldiers fighting around the great beasts, dust and fury. " + STYLE),
    ("load_spqr_11", "Ancient harbour of Carthage at golden sunset, the circular Cothon military harbour with Phoenician warships arranged in perfect order, merchant vessels in the outer harbour, the great city rising on the hill, North African coast glowing in warm Mediterranean light. " + STYLE),
    ("load_spqr_12", "Greek trireme fleet sailing at dawn through the Aegean Sea past rocky islands, classical Greek warships with bronze rams and painted eyes on the prows, morning mist rising off the water, oarsmen pulling in perfect rhythm, beautiful and serene ancient seascape. " + STYLE),
    ("load_spqr_13", "Battle of Heraclea 280 BC, Pyrrhus of Epirus leading towering war elephants against Roman legions in the green hills of southern Italy, Roman soldiers breaking formation in terror before the great beasts, Epirote and Greek infantry following behind, dramatic ancient battle. " + STYLE),
    ("load_spqr_14", "Roman legionaries constructing a fortified military castra camp at dusk, perfectly organised square earthwork with rows of tents inside, soldiers digging ditches and raising palisades with methodical precision, campfires being lit, Italian countryside bathed in golden hour light. " + STYLE),
    ("load_spqr_15", "The great Lighthouse of Alexandria blazing with fire at night over the harbour, Ptolemaic warships and merchant vessels filling the water below, magnificent city of Alexandria glowing on the Egyptian coast, moonlit Mediterranean sea, the most spectacular wonder of the ancient world. " + STYLE),

    # Vanilla Replacements (1-20)
    ("load_1", "Gallic tribal warriors preparing for an ambush in a dense European forest, bronze shields, iron swords, dramatic dappled sunlight through the trees. " + STYLE),
    ("load_2", "Iberian hillfort under siege, Celtic and Iberian warriors defending steep stone walls against an approaching enemy host, dramatic stormy sky. " + STYLE),
    ("load_3", "Ptolemaic pharaoh riding in a golden chariot past the Pyramids of Giza, thousands of Egyptian spearmen marching in procession, vast desert sands. " + STYLE),
    ("load_4", "Seleucid cataphracts marching across the Syrian plains, heavily armoured horsemen in shining scale mail with long lances, dust blowing in the wind. " + STYLE),
    ("load_5", "Spartan hoplites standing resolute at a mountain pass, crimson cloaks billowing in the wind, bronze Corinthian helmets gleaming, stoic defenders. " + STYLE),
    ("load_6", "A grand Roman triumph marching through the streets of Rome, general in a chariot pulled by four white horses, cheering crowds, ancient temples. " + STYLE),
    ("load_7", "Numidian light cavalry skirmishing in the vast Sahara desert, riders throwing javelins from horseback at full gallop, beautiful shifting sand dunes. " + STYLE),
    ("load_8", "A fierce naval boarding action between a Roman corvus and a Carthaginian quinquereme, soldiers fighting desperately on the gangplank over dark waters. " + STYLE),
    ("load_9", "Ancient Greek philosophers and generals planning strategy around a large map table in a marble temple, statues of gods looking down, incense burning. " + STYLE),
    ("load_10", "Samnite warriors making a desperate last stand in the Apennine mountains, rocky terrain, bronze armor and plumed helmets, heroic defense. " + STYLE),
    ("load_11", "Illyrian pirates launching a surprise attack on a merchant convoy from hidden coastal coves, fast lembi ships cutting through the water. " + STYLE),
    ("load_12", "A grand sacrifice to Jupiter before a Roman military campaign, augurs reading omens, smoke rising from marble altars, columns and eagles. " + STYLE),
    ("load_13", "Carthaginian Sacred Band marching into battle, elite infantry in white armor with large round shields and long spears, disciplined and terrifying. " + STYLE),
    ("load_14", "Thracian peltasts throwing javelins from a wooded hillside, crescent shields, fox-skin caps, swift and deadly skirmishers. " + STYLE),
    ("load_15", "A massive siege tower rolling towards a Hellenistic city wall, battering rams pounding the gates, defenders pouring boiling oil from above. " + STYLE),
    ("load_16", "Roman testudo formation advancing slowly through a hail of arrows and sling stones, overlapping shields creating an impenetrable shell. " + STYLE),
    ("load_17", "A fierce winter battle in the Alps, tribal ambushes, soldiers slipping in the snow, dramatic blizzard conditions and heroic struggles. " + STYLE),
    ("load_18", "The ancient city of Syracuse at dawn, grand walls, the Temple of Athena, and the great harbor protected by massive chains and artillery. " + STYLE),
    ("load_19", "A diplomatic meeting between a Roman consul and an eastern King in a magnificent tent, gold and purple silks, guards standing watch. " + STYLE),
    ("load_20", "Nighttime stealth attack, soldiers climbing ladders over an ancient city wall in the dark, moonlight illuminating the bronze of their weapons. " + STYLE),

    # DLC Replacements
    ("load_tfv", "Together for Victory: Allied ancient nations marching together, Greek and Roman banners side by side against a common threat. " + STYLE),
    ("load_dod", "Death or Dishonor: A defeated king surrendering his sword to a Roman general amidst the ruins of a burning city. " + STYLE),
    ("load_tiger", "Waking the Tiger: Eastern empires awakening, a massive army of Parthian or Seleucid soldiers marching out from a grand desert city. " + STYLE),
    ("load_wtt", "Waking the Tiger alt: A grand battle in the ancient Near East, towering elephants and chariots clashing under a blazing sun. " + STYLE),
    ("load_mtg", "Man the Guns: Massive ancient shipyards constructing dozens of quinqueremes, wooden ribs of ships, workers and engineers swarming the docks. " + STYLE),
    ("load_mtg_2", "Man the Guns 2: A terrifying naval storm, an ancient fleet struggling against colossal waves, oars shattering, lightning striking the sea. " + STYLE),
    ("load_mtg2", "Man the Guns 3: A naval blockade of an ancient port city, countless ships forming an impenetrable wall on the water. " + STYLE),
    ("load_lar", "La Resistance: Ancient spies and assassins in cloaks plotting in a dimly lit Roman tavern, secret scrolls and daggers on the table. " + STYLE),
    ("load_botb", "Battle for the Bosporus: The magnificent ancient walls of Byzantium or Troy, standing strong along the strait, massive fleets passing by. " + STYLE),
    ("load_nsb", "No Step Back: A brutal and muddy trench warfare in a siege camp, legionaries holding the line in driving rain. " + STYLE),
    ("load_nsb2", "No Step Back 2: A logistical train of thousands of mules and wagons carrying grain to a massive ancient army camp. " + STYLE),
    ("load_bba", "By Blood Alone: An intense gladiatorial combat in a large ancient arena, sand stained with blood, cheering crowds above. " + STYLE),
    ("load_aat", "Arms Against Tyranny: A massive slave revolt breaking out, gladiators and peasants raising crude weapons against armored guards. " + STYLE),
    ("load_aat2", "Arms Against Tyranny 2: A heroic stand of an outnumbered garrison defending a narrow city gate against an invading horde. " + STYLE),
    ("load_toa", "Trial of Allegiance: A dramatic betrayal on the battlefield, allied cavalry turning their spears against their own commanders. " + STYLE),
    ("load_ww", "Wunderwaffe/Secret Weapons: Archimedes' heat ray focusing sunlight to burn enemy ships in the harbor, brilliant and terrifying ancient science. " + STYLE),
    ("load_goe", "Gotterdammerung: The apocalyptic burning of an ancient metropolis, massive columns collapsing, absolute destruction and end of an empire. " + STYLE),
    ("load_got", "Gotterdammerung alt: A desperate final charge of the last remaining defenders out from a besieged citadel into a sea of enemies. " + STYLE),
]

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
        f.write(struct.pack("<I",   w * 4))
        f.write(struct.pack("<I",   0))
        f.write(struct.pack("<I",   0))
        f.write(struct.pack("<11I", *([0] * 11)))
        f.write(struct.pack("<I",   32))
        f.write(struct.pack("<I",   DDPF_ALPHAPIXELS | DDPF_RGB))
        f.write(struct.pack("<I",   0))
        f.write(struct.pack("<I",   32))
        f.write(struct.pack("<I",   0x00FF0000))
        f.write(struct.pack("<I",   0x0000FF00))
        f.write(struct.pack("<I",   0x000000FF))
        f.write(struct.pack("<I",   0xFF000000))
        f.write(struct.pack("<I",   DDSCAPS_TEXTURE))
        f.write(struct.pack("<4I",  0, 0, 0, 0))
        f.write(img.tobytes("raw", "BGRA"))

def call_imagen(prompt: str, api_key: str) -> bytes:
    payload = json.dumps({
        "instances":  [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "4:3",
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
        
    if "predictions" not in data:
        raise ValueError(f"API response missing 'predictions' (likely safety blocked). Response: {json.dumps(data)}")
        
    b64 = data["predictions"][0]["bytesBase64Encoded"]
    return base64.b64decode(b64)

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
        img.save(png_path)
        full_img = img.resize((FULL_W, FULL_H), Image.LANCZOS)
        write_dds(full_dds, full_img)
        small_img = img.resize((SMALL_W, SMALL_H), Image.LANCZOS)
        write_dds(small_dds, small_img)

        kb = full_dds.stat().st_size // 1024
        print(f"  -> {name}.dds ({kb} KB)  +  {name}_small.dds  +  png backup\n")
        done += 1

        if idx < total:
            time.sleep(REQUEST_DELAY)

    print(f"\nDone. {done}/{total} screens generated.")

if __name__ == "__main__":
    main()