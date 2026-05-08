#!/usr/bin/env python3
"""
generate_flags.py
Generates uncompressed TGA flags (82×52, 41×26, 10×7) for all SPQR mod nations
and updates common/countries/ color definitions to match.
SPQ (Rome) is intentionally skipped — its proper flag already exists.
"""
import struct, os, re

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─────────────────────────────────────────────────────────────────────────────
# TGA writer  (Type 2 — uncompressed 24-bit true-color, top-left origin)
# ─────────────────────────────────────────────────────────────────────────────
def write_tga(path, width, height, pixels):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(struct.pack('<BBBHHBHHHHBB',
            0, 0, 2,            # no id, no colormap, uncompressed truecolor
            0, 0, 0,            # colormap spec (none)
            0, 0,               # origin x, y
            width, height,
            24, 0x20            # 24-bit, top-left origin
        ))
        for r, g, b in pixels:
            f.write(struct.pack('BBB', b, g, r))   # TGA uses BGR order

def render(fn, w, h):
    return [fn(x, y, w, h) for y in range(h) for x in range(w)]

# ─────────────────────────────────────────────────────────────────────────────
# Design helpers
# ─────────────────────────────────────────────────────────────────────────────
def triband(ca, cb):
    """Horizontal triband: ca / cb / ca"""
    def f(x, y, w, h):
        t = y / h
        return cb if 0.33 <= t < 0.67 else ca
    return f

def bicolor_h(ca, cb):
    """Top half ca, bottom half cb"""
    def f(x, y, w, h):
        return ca if y < h / 2 else cb
    return f

def diagonal(ca, cb):
    """Top-left triangle ca, bottom-right triangle cb"""
    def f(x, y, w, h):
        return ca if (x / w + y / h) < 1.0 else cb
    return f

# ─────────────────────────────────────────────────────────────────────────────
# Nation table
# (tag, design_fn, map_rgb)
# map_rgb drives both the flag's dominant colour and the in-game map colour.
# Every colour is unique; colours are chosen to be visually distinct on the map.
# ─────────────────────────────────────────────────────────────────────────────
NATIONS = [
    # Tag   Design                                    Map RGB
    ("CRG", triband((110, 20,130), (210,170, 50)),  (110, 20,130)),  # Carthage   — Punic purple / gold
    ("MCD", triband(( 30, 60,175), (210,170, 50)),  ( 30, 60,175)),  # Macedonia  — royal blue / gold
    ("KMT", triband((205,165, 40), ( 40,100,180)),  (205,165, 40)),  # Egypt      — pharaoh gold / Nile blue
    ("SEL", triband(( 20,130,185), (230,230,230)),  ( 20,130,185)),  # Seleucid   — cyan-steel / white
    ("SYC", triband((195, 55, 35), (240,240,240)),  (195, 55, 35)),  # Syracuse   — deep red / white
    ("GRC", triband(( 75,150,205), (240,240,240)),  ( 75,150,205)),  # Achaean    — Aegean blue / white
    ("LAC", bicolor_h((145, 20, 55), ( 20, 20, 20)), (145, 20, 55)), # Sparta     — crimson / black
    ("SMN", triband(( 90,145, 40), (175,115, 35)),  ( 90,145, 40)),  # Samnites   — olive / earth brown
    ("PHN", triband((155, 50,200), (210,170, 50)),  (155, 50,200)),  # Mauretania — violet / gold
    ("IBR", triband((195, 90, 20), (240,200, 25)),  (195, 90, 20)),  # Iberia     — burnt orange / amber
    ("GLN", triband(( 25,135, 50), (210,170, 50)),  ( 25,135, 50)),  # Gauls      — forest green / gold
    ("ILL", diagonal(( 45,185,140), (240,240,240)), ( 45,185,140)),  # Illyria    — teal / white
    ("THR", bicolor_h((165,135, 25), (100, 60, 20)), (165,135, 25)), # Thrace     — dark gold / brown
    ("WLD", triband(( 80, 80, 80), ( 55, 55, 55)),  ( 80, 80, 80)),  # Wasteland  — slate grey
]

SIZES = [
    ("",        82, 52),   # main flag
    ("medium/", 41, 26),   # medium flag
    ("small/",  10,  7),   # small flag
]

# ─────────────────────────────────────────────────────────────────────────────
# Generate flag TGAs
# ─────────────────────────────────────────────────────────────────────────────
flags_root = os.path.join(MOD, "gfx", "flags")

for tag, design, _ in NATIONS:
    pixels_cache = {}
    for subdir, w, h in SIZES:
        if (w, h) not in pixels_cache:
            pixels_cache[(w, h)] = render(design, w, h)
        pixels = pixels_cache[(w, h)]
        base = os.path.join(flags_root, subdir)
        write_tga(os.path.join(base, f"{tag}.tga"),            w, h, pixels)
        write_tga(os.path.join(base, f"{tag}_neutrality.tga"), w, h, pixels)
    print(f"  {tag} — flags written ({tag}.tga + {tag}_neutrality.tga, all 3 sizes)")

# ─────────────────────────────────────────────────────────────────────────────
# Update common/countries/colors.txt
# ─────────────────────────────────────────────────────────────────────────────
color_map = {tag: rgb for tag, _, rgb in NATIONS}
color_map["SPQ"] = (150, 20, 20)   # preserve Rome's existing colour

colors_path = os.path.join(MOD, "common", "countries", "colors.txt")
with open(colors_path) as f:
    content = f.read()

def repl_colors(m):
    tag = m.group(1)
    if tag in color_map:
        r, g, b = color_map[tag]
        return f'{tag} = {{ color = rgb {{ {r} {g} {b} }} }}'
    return m.group(0)

content = re.sub(
    r'(\w+)\s*=\s*\{\s*color\s*=\s*rgb\s*\{[^}]*\}\s*\}',
    repl_colors, content
)
with open(colors_path, 'w') as f:
    f.write(content)
print("\n  common/countries/colors.txt — updated")

# ─────────────────────────────────────────────────────────────────────────────
# Update common/countries/{Name}.txt  (the `color = { R G B }` line in each)
# ─────────────────────────────────────────────────────────────────────────────
COUNTRY_FILES = {
    "CRG": "Carthage.txt",    "MCD": "Macedonia.txt",
    "KMT": "Egypt.txt",       "SEL": "Seleucida.txt",
    "SYC": "Syracuse.txt",    "GRC": "Greeks.txt",
    "LAC": "Sparta.txt",      "SMN": "Samnites.txt",
    "PHN": "Phoenicia.txt",   "IBR": "Iberia.txt",
    "GLN": "Gauls.txt",       "ILL": "Illyria.txt",
    "THR": "Thrace.txt",      "WLD": "Wasteland.txt",
}

for tag, filename in COUNTRY_FILES.items():
    r, g, b = color_map[tag]
    path = os.path.join(MOD, "common", "countries", filename)
    with open(path) as f:
        text = f.read()
    # Replace `color = { ... }` but not `color_ui = { ... }`
    text = re.sub(r'(?<![_\w])color\s*=\s*\{[^}]*\}', f'color = {{ {r} {g} {b} }}', text)
    with open(path, 'w') as f:
        f.write(text)
    print(f"  {filename}: color = {{ {r} {g} {b} }}")

print("\nDone. All flags generated and colours updated.")
