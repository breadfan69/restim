#!/usr/bin/env python3
from PIL import Image
import os

# Create ico files from PNG icons
for icon_name in ['banana', 'walnut', 'coyote']:
    png_path = f'resources/icons/{icon_name}.png'
    ico_path = f'resources/{icon_name}.ico'
    
    if os.path.exists(png_path):
        img = Image.open(png_path)
        img_resized = img.resize((256, 256), Image.Resampling.LANCZOS)
        img_resized.save(ico_path, 'ICO')
        print(f'Created {ico_path}')
    else:
        print(f'Error: {png_path} not found')
