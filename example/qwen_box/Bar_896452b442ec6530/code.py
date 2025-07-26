from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Genre,Popularity
Rock,80
Pop,85
Country,70
Jazz,40
Classical,60
Hip-Hop,90
Electronic,75
R&B,65
""")
df = pd.read_csv(data)

genres = df['Genre'].values
popularity = df['Popularity'].values

fig, ax = plt.subplots()

# Create bars
bars = ax.bar(genres, popularity, color='skyblue', edgecolor='black')

# Add title, labels and legend
ax.set_title("Popularity of Different Music Genres")
ax.set_xlabel("Music Genres")
ax.set_ylabel("Popularity")
ax.legend(['Popularity'])

# Add grids on the background
ax.grid(True)

# Set the face color to a light color
ax.set_facecolor('lightgray')

# Add data value on top of each bar
ax.bar_label(bars)

# Save chart as a png file
plt.tight_layout()
plt.savefig("myplot.png")