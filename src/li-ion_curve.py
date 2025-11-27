import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# 1. Li-ion (NMC/NCA) Voltage Curve
# Linear drop from 4.2 to 3.6, then steep drop
soc = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
voltage = np.array([3.00, 3.30, 3.40, 3.50, 3.60, 3.70, 3.80, 3.90, 4.00, 4.10, 4.20])

# 2. Smooth Curve
X_Y_Spline = make_interp_spline(soc, voltage)
X_ = np.linspace(soc.min(), soc.max(), 500)
Y_ = X_Y_Spline(X_)

# 3. Setup Graph (Green Theme for Standard Li-ion)
plt.figure(figsize=(10, 6), facecolor='#ffffff')
ax = plt.axes()
ax.set_facecolor('#f8f9fa')

# Plot
plt.plot(X_, Y_, color='#27AE60', linewidth=3, label='Discharge Curve')

# 4. Decoration
plt.title('Li-ion (3.7V) State of Charge vs Voltage', fontsize=16, fontweight='bold', color='#333333')
plt.xlabel('State of Charge (%)', fontsize=12)
plt.ylabel('Voltage (V)', fontsize=12)

plt.xlim(0, 100)
plt.ylim(2.8, 4.4)
plt.xticks(np.arange(0, 101, 10))
plt.grid(color='#cccccc', linestyle='--', linewidth=0.5)

# 5. Highlight
plt.axvspan(20, 80, color='#27AE60', alpha=0.1)
plt.text(50, 3.5, 'Linear Usage Range', ha='center', fontsize=10, color='green')

plt.tight_layout()
plt.savefig('liion_chart.png', dpi=300)
print("Graph saved to liion_chart.png")