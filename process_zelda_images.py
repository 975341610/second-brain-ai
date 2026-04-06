import os
from PIL import Image

def convert_and_save(src_path, dest_path, max_size=None):
    img = Image.open(src_path)
    if max_size:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Save as WebP
    img.save(dest_path, "WEBP", quality=85)
    print(f"Converted {src_path} -> {dest_path}")

# Mapping: original_filename -> (new_subdir, new_name, max_size)
mapping = {
    "023.jpg": ("splash", "main.webp", (1920, 1080)),
    "353.jpg": ("splash", "champions.webp", (1920, 1080)),
    "024.jpg": ("ui", "hyrule_day.webp", (1920, 1080)),
    "019.jpg": ("ui", "hyrule_sunset.webp", (1920, 1080)),
    "050.jpg": ("sprites", "link.webp", (800, 1200)),
    "354.jpg": ("sprites", "zelda.webp", (800, 1200)),
    "357.jpg": ("sprites", "revali.webp", (800, 1200)),
    "358.jpg": ("sprites", "urbosa.webp", (800, 1200)),
    "361.jpg": ("sprites", "sidon.webp", (800, 1200)),
}

source_dir = "assets/zelda_images/塞尔达图片/"
target_base_dir = "second-brain-ai/frontend/src/assets/"

results = []

for src_name, (subdir, new_name, max_size) in mapping.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(target_base_dir, subdir, new_name)
    
    if os.path.exists(src_path):
        convert_and_save(src_path, dest_path, max_size)
        results.append({
            "old": src_name,
            "new": os.path.join(subdir, new_name),
            "full_path": dest_path
        })
    else:
        print(f"Warning: {src_path} not found")

# Print the report
print("\nRenaming Report:")
print("| Original Filename | New Filename | Category |")
print("| --- | --- | --- |")
for item in results:
    cat = item['new'].split('/')[0]
    print(f"| {item['old']} | {item['new']} | {cat} |")
