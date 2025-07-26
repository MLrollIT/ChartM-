from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data 
data = StringIO("""Year,Coal,Oil,Natural Gas
2005,4500,5000,3800
2006,4600,5100,3900
2007,4450,5100,4000
2008,4350,5500,4200
2009,4300,5300,4250
2010,4250,5200,4300
2011,4300,5600,4400
2012,4200,5800,4500
""")
df = pd.read_csv(data)

# Plot
fig, ax = plt.subplots()

for column in df.columns[1:]:
    ax.plot(df['Year'], df[column], marker='o', linestyle='-.', linewidth=2, color='red', markersize=5, alpha=0.7, label=column)
    for x, y in zip(df['Year'], df[column]):
        ax.text(x, y, str(y))

# Annotations
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Year')
ax.set_ylabel('Energy Production (in Million Tonnes)')
ax.set_title('Energy Production from Different Sources Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')
plt.tight_layout()
plt.savefig('myplot.png')

# Update label and snap state
for line in ax.lines:
    line.set_label('A new Label')
    line.set_snap(True)