from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Provided data
data = {
    "Genre": ["Horror", "Comedy", "Drama"],
    "2010": [100, 200, 150],
    "2020": [180, 170, 300]
}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Create figure and axes
fig, ax = plt.subplots()

# Set the background color of the chart to white
ax.set_facecolor('white')

# Plotting data
for index, row in df.iterrows():
    ax.scatter([2010, 2020], [row['2010'], row['2020']], label=row['Genre'], marker='o')

# Annotating data values above the point on the chart figure
for i, txt in enumerate(df['2010']):
    ax.annotate(txt, (2010, df['2010'][i]))
for i, txt in enumerate(df['2020']):
    ax.annotate(txt, (2020, df['2020'][i]))

# Setting labels, title and grid
ax.set_xlabel('Year')
ax.set_ylabel('Values')
ax.set_title('Scatter Chart')

# Change the color of the grid lines to light blue
ax.grid(True, color='lightblue', linestyle='--', linewidth=0.5)

# Adding legend
ax.legend()

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")