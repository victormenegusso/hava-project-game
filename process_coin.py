from PIL import Image

def process_image(input_path, output_path, target_size):
    try:
        img = Image.open(input_path).convert("RGBA")
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Check for white (or very close to white)
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0)) # Transparent
            else:
                newData.append(item)
        
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Processed {input_path} -> {output_path} ({target_size})")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Process Coin
process_image(
    "C:/Users/victo/.gemini/antigravity/brain/fda8ac8a-e2a5-4afc-967a-efd2b097ad6b/coin_1769968547671.png", 
    "assets/images/coin.png", 
    (32, 32)
)
