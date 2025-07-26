from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
"Vehicle Type","2016","2017","2018","2019","2020"
"Sedans",4000,8000,6000,7000,9000
"SUVs",3000,3000,6000,5000,8000
"Electric Vehicles",1000,5000,2000,2500,5000
"Trucks",2500,2000,3000,2000,1000
"Motorcycles",5000,4000,6000,8000,7000
"Hybrids",2000,3000,7000,5000,6000
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['2016'].values, df['2017'].values, df['2018'].values, df['2019'].values, df['2020'].values]
labels = ['2016', '2017', '2018', '2019', '2020']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym="o")

# Set the clipping state of the boxes that contain the center point of the bounding box to True
for box in bp['boxes']:
    box.set_clip_on(True)

# Change the box body's face color to #bcea5d
for patch in bp['boxes']:
    patch.set_facecolor('#bcea5d')

# Set title and labels
ax.set_title('Vehicle Sales Over The Years')
ax.set_xlabel('Years')
ax.set_ylabel('Sales')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], df['Vehicle Type'], loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("Edit_figure.png")