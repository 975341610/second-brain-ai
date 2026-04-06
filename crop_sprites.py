import cv2
import os
import numpy as np

def crop_sprites(image_path, output_dir, prefix):
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use a safer threshold to ignore light gray background noise
    # Since background is ~230-255 and elements are dark (0-50),
    # threshold 128 is much safer than 250.
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    count = 1
    # Filter and collect boxes
    bounding_boxes = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Skip small noise
        if w < 20 or h < 20:
            continue
        bounding_boxes.append((x, y, w, h))
        
    # Sort boxes by y coordinate then x coordinate for more intuitive naming
    bounding_boxes.sort(key=lambda b: (b[1], b[0]))

    for x, y, w, h in bounding_boxes:
        # Crop the element from the original image
        crop = img[y:y+h, x:x+w]

        # Use the mask for alpha channel to preserve transparency
        mask_crop = thresh[y:y+h, x:x+w]
        
        # Split channels
        b, g, r = cv2.split(crop)
        # Combine BGR and Mask to get BGRA
        rgba = cv2.merge([b, g, r, mask_crop])

        # Save to PNG
        output_name = f"{prefix}_{count:03d}.png"
        output_path = os.path.join(output_dir, output_name)
        cv2.imwrite(output_path, rgba)
        count += 1
    
    print(f"Total {count-1} sprites cropped from {image_path}")

output_folder = "second-brain-ai/frontend/src/assets/p5r/"
# Clear output directory to avoid old files if needed
if os.path.exists(output_folder):
    for f in os.listdir(output_folder):
        os.remove(os.path.join(output_folder, f))
else:
    os.makedirs(output_folder, exist_ok=True)

crop_sprites("./img_v3_02106_05fcfd29-3203-43df-bb18-e61e6d68a35g.png", output_folder, "sprite1")
crop_sprites("./img_v3_02106_7a7fe163-0bb4-4a78-950e-7995ba2c65cg.png", output_folder, "sprite2")
