from PIL import Image
from pathlib import Path

# === Config ===
FOLDER = Path("testdata")  # Replace with actual folder path
FILES = sorted(FOLDER.iterdir())

# === Process and Rename ===
for i, file in enumerate(FILES, start=1):
    target_name = FOLDER / f"{i}.png"

    if file.suffix.lower() != ".png":
        with Image.open(file) as img:
            img.convert("RGB").save(target_name, format="PNG")
        file.unlink()  # Delete original non-png file
    else:
        file.rename(target_name)

print("✅ Done: All files converted and renamed to PNG.")
