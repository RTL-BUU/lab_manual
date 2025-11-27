import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. Li-Po Standard Voltage Curve (Resting Voltage)
# Data points approximated for standard Li-Po chemistry
soc = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
voltage = np.array([3.20, 3.60, 3.68, 3.73, 3.79, 3.85, 3.92, 3.99, 4.06, 4.13, 4.20])

# 2. Smooth Curve Interpolation
X_Y_Spline = make_interp_spline(soc, voltage)
X_ = np.linspace(soc.min(), soc.max(), 500)
Y_ = X_Y_Spline(X_)

# 3. Setup Graph Theme (Batly Style)
plt.figure(figsize=(10, 6), facecolor='#ffffff')
ax = plt.axes()
ax.set_facecolor('#f8f9fa')

# Plot the curve
plt.plot(X_, Y_, color='#C0392B', linewidth=3, label='Discharge Curve') # สีแดงเลือดหมู

# 4. Decoration
plt.title('Li-Po (3.7V) State of Charge vs Voltage', fontsize=16, fontweight='bold', color='#333333')
plt.xlabel('State of Charge (%)', fontsize=12)
plt.ylabel('Voltage (V)', fontsize=12)

# Axis Settings
plt.xlim(0, 100)
plt.ylim(3.0, 4.4)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(3.0, 4.5, 0.2))
plt.grid(color='#cccccc', linestyle='--', linewidth=0.5)

# 5. Highlight Key Points
key_points = [(20, 3.68), (50, 3.85), (100, 4.20)]
for x, y in key_points:
    plt.plot(x, y, 'ko', markersize=6) # จุดสีดำ
    plt.text(x+2, y-0.05, f'{y}V ({x}%)', fontsize=10, color='#333')

# Storage Zone Highlight
plt.axvspan(45, 55, color='#27AE60', alpha=0.15) # สีเขียวอ่อนช่วง Storage
plt.text(50, 4.3, 'Best Storage Range (3.80V-3.85V)', ha='center', fontsize=10, color='green', fontweight='bold')

plt.tight_layout()

# 6. Save File
plt.savefig('lipo_chart.png', dpi=300)
print("Graph saved to lipo_chart.png")
# plt.show()