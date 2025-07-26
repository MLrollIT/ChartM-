from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = StringIO("""
TV Show Type,2017,2018,2019,2020,2021
Drama,45,60,55,85,60
Comedy,50,80,75,85,50
Reality,60,45,70,50,55
Documentary,30,35,40,60,45
Talk Show,40,70,80,50,60
""")
df = pd.read_csv(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan', 'magenta']
markers = ['.', 'o', 'v', '^', 's']

# Plot
fig, ax = plt.subplots()
for i in range(len(df)):
    ax.plot(df.columns[1:], df.iloc[i, 1:], 
            linestyle=choice(linestyles), 
            color=colors[i], 
            marker=markers[i], 
            markersize=10, 
            alpha=0.7, 
            label=df.iloc[i, 0])
    
    for j in range(1, len(df.columns)):
        ax.annotate(df.iloc[i, 0], 
                    (df.columns[j], df.iloc[i, j]))

ax.set_title('TV Show Types Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.legend(title='TV Show Type:')
ax.grid(True)

# Change the background color to white
fig.set_facecolor('white') # This line was modified

# Increase the line thickness of the plot that contains the center point of the bounding box to 1.797
bbox = ax.bbox_to_anchor((0.5, 0.5), which='center')
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], bbox_points[0][1] + 1.797)
bbox.set_points(bbox_points)

plt.tight_layout()
plt.savefig('myplot.png')