from PIL import Image, ImageDraw

def create_spike_image(output_path, size=(32, 32)):
    try:
        # Create transparent image
        img = Image.new("RGBA", size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Define triangle points (bottom-left, top-center, bottom-right)
        # Pointing UP
        width, height = size
        p1 = (0, height - 1)           # Bottom left
        p2 = (width // 2, 0)           # Top center
        p3 = (width - 1, height - 1)   # Bottom right
        
        # Draw red triangle
        draw.polygon([p1, p2, p3], fill=(255, 0, 0, 255), outline=(100, 0, 0, 255))
        
        img.save(output_path, "PNG")
        print(f"Created spike placeholder at {output_path}")
        
    except Exception as e:
        print(f"Error creating spike image: {e}")

create_spike_image("assets/images/spikes.png")
