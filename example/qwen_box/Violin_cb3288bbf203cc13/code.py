# Library imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
crop_types = ["Wheat", "Maize","Rice","Soybeans","Barley"]
data = [[2.5, 2.3, 2.6, 2.4, 2.7, 2.8, 2.9, 2.7, 2.8, 2.6],
        [3.8, 4.0, 3.9, 3.7, 3.6, 3.8, 3.9, 4.2, 4.1, 3.9],
        [6.2, 6.4, 6.5, 6.3, 6.6, 6.4, 6.8, 6.7, 6.6, 6.5],
        [2.0, 2.2, 2.1, 1.9, 2.0, 2.1, 2.2, 2.3, 2.1, 2.0],
        [2.8, 2.9, 3.0, 2.8, 2.7, 3.1, 3.0, 2.9, 3.1, 2.8]]

# Figure initialization
plt.figure(figsize=(10, 6))

# Creating violin plot
sns.violinplot(data=data)

# Setting x and y axes labels
plt.xlabel('Crops')
plt.ylabel('Yield (metric tons per hectare)')

# Setting x-axis tick labels to the crop names
plt.xticks(list(range(len(crop_types))), crop_types)

# Setting plot title
plt.title('Effects of Climate Change on Global Crop Yields (Last Decade)')

# Get the bounding box of the violin plot
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the center point of the bounding box
center_point = bbox.center

# Set the animated state of the box part of the violin that contains the center point of the bounding box to True
violin = plt.gca().collections[0]
violin.set_animated(True)

# Update its transformation to align with the figure's coordinate system
violin.set_transform(plt.gcf().transFigure)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")