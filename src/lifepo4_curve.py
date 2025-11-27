import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. ข้อมูลมาตรฐาน LiFePO4 (3.2V Cell)
# State of Charge (%)
soc = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# Voltage (V) - ข้อมูลจากสเปคมาตรฐาน
voltage = np.array([2.50, 3.00, 3.20, 3.22, 3.25, 3.26, 3.27, 3.30, 3.32, 3.35, 3.65])

# 2. ทำให้เส้นโค้งเนียนขึ้น (Smooth Curve) ด้วย Spline Interpolation
X_Y_Spline = make_interp_spline(soc, voltage)
X_ = np.linspace(soc.min(), soc.max(), 500)
Y_ = X_Y_Spline(X_)

# 3. ตั้งค่ากราฟ (Theme: Batly Style - Yellow/Dark Grey)
plt.figure(figsize=(10, 6), facecolor='#ffffff') # พื้นหลังรูป
ax = plt.axes()
ax.set_facecolor('#f8f9fa') # พื้นหลังกราฟ

# วาดเส้นกราฟ
plt.plot(X_, Y_, color='#1A5276', linewidth=3, label='Discharge Curve') # เส้นสีน้ำเงินเข้ม

# 4. ตกแต่งกราฟ
plt.title('LiFePO4 (3.2V) State of Charge vs Voltage', fontsize=16, fontweight='bold', color='#333333')
plt.xlabel('State of Charge (%)', fontsize=12)
plt.ylabel('Voltage (V)', fontsize=12)

# กำหนดช่วงแกน
plt.xlim(0, 100)
plt.ylim(2.4, 3.8)
plt.xticks(np.arange(0, 101, 10))
plt.grid(color='#cccccc', linestyle='--', linewidth=0.5)

# 5. ไฮไลท์จุดสำคัญ (Knee Points)
key_points = [(10, 3.00), (90, 3.35)]
for x, y in key_points:
    plt.plot(x, y, 'ro') # จุดแดง
    plt.text(x+2, y-0.05, f'{y}V ({x}%)', fontsize=10, color='red')

# โซนทำงานปกติ (Flat Curve)
plt.axvspan(20, 80, color='#ffe70e', alpha=0.15) # สีเหลืองจางๆ ช่วงใช้งาน
plt.text(50, 3.4, 'Stable Operating Range (Flat Curve)', ha='center', fontsize=10, color='#555')

plt.tight_layout()

# 6. บันทึกไฟล์
plt.savefig('lifepo4_chart.png', dpi=300)
plt.show()