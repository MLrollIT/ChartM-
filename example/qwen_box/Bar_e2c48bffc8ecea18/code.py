from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Recycling Rate": [60, 50, 65, 74, 58, 70]
}

df = pd.DataFrame(data)

# Set colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

fig, ax = plt.subplots()
bars = ax.bar(df["City"], df["Recycling Rate"], color=colors, edgecolor='black')

# Set title, x and y axis labels with modified font sizes
ax.set_title("Recycling Rate in Different Cities", fontsize=20)
ax.set_xlabel("City", fontsize=15)
ax.set_ylabel("Recycling Rate (%)", fontsize=15)

# Set tick labels font size
ax.tick_params(axis='both', which='major', labelsize=12)

# Add grid and set background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate the data value on the chart
ax.bar_label(bars)

# Save the figure with adjusted layout
plt.tight_layout()
plt.savefig("myplot.png")