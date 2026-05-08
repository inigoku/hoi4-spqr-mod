#!/usr/bin/env python3
"""
Generate HoI4 leader portraits using Google Imagen 4.

Portraits are saved as 156x210 TGA files under gfx/leaders/{TAG}/.
Each country leader, field marshal, and general gets their own portrait.

Requirements:
    pip install Pillow

Usage:
    export GOOGLE_API_KEY=your_key_here
    python3 generate_ai_portraits.py
    python3 generate_ai_portraits.py --tag SPQ
    python3 generate_ai_portraits.py --overwrite
    python3 generate_ai_portraits.py --dry-run
    python3 generate_ai_portraits.py --update-history
"""

import argparse
import base64
import json
import os
import re
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

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
MOD_DIR = SCRIPT_DIR.parent
GFX_DIR = MOD_DIR / "gfx" / "leaders"
HISTORY_DIR = MOD_DIR / "history" / "countries"

# ---------------------------------------------------------------------------
# Portrait dimensions (HoI4 standard)
# ---------------------------------------------------------------------------
WIDTH, HEIGHT = 156, 210

# ---------------------------------------------------------------------------
# Imagen 4 endpoint
# ---------------------------------------------------------------------------
IMAGEN_URL = (
    "https://generativelanguage.googleapis.com/v1beta"
    "/models/imagen-4.0-generate-001:predict"
)
REQUEST_DELAY = 3.0  # seconds between API calls

# ---------------------------------------------------------------------------
# Art-style suffix appended to every prompt
# ---------------------------------------------------------------------------
STYLE = (
    "ancient Roman mosaic fresco style, small colourful tesserae squares, "
    "wall painting on plaster, muted terracotta and ochre palette, "
    "264 BC Punic Wars era, serious formal portrait, "
    "head-and-shoulders composition, centred face, no text or lettering"
)

# ---------------------------------------------------------------------------
# Leader data  (names from localisation/english/spqr_countries_l_english.yml)
# ---------------------------------------------------------------------------
LEADERS = [
    # ── SPQ : Rome ──────────────────────────────────────────────────────────
    dict(tag="SPQ", role="country_leader",
         name="Appius Claudius Caudex",
         file="Portrait_Appius_Claudius.tga",
         country="Roman Republic",
         desc="Marble voice of the Senate and sword of Rome: his rule promises "
              "order, conquest, and everlasting glory for the Republic."),
    dict(tag="SPQ", role="field_marshal",
         name="Publius Cornelius Scipio",
         file="Portrait_Scipio.tga",
         country="Roman Republic",
         desc="Consul and Roman field commander, father of Scipio Africanus, "
              "leading the legions of Rome into Sicily."),
    dict(tag="SPQ", role="general",
         name="Quintus Fabius Maximus",
         file="Portrait_Fabius.tga",
         country="Roman Republic",
         desc="Cautious Roman strategist, the Delayer, master of attritional "
              "warfare and patient defender of the Republic."),

    # ── CRG : Carthage ──────────────────────────────────────────────────────
    dict(tag="CRG", role="country_leader",
         name="Hanno II",
         file="Portrait_Hanno.tga",
         country="Carthage",
         desc="Suffete of Carthage and master of the Punic sea: his seal opens "
              "golden routes and his fleet closes them to rivals."),
    dict(tag="CRG", role="field_marshal",
         name="Hannibal Barca",
         file="Portrait_Hannibal.tga",
         country="Carthage",
         desc="Brilliant Carthaginian general, son of Hamilcar, destined to "
              "lead the greatest Punic army across the Alps."),
    dict(tag="CRG", role="general",
         name="Hasdrubal Barca",
         file="Portrait_Hasdrubal.tga",
         country="Carthage",
         desc="Punic general and brother of Hannibal, commander of Carthaginian "
              "forces in Iberia and guardian of the western empire."),

    # ── MCD : Macedonia ─────────────────────────────────────────────────────
    dict(tag="MCD", role="country_leader",
         name="Antigonus II Gonatas",
         file="Portrait_Antigonus.tga",
         country="Macedonia",
         desc="Basileus of Macedon and hammer of the Balkans: born to command "
              "courts, forged to decide wars."),
    dict(tag="MCD", role="field_marshal",
         name="Demetrius II",
         file="Portrait_Demetrius.tga",
         country="Macedonia",
         desc="Macedonian prince and successor, commanding the Macedonian "
              "phalanx with the authority of Alexander's legacy."),
    dict(tag="MCD", role="general",
         name="Philippus V",
         file="Portrait_Philippus.tga",
         country="Macedonia",
         desc="Future king of Macedon, young prince being trained in the "
              "Macedonian martial tradition of the Antigonid dynasty."),

    # ── KMT : Ptolemaic Egypt ────────────────────────────────────────────────
    dict(tag="KMT", role="country_leader",
         name="Ptolemy II Philadelphus",
         file="Portrait_Ptolemy.tga",
         country="Ptolemaic Egypt",
         desc="Pharaoh of Alexandria, lord of the Nile and libraries alike: "
              "his crown fuses wisdom, wealth, and imperial ambition."),
    dict(tag="KMT", role="field_marshal",
         name="Patroclus",
         file="Portrait_Patroclus.tga",
         country="Ptolemaic Egypt",
         desc="Ptolemaic admiral and strategos commanding Egypt's forces in "
              "the Aegean and Syrian campaigns."),
    dict(tag="KMT", role="general",
         name="Scopas",
         file="Portrait_Scopas.tga",
         country="Ptolemaic Egypt",
         desc="Greek mercenary general in Ptolemaic service, veteran of the "
              "eastern Mediterranean wars of the Hellenistic kingdoms."),

    # ── SEL : Seleucid Empire ────────────────────────────────────────────────
    dict(tag="SEL", role="country_leader",
         name="Antiochus II Theos",
         file="Portrait_Antiochus.tga",
         country="Seleucid Empire",
         desc="Seleucid great king, master of satrapies and caravan roads: "
              "his scepter holds a vast empire against the pull of fracture."),
    dict(tag="SEL", role="field_marshal",
         name="Zeuxis",
         file="Portrait_Zeuxis.tga",
         country="Seleucid Empire",
         desc="Seleucid viceroy and general commanding the armies of Asia "
              "Minor and the western satrapies."),
    dict(tag="SEL", role="general",
         name="Molon",
         file="Portrait_Molon.tga",
         country="Seleucid Empire",
         desc="Satrap of Media and capable Seleucid general, one of the most "
              "dangerous commanders in the eastern empire."),

    # ── SYC : Syracuse ──────────────────────────────────────────────────────
    dict(tag="SYC", role="country_leader",
         name="Hiero II",
         file="Portrait_Hiero.tga",
         country="Syracuse",
         desc="Throne of Syracuse and beacon of Sicily: his will turns harbors "
              "into bastions and diplomacy into dominion."),
    dict(tag="SYC", role="field_marshal",
         name="Gelon II",
         file="Portrait_Gelon.tga",
         country="Syracuse",
         desc="Son of Hiero II and crown prince of Syracuse, commander of "
              "Syracusan forces in the defence of Sicily."),
    dict(tag="SYC", role="general",
         name="Epicydes",
         file="Portrait_Epicydes.tga",
         country="Syracuse",
         desc="Syracusan general of Carthaginian descent, defender of the "
              "city during the great Roman siege."),

    # ── GRC : Achaean League ─────────────────────────────────────────────────
    dict(tag="GRC", role="country_leader",
         name="Margos of Keryneia",
         file="Portrait_Margos.tga",
         country="Achaean League",
         desc="Tribune of western Hellas: he summons rival poleis toward one "
              "destiny with burning rhetoric and iron discipline."),
    dict(tag="GRC", role="field_marshal",
         name="Aratus of Sicyon",
         file="Portrait_Aratus.tga",
         country="Achaean League",
         desc="Greek statesman and strategos who united the Peloponnesian "
              "poleis under the Achaean League banner."),
    dict(tag="GRC", role="general",
         name="Philopoemen",
         file="Portrait_Philopoemen.tga",
         country="Achaean League",
         desc="The Last of the Greeks, greatest Achaean general, reformer "
              "of the phalanx and defender of Hellenic freedom."),

    # ── LAC : Sparta ─────────────────────────────────────────────────────────
    dict(tag="LAC", role="country_leader",
         name="Acrotatus II",
         file="Portrait_Acrotatus.tga",
         country="Sparta",
         desc="King of Sparta, guardian of the agoge: every order beats with "
              "the pulse of ancient Lacedaemonian pride."),
    dict(tag="LAC", role="field_marshal",
         name="Cleomenes III",
         file="Portrait_Cleomenes.tga",
         country="Sparta",
         desc="Spartan king and reformer who sought to restore the Lycurgan "
              "constitution and renew Spartan martial glory."),
    dict(tag="LAC", role="general",
         name="Agis IV",
         file="Portrait_Agis.tga",
         country="Sparta",
         desc="Young Spartan king who attempted radical social reform to "
              "rebuild the Spartan warrior citizen army."),

    # ── SMN : Samnium ────────────────────────────────────────────────────────
    dict(tag="SMN", role="country_leader",
         name="Gellius Egnatius",
         file="Portrait_Egnatius.tga",
         country="Samnium",
         desc="Lord of Samnite strongholds: his name echoes through the "
              "valleys as a vow of ruthless endurance."),
    dict(tag="SMN", role="field_marshal",
         name="Pontius Telesinus",
         file="Portrait_Pontius.tga",
         country="Samnium",
         desc="Samnite general of fierce reputation, last great champion of "
              "Samnite independence against Roman expansion."),
    dict(tag="SMN", role="general",
         name="Gavius Pontius",
         file="Portrait_Gavius.tga",
         country="Samnium",
         desc="Samnite mountain warrior and son of the great Pontius who "
              "humiliated Rome at the Caudine Forks."),

    # ── PHN : Mauretania ─────────────────────────────────────────────────────
    dict(tag="PHN", role="country_leader",
         name="Baga",
         file="Portrait_Baga.tga",
         country="Mauretania",
         desc="Mauretanian lord of the ocean frontier: he binds clans, "
              "fortifies ports, and raises a kingdom from the edge."),
    dict(tag="PHN", role="field_marshal",
         name="Bocchus I",
         file="Portrait_Bocchus.tga",
         country="Mauretania",
         desc="Mauretanian king commanding the nomadic Berber cavalry of "
              "the North African Atlantic coast."),
    dict(tag="PHN", role="general",
         name="Bogud",
         file="Portrait_Bogud.tga",
         country="Mauretania",
         desc="Berber war leader commanding the swift desert horsemen and "
              "tribal warriors of Mauretanian clans."),

    # ── IBR : Iberia ─────────────────────────────────────────────────────────
    dict(tag="IBR", role="country_leader",
         name="Indibilis",
         file="Portrait_Indibilis.tga",
         country="Iberia",
         desc="Warlord of untamed Iberia: his prestige gathers scattered "
              "tribes into a single fighting will."),
    dict(tag="IBR", role="field_marshal",
         name="Mandonius",
         file="Portrait_Mandonius.tga",
         country="Iberia",
         desc="Iberian chieftain, brother of Indibilis and co-commander of "
              "the fierce Ilergetes warriors of Hispania."),
    dict(tag="IBR", role="general",
         name="Istolatius",
         file="Portrait_Istolatius.tga",
         country="Iberia",
         desc="Iberian tribal captain commanding the light javelin skirmishers "
              "and cavalry of the Celtiberian highlands."),

    # ── GLN : Gauls / Massalia ───────────────────────────────────────────────
    dict(tag="GLN", role="country_leader",
         name="Aristarchos of Massalia",
         file="Portrait_Aristarchos.tga",
         country="Massalia",
         desc="Archon of Massalia: a merchant in peace, a fierce strategist "
              "whenever the coast demands steel."),
    dict(tag="GLN", role="field_marshal",
         name="Euthymenes",
         file="Portrait_Euthymenes.tga",
         country="Massalia",
         desc="Massalian navigator and general commanding the Greek colony's "
              "forces on the Gallic coast."),
    dict(tag="GLN", role="general",
         name="Protis",
         file="Portrait_Protis.tga",
         country="Massalia",
         desc="Greek Massalian commander leading the mixed Greek and Gallic "
              "forces defending the colony's hinterland."),

    # ── ILL : Illyria ─────────────────────────────────────────────────────────
    dict(tag="ILL", role="country_leader",
         name="Pleuratus II",
         file="Portrait_Pleuratus.tga",
         country="Illyria",
         desc="Illyrian king of the Adriatic: his ships arrive like storms, "
              "and his banner turns ports into oaths."),
    dict(tag="ILL", role="field_marshal",
         name="Agron",
         file="Portrait_Agron.tga",
         country="Illyria",
         desc="King of the Ardiaei Illyrians, builder of the first Illyrian "
              "naval power dominating the Adriatic Sea."),
    dict(tag="ILL", role="general",
         name="Scerdilaidas",
         file="Portrait_Scerdilaidas.tga",
         country="Illyria",
         desc="Illyrian prince and admiral commanding the swift lembi warships "
              "raiding the coasts of Greece and Macedonia."),

    # ── THR : Thrace ─────────────────────────────────────────────────────────
    dict(tag="THR", role="country_leader",
         name="Cotys I of Thrace",
         file="Portrait_Cotys.tga",
         country="Thrace",
         desc="Odrysian monarch of hard-riding warriors: on the frontier of "
              "empires, his crown endures through daring and cold resolve."),
    dict(tag="THR", role="field_marshal",
         name="Seuthes III",
         file="Portrait_Seuthes.tga",
         country="Thrace",
         desc="Odrysian Thracian king who rebuilt Thracian power, founder of "
              "Seuthopolis, commanding fierce Thracian cavalry."),
    dict(tag="THR", role="general",
         name="Rhoemetalces",
         file="Portrait_Rhoemetalces.tga",
         country="Thrace",
         desc="Thracian prince commanding the swift horse archers and peltasts "
              "of the Pontic steppe borderlands."),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def build_prompt(leader: dict) -> str:
    role_label = {
        "country_leader": "ruler",
        "field_marshal":  "field marshal",
        "general":        "general",
    }.get(leader["role"], leader["role"])
    return (
        f"Portrait of {leader['name']}, {role_label} of {leader['country']} "
        f"circa 264 BC. {leader['desc']} Style: {STYLE}."
    )


def call_imagen(prompt: str, api_key: str) -> bytes:
    payload = json.dumps({
        "instances":  [{"prompt": prompt}],
        "parameters": {"sampleCount": 1},
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


def save_tga(img_bytes: bytes, out_path: Path) -> None:
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(out_path), format="TGA")


def portrait_path(leader: dict) -> Path:
    return GFX_DIR / leader["tag"] / leader["file"]


# ---------------------------------------------------------------------------
# History-file updater
# ---------------------------------------------------------------------------

def update_history_files(leaders: list[dict], dry_run: bool) -> None:
    """
    Patch history/countries files so each leader's `portrait` key points to
    the newly generated TGA file.  Matches on the leader name inside the
    country_leader / field_marshal / corps_commander block.
    """
    # Build a map: tag -> { name -> new_portrait_path }
    by_tag: dict[str, dict[str, str]] = {}
    for ldr in leaders:
        tag = ldr["tag"]
        rel = f"gfx/leaders/{tag}/{ldr['file']}"
        by_tag.setdefault(tag, {})[ldr["name"]] = rel

    for hist_file in sorted(HISTORY_DIR.glob("*.txt")):
        # Extract tag from filename like "CRG - Carthage.txt"
        m = re.match(r"^([A-Z]{2,3})\s+-", hist_file.name)
        if not m:
            continue
        tag = m.group(1)
        if tag not in by_tag:
            continue

        text = hist_file.read_text(encoding="utf-8")
        changed = False

        for name, rel_path in by_tag[tag].items():
            # Replace portrait line inside the block that contains this name.
            # Strategy: find blocks that contain `name = "NAME"` and update
            # the adjacent `portrait =` line within the same brace scope.
            pattern = re.compile(
                r'(name\s*=\s*"' + re.escape(name) + r'"[^}]*?)'
                r'(portrait\s*=\s*"[^"]*")',
                re.DOTALL,
            )
            replacement = r'\1portrait = "' + rel_path + '"'
            new_text, n = pattern.subn(replacement, text)
            if n:
                text = new_text
                changed = True
                print(f"  [{tag}] {name} -> {rel_path}")

        if changed:
            if dry_run:
                print(f"  (dry-run) would write {hist_file.name}")
            else:
                hist_file.write_text(text, encoding="utf-8")
                print(f"  Wrote {hist_file.name}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate HoI4 ancient leader portraits via Google Imagen 4"
    )
    parser.add_argument("--tag", help="Only process this country tag, e.g. SPQ")
    parser.add_argument("--overwrite", action="store_true",
                        help="Re-generate even if TGA already exists")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print prompts and paths without calling the API")
    parser.add_argument("--update-history", action="store_true",
                        help="Also patch history/countries/*.txt portrait paths")
    args = parser.parse_args()

    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key and not args.dry_run:
        print("ERROR: export GOOGLE_API_KEY=<your key> before running.")
        sys.exit(1)

    leaders = LEADERS
    if args.tag:
        leaders = [l for l in leaders if l["tag"] == args.tag.upper()]
        if not leaders:
            print(f"No leaders found for tag '{args.tag}'")
            sys.exit(1)

    total = len(leaders)
    generated = []

    for i, ldr in enumerate(leaders, 1):
        out = portrait_path(ldr)
        prompt = build_prompt(ldr)
        role_label = ldr["role"].replace("_", " ")
        print(f"[{i}/{total}] {ldr['tag']} {role_label}: {ldr['name']}")

        if args.dry_run:
            print(f"  -> {out.relative_to(MOD_DIR)}")
            print(f"  PROMPT: {prompt}\n")
            generated.append(ldr)
            continue

        if out.exists() and not args.overwrite:
            print(f"  SKIP (exists) {out.relative_to(MOD_DIR)}")
            generated.append(ldr)
            continue

        try:
            img_bytes = call_imagen(prompt, api_key)
            save_tga(img_bytes, out)
            print(f"  Saved {WIDTH}x{HEIGHT} TGA -> {out.relative_to(MOD_DIR)}")
            generated.append(ldr)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode(errors="replace")
            print(f"  HTTP {exc.code} ERROR: {body}")
        except Exception as exc:
            print(f"  ERROR: {exc}")

        if i < total:
            time.sleep(REQUEST_DELAY)

    if args.update_history and generated:
        print("\nUpdating history files …")
        update_history_files(generated, dry_run=args.dry_run)

    print(f"\nDone. {len(generated)}/{total} portraits processed.")


if __name__ == "__main__":
    main()
