from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSV data in a dictionary
data_dict = {"Service": ["Online Shopping", "Digital Payment", "Streaming Services", "Cloud Storage"],
             "Usage": [80, 60, 100, 120]}

# Convert dictionary to dataframe
df = pd.DataFrame(data_dict)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize =(10, 7))

# Create a box plot
bp = ax.boxplot(df['Usage'], patch_artist = True, notch = True, vert = 0, widths = 0.5, sym = 'r+')

# Change the face color of the box to light green
bp['boxes'][0].set_facecolor('#90ee90')

# Set the background color of the chart
ax.set_facecolor('lightgray')

# Add a grid
ax.grid(True)

# Set the title and labels
ax.set_title('Usage of Different Services')
ax.set_xlabel('Service')
ax.set_ylabel('Usage')

# Annotate data value on the chart
for i, v in enumerate(df['Usage']):
    ax.text(v + 3, i + 1, str(v), color='blue', fontweight='bold')

# Add a legend
ax.legend([bp["boxes"][0]], ['Usage'], loc='upper right')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')