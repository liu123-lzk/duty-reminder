"""用 PIL 从 SVG 生成 PNG 图标"""
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])
    from PIL import Image, ImageDraw, ImageFont

import os

def create_icon(size, path):
    img = Image.new('RGBA', (size, size), (26, 26, 46, 255))
    draw = ImageDraw.Draw(img)
    
    # 圆角矩形
    r = size // 8
    draw.rounded_rectangle([0, 0, size, size], radius=r, fill=(26, 26, 46, 255))
    
    # 黄色圆
    cy = size * 0.38
    cr = size * 0.18
    draw.ellipse([size//2-cr, cy-cr, size//2+cr, cy+cr], fill=(251, 191, 36, 255))
    
    # 文字 "执勤"
    try:
        font_size = size // 6
        font = ImageFont.truetype("C:\\Windows\\Fonts\\msyh.ttc", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "执勤"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((size//2 - tw//2, size * 0.72 - th//2), text, fill=(226, 232, 240, 255), font=font)
    
    img.save(path, 'PNG')

base = os.path.dirname(os.path.abspath(__file__))
create_icon(192, os.path.join(base, 'icon-192.png'))
create_icon(512, os.path.join(base, 'icon-512.png'))
print("Icons generated!")
