import os
from pathlib import Path
from PIL import Image
import pytesseract

# === Configuration ===
INPUT_FOLDER = Path("testdata")
OUTPUT_FOLDER = Path("results")
MODEL = "trustsoft8_v1"

# === Create output directory if it doesn't exist ===
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# === Supported image extensions ===
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".tif"}

# === Process all image files in the input folder ===
for image_path in INPUT_FOLDER.iterdir():
    if image_path.suffix.lower() in IMAGE_EXTS:
        print(f"🖼️ Processing: {image_path.name}")
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img, lang=MODEL)

            output_file = OUTPUT_FOLDER / f"{MODEL}_{image_path.stem}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"✅ Saved to: {output_file}")

        except Exception as e:
            print(f"❌ Failed to process {image_path.name}: {e}")
