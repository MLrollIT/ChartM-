# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare the data
simulations = ['Garden Oasis', 'Enchanted Forest', 'Underwater Paradise']
color_intensities = [
    [8, 5, 7, 6, 9, 8, 6, 7, 5, 6],
    [7, 6, 5, 8, 7, 9, 6, 5, 8, 7],
    [6, 8, 7, 5, 6, 5, 9, 7, 8, 6]
]

# Create a DataFrame
df = pd.DataFrame(dict(zip(simulations, color_intensities))).melt()

# Rename columns
df.columns = ['Simulation', 'Color Intensity']

# Create Violin Plot
plt.figure(figsize=(10,8))
sns.violinplot(x='Simulation', y='Color Intensity', data=df)

# Display the plot
plt.title('Violin plot of the floral color intensities in different VR simulations')

# Change the color of the violins that contain the center point of the bounding box to #0b8c81
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
ax = plt.gca()
ax.set_position(bbox)
ax.set_facecolor('#0b8c81')
ax.set_rasterized(False)

plt.tight_layout()
plt.savefig("figure.png")