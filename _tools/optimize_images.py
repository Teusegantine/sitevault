import os
from PIL import Image
import glob

dirs_to_optimize = [
    "assets/images/characters",
    "assets/images/logo"
]
html_file = "index.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

for d in dirs_to_optimize:
    png_files = glob.glob(os.path.join(d, "*.png")) + glob.glob(os.path.join(d, "*.jpg")) + glob.glob(os.path.join(d, "*.jpeg"))
    for file_path in png_files:
        try:
            img = Image.open(file_path)
            
            # Use appropriate resolution based on directory
            max_size = (1200, 1200) if "characters" in d else (800, 800)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            ext = os.path.splitext(file_path)[1]
            webp_path = file_path.replace(ext, ".webp")
            img.save(webp_path, "WEBP", quality=85, method=6)
            
            # Update HTML
            old_path = file_path.replace("\\", "/")
            new_path = webp_path.replace("\\", "/")
            content = content.replace(old_path, new_path)
            
            # Clean up old file
            os.remove(file_path)
            print(f"Optimized: {old_path} -> {new_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Additional optimizations complete!")
