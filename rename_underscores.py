#!/usr/bin/env python3
"""
rename_underscores.py
Replace "_" with "-" in file names (and optionally folder names) in a MyST
web book, and update every reference to those names in myst.yml, Markdown,
notebooks, CSS, BibTeX, etc.

Usage (run from the book's root folder, where myst.yml lives):

    python rename_underscores.py                 # dry run: show what would change
    python rename_underscores.py --apply         # rename files + update references
    python rename_underscores.py --dirs          # dry run, folders included
    python rename_underscores.py --dirs --apply  # rename files AND folders

Options:
    --root PATH   book folder (default: current folder)

Not renamed:
  - names starting with "_" or "." (e.g. _toc.yml, __init__.py, .gitignore)
  - Python files (.py), because module names can't contain dashes
  - anything inside .git, _build, .github, .ipynb_checkpoints, node_modules
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

SKIP_DIRS = {".git", "_build", ".github", ".ipynb_checkpoints",
             "node_modules", "__pycache__"}
SKIP_SUFFIXES = {".py", ".pyc"}
TEXT_SUFFIXES = {".md", ".ipynb", ".yml", ".yaml", ".css", ".html", ".bib",
                 ".txt", ".py", ".json", ".tex", ".csv"}


def walk(root):
    """os.walk that skips excluded and hidden folders."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames
                             if d not in SKIP_DIRS and not d.startswith("."))
        yield Path(dirpath), dirnames, sorted(filenames)


def wants_rename(name, is_dir=False):
    if "_" not in name:
        return False
    if name.startswith(("_", ".")):
        return False
    if not is_dir and Path(name).suffix.lower() in SKIP_SUFFIXES:
        return False
    return True


def make_pattern(old_name, is_dir):
    """Match old_name only as a whole path component, not inside other names."""
    before = r"(?<![\w.-])"
    after = r"(?=/)" if is_dir else r"(?![\w.-])"
    return re.compile(before + re.escape(old_name) + after)


def git_available(root):
    r = subprocess.run(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
                       capture_output=True, text=True)
    return r.returncode == 0


def move(src, dst, use_git):
    """Use 'git mv' when possible so Git records a rename; else a plain rename."""
    if use_git:
        r = subprocess.run(["git", "mv", str(src), str(dst)],
                           capture_output=True, text=True)
        if r.returncode == 0:
            return
    src.rename(dst)


def update_references(root, replacements, apply):
    edited = 0
    for dirpath, _, filenames in walk(root):
        for f in filenames:
            path = dirpath / f
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            try:
                with open(path, encoding="utf-8", newline="") as fh:
                    text = fh.read()
            except (UnicodeDecodeError, OSError):
                continue
            new_text, hits = text, 0
            for pattern, new_name in replacements:
                new_text, n = pattern.subn(lambda m, s=new_name: s, new_text)
                hits += n
            if hits:
                edited += 1
                print(f"  edit    {path.relative_to(root)}  "
                      f"({hits} reference{'s' if hits != 1 else ''})")
                if apply:
                    with open(path, "w", encoding="utf-8", newline="") as fh:
                        fh.write(new_text)
    return edited


def main():
    ap = argparse.ArgumentParser(description="Replace _ with - in MyST book file names.")
    ap.add_argument("--root", default=".", help="book folder (default: current folder)")
    ap.add_argument("--apply", action="store_true", help="make the changes (default: dry run)")
    ap.add_argument("--dirs", action="store_true", help="also rename folders")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not (root / "myst.yml").exists():
        sys.exit(f"No myst.yml found in {root}. Run this from the book's root "
                 f"folder or use --root PATH.")

    # 1. Work out what to rename
    files, dirs = [], []
    for dirpath, dirnames, filenames in walk(root):
        files += [dirpath / f for f in filenames if wants_rename(f)]
        if args.dirs:
            dirs += [dirpath / d for d in dirnames if wants_rename(d, is_dir=True)]

    renames, replacements = [], []
    for path, is_dir in [(p, False) for p in files] + [(p, True) for p in dirs]:
        new = path.with_name(path.name.replace("_", "-"))
        if new.exists():
            print(f"  SKIP    {path.relative_to(root)}  ({new.name} already exists)")
            continue
        renames.append((path, new, is_dir))
        replacements.append((make_pattern(path.name, is_dir), new.name))

    if not renames:
        print("Nothing to rename.")
        return

    mode = "APPLYING" if args.apply else "DRY RUN (nothing will be changed)"
    print(f"\n{mode}\n")

    print("Renames:")
    for old, new, is_dir in renames:
        kind = "folder" if is_dir else "file  "
        print(f"  {kind}  {old.relative_to(root)}  ->  {new.name}")

    # 2. Update references first, while the old paths still exist
    print("\nReferences:")
    edited = update_references(root, replacements, args.apply)
    if not edited:
        print("  (none found)")

    # 3. Rename files, then folders deepest-first so parent paths stay valid
    if args.apply:
        use_git = git_available(root)
        for old, new, _ in sorted(renames, key=lambda r: (r[2], -len(r[0].parts))):
            move(old, new, use_git)

    print(f"\n{len(renames)} item(s) to rename, {edited} file(s) with references.")
    if not args.apply:
        print("Run again with --apply to make these changes.")
    else:
        print("Done. Now run 'myst build' and check the output for broken links.")


if __name__ == "__main__":
    main()
