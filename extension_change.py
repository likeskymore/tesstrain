import os
from PIL import Image  # Make sure Pillow is installed: pip install pillow

# === Set your directory ===
directory ="data/trustsoft-ground-truth"  # ← Replace this with your actual path

# === 1. Rename .txt files to .gt.txt ===
for filename in os.listdir(directory):
    if filename.endswith(".txt") and not filename.endswith(".gt.txt"):
        base = filename[:-4]  # remove ".txt"
        new_filename = f"{base}.gt.txt"
        os.rename(
            os.path.join(directory, filename),
            os.path.join(directory, new_filename)
        )
        print(f"Renamed TXT: {filename} → {new_filename}")

# === 2. Convert .jpg to .png ===
for filename in os.listdir(directory):
    if filename.lower().endswith(".jpg"):
        jpg_path = os.path.join(directory, filename)
        png_filename = filename[:-4] + ".png"
        png_path = os.path.join(directory, png_filename)

        try:
            with Image.open(jpg_path) as img:
                img.save(png_path)
            print(f"Converted: {filename} → {png_filename}")
            os.remove(jpg_path)  # optional: delete original JPG
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
