from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO("""
Genre,Popularity
Action,10
Romance,50
Comedy,20
Horror,30
""")

df = pd.read_csv(data)
df = df.sort_values('Popularity')

fig, ax = plt.subplots()

# Draw the bar chart
bars = ax.barh(df['Genre'], df['Popularity'], color="skyblue", edgecolor='black')

# Add the data value on the bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 5 points horizontal offset
                textcoords="offset points",
                ha='left', va='center')

ax.set_xlabel('Popularity')
ax.set_ylabel('Genre')
ax.set_title('Popularity of Different Movie Genres')
ax.grid(True)
ax.set_facecolor('lightgray')

# Set the fill pattern of the bars that contain the center point of the bounding box to '.', and change their edge color to '#511097'
for bar in bars:
    if bar.contains((25, 25)):
        bar.set_facecolor('.')
        bar.set_edgecolor('#511097')

plt.tight_layout()
plt.savefig("myplot.png")