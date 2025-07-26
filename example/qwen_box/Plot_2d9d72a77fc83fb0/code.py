from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = 'Year,Phishing Attacks,Malware Attacks,Ransomware Attacks\n2015,5000,7000,2000\n2016,6000,8500,4000\n2017,8200,5000,8000\n2018,9000,6500,5000\n2019,7000,4000,10000\n2020,10000,9000,12000\n2021,9500,8500,14000'
df = pd.read_csv(StringIO(data))

# Plot
fig, ax = plt.subplots()

# Define colors for each line
line_colors = {'Phishing Attacks': 'red', 'Malware Attacks': 'green', 'Ransomware Attacks': 'blue'}

for column in df.columns[1:]:
    ax.plot(df['Year'], df[column], marker='o', linestyle='-.', label=column, linewidth=2.5, color=line_colors[column], markersize=8, alpha=0.7)
    for x, y in zip(df['Year'], df[column]):
        ax.text(x, y, str(y))

# Annotations
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Year')
ax.set_ylabel('Number of Attacks')
ax.set_title('Number of Different Cyber Attacks Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('white')  # Change background color to white
plt.tight_layout()
plt.savefig('myplot.png')

# Modify the object in the chart
bbox = ax.bbox_to_transform(ax.transAxes.transform(((140, 111), (140 + 194, 111 + 805))))
clip_box = matplotlib.transforms.Bbox.from_extents(bbox.xmin, bbox.ymin, bbox.width, bbox.height)
ax.add_artist(ax.clip_path(clip_box))

# Set the edge color of the same lines to the Target_object to #952ace
for line in ax.get_lines():
    line.set_edgecolor('#952ace')

plt.savefig('Edit_figure.png')