import os
import shutil
import json
import sys
import ctypes

DESKTOP_PATH = os.path.expanduser("~/Desktop")
RULES_FILE = "rules.json"
UNDO_LOG = os.path.join(DESKTOP_PATH, ".desktop_organizer_undo.log")


def load_rules():
    with open(RULES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    rules = data["rules"]
    rules.sort(key=lambda r: r["priority"])
    return rules


def organize(dry_run=False):
    rules = load_rules()
    moves = []
    moved_count = 0

    for filename in os.listdir(DESKTOP_PATH):
        src = os.path.join(DESKTOP_PATH, filename)

        if not os.path.isfile(src):
            continue

        for rule in rules:
            if any(filename.lower().endswith(ext) for ext in rule["extensions"]):
                dest_dir = os.path.join(DESKTOP_PATH, rule["destination"])
                os.makedirs(dest_dir, exist_ok=True)

                dest = os.path.join(dest_dir, filename)

                if os.path.abspath(src) == os.path.abspath(dest):
                    break  # already organized

                if dry_run:
                    print(f"[DRY-RUN] {filename} → {rule['destination']}/")
                    break

                try:
                    shutil.move(src, dest)
                    moves.append(f"{dest}|{src}")
                    moved_count += 1
                except Exception:
                    pass

                break  # first matching rule wins

    if moves and not dry_run:
        with open(UNDO_LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(moves))

    return moved_count


def undo():
    if not os.path.exists(UNDO_LOG):
        ctypes.windll.user32.MessageBoxW(
            0, "No undo information found.", "Undo", 0
        )
        return

    with open(UNDO_LOG, "r", encoding="utf-8") as f:
        moves = f.readlines()

    for line in reversed(moves):
        dest, src = line.strip().split("|")
        if os.path.exists(dest):
            try:
                shutil.move(dest, src)
            except Exception:
                pass

    os.remove(UNDO_LOG)

    ctypes.windll.user32.MessageBoxW(
        0, "Desktop organization has been undone.", "Undo Complete", 0
    )


if __name__ == "__main__":
    if "--undo" in sys.argv:
        undo()
    elif "--dry-run" in sys.argv:
        organize(dry_run=True)
    else:
        moved = organize()
        ctypes.windll.user32.MessageBoxW(
            0,
            f"Desktop organized successfully.\nFiles moved: {moved}",
            "Desktop Organizer",
            0
        )
