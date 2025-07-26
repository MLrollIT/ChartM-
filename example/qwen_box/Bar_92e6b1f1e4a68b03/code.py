from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
"TV Show Type","Popularity Index"
"Drama",80
"Reality",120
"Comedy",60
"Documentary",140
"Action",90
"Horror",70
"Sci-Fi",130
""")

df = pd.read_csv(data, sep=",")
tv_show_type = df["TV Show Type"].values
popularity_index = df["Popularity Index"].values

fig, ax = plt.subplots()

# Define the color gradient (from light blue to dark blue)
colors = plt.cm.Blues(np.linspace(0.3, 1, len(tv_show_type)))

# Draw the bar chart with the new color gradient and grey edgecolor
bars = ax.bar(tv_show_type, popularity_index, align='center', color=colors, edgecolor='grey')

# Annotate the data value on the bar
ax.bar_label(bars)

ax.set_xlabel('TV Show Type')
ax.set_ylabel('Popularity Index')
ax.set_title('Popularity Index of Different TV Show Types')

ax.grid(True)
ax.set_facecolor('lightgray')

# Set the animated state of the bars that contain the center point of the bounding box to False
for bar in bars:
    if bar.get_x() + bar.get_width() / 2 == 120:
        bar.set_animated(False)

plt.tight_layout()
plt.savefig("myplot.png")