from PIL import Image, ImageDraw, ImageFont
import os

def create_rtl_favicon(output_path, size=64, bg_color="#003366", text_color="#FFFFFF"):
    # 1. สร้างพื้นหลังสี่เหลี่ยม (สีน้ำเงินเข้ม RTL)
    image = Image.new("RGBA", (size, size), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    # 2. เตรียมฟอนต์ (พยายามใช้ฟอนต์ที่มีในเครื่อง ถ้าไม่มีจะใช้ Default)
    # เราจะวาดตัว 'R' ให้ใหญ่ๆ ตรงกลาง
    try:
        # ลองเรียกฟอนต์หนาๆ ใน Windows (เช่น Arial Bold)
        font_path = "arialbd.ttf" 
        font_size = int(size * 0.75) # ขนาดตัวอักษร 75% ของกล่อง
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        # ถ้าหาฟอนต์ไม่เจอ ให้ใช้ default (อาจจะไม่สวยเท่า)
        font = ImageFont.load_default()
        print("Warning: Arial Bold font not found, using default.")

    # 3. คำนวณตำแหน่งจัดกึ่งกลาง
    text = "R"
    # ใช้ textbbox เพื่อหาขนาดที่แท้จริงของตัวอักษร
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w = right - left
    text_h = bottom - top
    
    x = (size - text_w) // 2
    y = (size - text_h) // 2 - (size * 0.1) # ขยับขึ้นนิดนึงเพื่อความสมดุลสายตา

    # 4. วาดตัว R สีขาว
    draw.text((x, y), text, font=font, fill=text_color)
    
    # 5. บันทึกไฟล์
    image.save(output_path)
    print(f"สร้าง Favicon สำเร็จ: {output_path}")

# --- เรียกใช้งาน ---
# สร้างไฟล์ชื่อ favicon_rtl.png
create_rtl_favicon("favicon_rtl.png")