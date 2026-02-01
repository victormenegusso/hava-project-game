from PIL import Image

def process_image(input_path, output_path, target_size):
    try:
        img = Image.open(input_path).convert("RGBA")
        
        # Resize to target size using Nearest Neighbor to keep pixel art look
        # But if the image is huge (1024) and we want 64, we might lose detail with Nearest if it's not perfect grid
        # Let's use BOX or LANCZOS for downscaling high-res generation, 
        # but since we want "Pixel Art" look, usually NEAREST is best if the source IS pixel art.
        # However, the source is AI generated 1024x1024. It likely has "soft" pixels.
        # Let's resize with LANCZOS to get a sharp small image, then maybe quantize?
        # Actually, let's just resize with LANCZOS.
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Check for white (or very close to white)
            # Threshold: 240
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0)) # Transparent
            else:
                newData.append(item)
        
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Processed {input_path} -> {output_path} ({target_size})")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Process Player
process_image(
    "C:/Users/victo/.gemini/antigravity/brain/fda8ac8a-e2a5-4afc-967a-efd2b097ad6b/player_white_bg_1769967995972.png", 
    "assets/images/player.png", 
    (64, 64)
)

# Process Tileset
process_image(
    "C:/Users/victo/.gemini/antigravity/brain/fda8ac8a-e2a5-4afc-967a-efd2b097ad6b/tileset_white_bg_1769968011247.png", 
    "assets/images/tileset.png", 
    (128, 128)
)
