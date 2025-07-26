from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Prepare data
data = {
    "Time Period": ["Morning", "Afternoon", "Evening", "Night", "Early Morning", "Late Night", "Midnight"],
    "App Usage": [120, 80, 150, 90, 70, 200, 50],
    "Call Duration": [15, 20, 25, 10, 5, 30, 8],
    "Data Consumption": [2.5, 3.0, 2.0, 1.5, 1.0, 3.5, 1.2]
}
df = pd.DataFrame(data)

# Create subplots
fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([df["App Usage"], df["Call Duration"], df["Data Consumption"]],
                patch_artist = True, notch = True, vert = 0, widths = 0.5,
                labels = ["App Usage", "Call Duration", "Data Consumption"])

colors = ['#0000FF', '#00FF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Add annotations
for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    ax.annotate(f'Median: {y}', (x, y), textcoords="offset points", xytext=(10,-10), ha='center', fontsize=8, color='black')

# Add title and labels
ax.set_title('Usage Statistics')
ax.set_xlabel('Metrics')
ax.set_ylabel('Values')

# Remove grid and set background color to white
ax.grid(False)
ax.set_facecolor('white')  # Background color changed to white

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")