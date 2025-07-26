from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data
data = StringIO("""
Diets,2015,2020
Vegan,30,90
Keto,60,40
Intermittent Fasting,20,100
Paleo,70,30
Gluten Free,50,70
""")
df = pd.read_csv(data)

# Plot
fig, ax = plt.subplots()

for column in df.columns[1:]:
    ax.plot(df['Diets'], df[column], marker='o', linestyle='--', label=column, linewidth=2.0, color='blue', markersize=6, alpha=0.7)
    for x, y in zip(df['Diets'], df[column]):
        ax.text(x, y, str(y))

# Annotations
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Diets')
ax.set_ylabel('Number of People')
ax.set_title('Popularity of Diets in 2015 and 2020')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')
plt.tight_layout()
plt.savefig('myplot.png')

# Modify the shape of the data points for the line that contains the center point of the bounding box to 'square'
for line in ax.lines:
    if line.get_label() == '2020':
        line.set_marker('square')
plt.savefig('Edit_figure.png')