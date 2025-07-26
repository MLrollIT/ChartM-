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

# Set the picker state of the violins that contain the center point of the bounding box to True
plt.gcf().axes[0].violin_collection.set_picker(True)

# Apply a stroke with a line width of 2.985 and a foreground color of #74cc06 to the violins that contain the center point of the bounding box
plt.gcf().axes[0].violin_collection.set_edgecolor('#74cc06')
plt.gcf().axes[0].violin_collection.set_linewidth(2.985)

# Display the plot
plt.title('Violin plot of the floral color intensities in different VR simulations')

plt.tight_layout()
plt.savefig("figure.png")