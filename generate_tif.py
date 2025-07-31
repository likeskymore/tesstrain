import subprocess
from pathlib import Path

INPUT_DIR = Path("testdata")
OUTPUT_DIR = Path("debug")
CUSTOM_MODEL_NAME = "trustsoft1"
TESSDATA_DIR = "E:/Tesseract/tessdata"

# Supported image extensions
IMAGE_EXTS = [".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp"]

for image_path in INPUT_DIR.iterdir():
    if image_path.suffix.lower() not in IMAGE_EXTS:
        continue

    image_name = image_path.stem
    output_base = OUTPUT_DIR / image_name

    cmd = [
        "tesseract",
        str(image_path),
        str(output_base),
        "-l", CUSTOM_MODEL_NAME,
        "--oem", "3",
        "--psm", "3",
        "--tessdata-dir", TESSDATA_DIR,
        "-c", "tessedit_write_images=true"
    ]

    print(f"🖼️ Processing: {image_path.name}")
    try:
        subprocess.run(cmd, check=True)

        # Delete .txt output if it exists
        txt_output = output_base.with_suffix(".txt")
        if txt_output.exists():
            txt_output.unlink()
            print(f"🗑️ Deleted: {txt_output.name}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error processing {image_path.name}: {e}")
