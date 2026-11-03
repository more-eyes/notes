#!/usr/bin/env python3
"""Build link preview cards for more-eyes.org.

For each note in the repository root, read the title (the first "# " line),
the subtitle (the italic line under it), and the number on the Version line.
Draw a 1200x630 PNG for the note and write Jekyll front matter defaults that
point jekyll-seo-tag at it. The note files are not changed.

Usage:
  python3 .github/og/build_og.py --fonts DIR [--config _config.yml]

With --config, the defaults are appended to that file. Run this in CI on the
checked-out copy only; the generated images and config are not committed.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "assets" / "og"
SKIP = {"README.md", "STYLE.md", "AGENTS.md"}
W, H = 1200, 630
MARGIN = 80
INK = (31, 35, 40)
MUTED = (87, 96, 106)
RULE = (208, 215, 222)
BG = (255, 255, 255)
DASHES = "\u2013\u2014"

VERSION_RE = re.compile(r"^\|\s*\*\*Version\*\*\s*\|\s*([0-9]+(?:\.[0-9]+)+)")


def parse_note(path):
    title = subtitle = version = None
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if title is None and s.startswith("# "):
            title = s[2:].strip()
        elif title and subtitle is None and re.fullmatch(r"\*[^*].*\*", s):
            subtitle = s.strip("*").strip()
        m = VERSION_RE.match(s)
        if m:
            version = m.group(1)
            break
    if not (title and version):
        return None  # moved stubs and other non-notes have no Version line
    return {"file": path.name, "title": title, "subtitle": subtitle, "version": version}


def git_date(path, first):
    args = ["git", "log", "--format=%cI", "--", path.name]
    if first:
        args.insert(2, "--reverse")
    out = subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.split()
    return out[0] if out else None


def wrap(draw, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, fonts_dir, width):
    # Two lines at a large size if they fit, else three lines at a smaller one.
    for size, max_lines in ((76, 2), (70, 2), (64, 2), (58, 3), (54, 3), (50, 3)):
        font = ImageFont.truetype(str(fonts_dir / "Inter-Bold.ttf"), size)
        lines = wrap(draw, text, font, width)
        if len(lines) <= max_lines:
            return font, lines, size
    return font, lines[:3], size


def draw_card(out, title, subtitle, footer, fonts_dir):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    brand = ImageFont.truetype(str(fonts_dir / "Inter-SemiBold.ttf"), 34)
    body = ImageFont.truetype(str(fonts_dir / "Inter-Regular.ttf"), 34)
    foot = ImageFont.truetype(str(fonts_dir / "Inter-SemiBold.ttf"), 30)
    text_w = W - 2 * MARGIN

    d.text((MARGIN, 64), "more eyes", font=brand, fill=INK)
    d.line([(MARGIN, 122), (W - MARGIN, 122)], fill=RULE, width=2)

    tfont, tlines, tsize = fit_title(d, title, fonts_dir, text_w)
    y = 168
    for line in tlines:
        d.text((MARGIN, y), line, font=tfont, fill=INK)
        y += int(tsize * 1.18)
    if subtitle:
        y += 18
        for line in wrap(d, subtitle, body, text_w)[:2]:
            d.text((MARGIN, y), line, font=body, fill=MUTED)
            y += 46

    d.line([(MARGIN, H - 112), (W - MARGIN, H - 112)], fill=RULE, width=2)
    d.text((MARGIN, H - 88), footer, font=foot, fill=MUTED)
    url = "more-eyes.org"
    d.text((W - MARGIN - d.textlength(url, font=foot), H - 88), url, font=foot, fill=MUTED)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", required=True, type=pathlib.Path)
    ap.add_argument("--config", type=pathlib.Path)
    ap.add_argument("--only", help="build one note file, for previews")
    a = ap.parse_args()

    site_desc = "Open is not the same as looked at."
    draw_card(OUT_DIR / "more-eyes.png", "Open is not the same as looked at.",
              "Sourced, versioned notes on what evidence a software or custody claim needs.",
              "Notes", a.fonts)
    # Site wide default first; Jekyll prefers the more specific path scope below.
    defaults = [{"scope": {"path": ""}, "values": {"image": {
        "path": "/assets/og/more-eyes.png", "width": W, "height": H,
        "alt": "more eyes: " + site_desc}}}]

    for path in sorted(ROOT.glob("*.md")):
        if path.name in SKIP or (a.only and path.name != a.only):
            continue
        note = parse_note(path)
        if not note:
            continue
        for field in ("title", "subtitle"):
            if note[field] and any(c in note[field] for c in DASHES):
                print(f"warning: dash in {field} of {path.name}", file=sys.stderr)
        v = note["version"]
        img_rel = f"assets/og/{path.stem}-v{v}.png"
        draw_card(ROOT / img_rel, note["title"], note["subtitle"], f"Version {v}", a.fonts)
        values = {
            "title": f'{note["title"]} (v{v})',
            "image": {"path": "/" + img_rel, "width": W, "height": H,
                      "alt": f'{note["title"]} Version {v}. more eyes'},
            "seo": {"type": "Article"},
        }
        if note["subtitle"]:
            values["description"] = note["subtitle"]
        first, last = git_date(path, True), git_date(path, False)
        if first:
            values["date"] = first  # makes jekyll-seo-tag emit og:type article
        if last:
            values["last_modified_at"] = last
        defaults.append({"scope": {"path": path.name}, "values": values})
        print(f"{path.name}: v{v} -> {img_rel}")

    block = "\n# Added in CI by .github/og/build_og.py. Not committed.\ndefaults: " + json.dumps(defaults, ensure_ascii=False) + "\n"
    if a.config:
        text = a.config.read_text(encoding="utf-8")
        if re.search(r"^defaults:", text, re.M):
            sys.exit("_config.yml already has a defaults key; merge by hand")
        a.config.write_text(text + block, encoding="utf-8")
    else:
        sys.stdout.write(block)


if __name__ == "__main__":
    main()
