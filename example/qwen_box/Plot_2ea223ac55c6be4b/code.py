from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a DataFrame using the provided csv data
data = {
    "Year": [2016, 2017, 2018, 2019],
    "Books Published": [12000, 12500, 15000, 10000],
    "E-books Published": [4000, 6000, 8000, 12000],
    "Revenue": [20000000, 23000000, 30000000, 25000000]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plotting "Books Published" line
l1, = ax.plot(df["Year"], df["Books Published"], color="blue", linewidth=2, linestyle='-', marker='o', markersize=8, label="Books Published")

# Plotting "E-books Published" line
l2, = ax.plot(df["Year"], df["E-books Published"], color="green", linewidth=2, linestyle='--', marker='v', markersize=8, label="E-books Published")

# Plotting "Revenue" line
l3, = ax.plot(df["Year"], df["Revenue"]/1000000, color="red", linewidth=2, linestyle='-.', marker='s', markersize=8, label="Revenue (in millions)")

# Setting up labels, title, and legends
ax.set_xlabel('Year')
ax.set_ylabel('Number of Books / Revenue')
ax.set_title('Publishing Statistics Over The Years')
ax.legend()

# Annotating each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Books Published', 'E-books Published', 'Revenue']):
    y = line.get_ydata()[-1]
    ax.annotate(name,
                xy=(1,y),
                xytext=(6,0), 
                xycoords=ax.get_yaxis_transform(),
                textcoords="offset points",
                size="large",
                color=line.get_color(),
                ha="right")

# Adding grid and setting background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Set the clipping state of the lines that contain the center point of the bounding box to True
l1.set_clipping(True)
l2.set_clipping(True)
l3.set_clipping(True)

# Change the color of these lines to #4693dd
l1.set_color('#4693dd')
l2.set_color('#4693dd')
l3.set_color('#4693dd')

plt.tight_layout()
plt.savefig("myplot.png")