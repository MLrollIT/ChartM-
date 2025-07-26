from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

data = {
    'Malaria': (10000, 12000, 5000),
    'HIV/AIDS': (20000, 5000, 15000),
    'Diabetes': (15000, 18000, 8000),
    'Heart Disease': (12000, 25000, 10000),
    'Tuberculosis': (5000, 3000, 10000)
}

years = ["2001", "2006", "2011"]
y = np.arange(len(years)) 
height = 0.15 
multiplier = 0

fig, ax = plt.subplots()

for disease, values in data.items():
    offset = height * multiplier
    bars = ax.barh(y + offset, values, height, label=disease, edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

ax.set_xlabel('Number of Cases')
ax.set_title('Disease cases by year')
ax.set_yticks(y + height * 2)
ax.set_yticklabels(years)
ax.legend(loc='upper right', ncol=1)
ax.invert_yaxis() 
ax.grid(False)  # Disable gridlines
ax.set_facecolor('white')  # Change background to white
plt.tight_layout()
plt.savefig("myplot.png")