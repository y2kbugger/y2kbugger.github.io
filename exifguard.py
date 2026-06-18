#!/usr/bin/env python3
"""Detect and strip privacy-sensitive image metadata (EXIF/GPS/XMP/etc).

Phone cameras embed GPS coordinates, device make/model, serial numbers, and
timestamps in image metadata. Publishing those leaks where (and with what)
a photo was taken. This guard scans the content image tree and can strip the
offending metadata losslessly, while preserving display-critical tags
(EXIF Orientation and the embedded ICC color profile).

Usage:
    python exifguard.py check [PATH ...]   # exit 1 if any leak is found
    python exifguard.py strip [PATH ...]   # remove metadata in place

PATH defaults to ``content/img``. Stripping rewrites only the metadata; the
encoded pixel data is left untouched (no recompression).

Requires the ``exiftool`` command-line tool, which handles JPEG, PNG, GIF,
TIFF, and WebP losslessly.
"""
from __future__ import annotations

import json
import shutil
import struct
import subprocess
import sys
from pathlib import Path

DEFAULT_PATH = Path("content/img")
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".webp"}

# Metadata groups (exiftool family 0) that should never reach a published image.
SENSITIVE_GROUPS = {"EXIF", "GPS", "XMP", "IPTC", "MakerNotes", "Photoshop", "Adobe"}

# Tags that are kept on purpose because they affect how the image renders, not
# who/where it came from. Matched by bare tag name (after the group prefix).
# ``YCbCrPositioning`` is a non-identifying structural tag that exiftool
# re-adds to the rebuilt IFD when we preserve Orientation.
ALLOWED_TAGS = {"Orientation", "YCbCrPositioning"}

# Textual tags that leak identity even when stored in a format's own chunk
# group (e.g. PNG ``tEXt``/``iTXt`` or GIF comment extensions).
SENSITIVE_TEXT_TAGS = {
    "Artist", "Author", "By-line", "Comment", "Copyright", "Creator",
    "CreatorTool", "Description", "DocumentName", "HostComputer", "Make",
    "Model", "OwnerName", "Software", "Source", "Title", "UserComment",
}


def require_exiftool() -> str:
    exe = shutil.which("exiftool")
    if exe is None:
        sys.exit(
            "error: exiftool not found. Install it (e.g. `sudo pacman -S perl-image-exiftool`"
            " or `apt install libimage-exiftool-perl`) and retry."
        )
    return exe


# PNG ancillary chunks that carry metadata rather than pixels or color. EXIF
# from phone/Google/ImageMagick pipelines is often hidden in a ``zTXt`` "Raw
# profile" chunk that exiftool cannot delete, so we drop these chunks directly.
PNG_METADATA_CHUNKS = {b"tEXt", b"zTXt", b"iTXt", b"eXIf", b"tIME", b"dSIG"}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def strip_png_chunks(path: Path) -> bool:
    """Losslessly drop metadata chunks from a PNG. Returns True if rewritten.

    Only ancillary metadata chunks are removed; structural chunks (IHDR, PLTE,
    IDAT, IEND) and color/display chunks (iCCP, sRGB, gAMA, cHRM, sBIT, ...)
    are preserved byte-for-byte, so the decoded image is unchanged.
    """
    data = path.read_bytes()
    if data[:8] != PNG_SIGNATURE:
        return False
    out = bytearray(PNG_SIGNATURE)
    i = 8
    removed = False
    n = len(data)
    while i + 8 <= n:
        (length,) = struct.unpack(">I", data[i:i + 4])
        ctype = data[i + 4:i + 8]
        end = i + 12 + length  # length + type + data + crc
        if end > n:
            break
        if ctype in PNG_METADATA_CHUNKS:
            removed = True
        else:
            out += data[i:end]
        if ctype == b"IEND":
            break
        i = end
    if removed:
        path.write_bytes(bytes(out))
    return removed



def iter_images(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for root in paths:
        if root.is_file():
            if root.suffix.lower() in IMAGE_SUFFIXES:
                files.append(root)
        elif root.is_dir():
            files.extend(
                p for p in sorted(root.rglob("*"))
                if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
            )
    return files


def sensitive_tags(exiftool: str, files: list[Path]) -> dict[Path, list[str]]:
    """Return a mapping of file -> list of offending ``Group:Tag`` strings."""
    if not files:
        return {}
    proc = subprocess.run(
        [exiftool, "-json", "-G", "-a", "-s", "-n", *map(str, files)],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0 and not proc.stdout.strip():
        sys.exit(f"error: exiftool failed:\n{proc.stderr.strip()}")

    offenders: dict[Path, list[str]] = {}
    for entry in json.loads(proc.stdout or "[]"):
        path = Path(entry["SourceFile"])
        hits: list[str] = []
        for key in entry:
            if ":" not in key:
                continue
            group, _, tag = key.partition(":")
            if tag in ALLOWED_TAGS:
                continue
            if group in SENSITIVE_GROUPS or tag in SENSITIVE_TEXT_TAGS:
                hits.append(f"{group}:{tag}")
        if hits:
            offenders[path] = sorted(hits)
    return offenders


def cmd_check(exiftool: str, files: list[Path]) -> int:
    offenders = sensitive_tags(exiftool, files)
    if not offenders:
        print(f"clean: no sensitive metadata in {len(files)} image(s)")
        return 0
    print(f"LEAK: sensitive metadata found in {len(offenders)} of {len(files)} image(s):\n")
    for path in sorted(offenders):
        tags = offenders[path]
        gps = " [GPS]" if any(t.startswith("GPS:") for t in tags) else ""
        print(f"  {path}{gps}")
        print(f"      {', '.join(tags)}")
    print("\nRun `python exifguard.py strip` (or `make exif-strip`) to remove it.")
    return 1


def cmd_strip(exiftool: str, files: list[Path]) -> int:
    offenders = sensitive_tags(exiftool, files)
    if not offenders:
        print(f"clean: nothing to strip in {len(files)} image(s)")
        return 0
    targets = sorted(offenders)
    # PNGs often hide EXIF/XMP in text chunks exiftool can't delete; strip those
    # directly. exiftool handles the rest (JPEG/GIF/TIFF/WebP) while preserving
    # the display-critical Orientation tag and embedded ICC color profile.
    pngs = [p for p in targets if p.suffix.lower() == ".png"]
    others = [p for p in targets if p.suffix.lower() != ".png"]

    for path in pngs:
        strip_png_chunks(path)

    if others:
        proc = subprocess.run(
            [
                exiftool, "-all=", "-tagsfromfile", "@",
                "-Orientation", "-ICC_Profile",
                "-overwrite_original", *map(str, others),
            ],
            capture_output=True, text=True, check=False,
        )
        if proc.returncode != 0:
            sys.exit(f"error: exiftool strip failed:\n{proc.stderr.strip()}")

    remaining = sensitive_tags(exiftool, targets)
    for path in targets:
        status = "FAILED" if path in remaining else "stripped"
        print(f"  {status}: {path}")
    if remaining:
        sys.exit(f"\nerror: {len(remaining)} image(s) still contain metadata")
    print(f"\nstripped sensitive metadata from {len(targets)} image(s)")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 1 or argv[0] not in {"check", "strip"}:
        print(__doc__)
        return 2
    command, rest = argv[0], argv[1:]
    paths = [Path(p) for p in rest] or [DEFAULT_PATH]
    exiftool = require_exiftool()
    files = iter_images(paths)
    if command == "check":
        return cmd_check(exiftool, files)
    return cmd_strip(exiftool, files)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
