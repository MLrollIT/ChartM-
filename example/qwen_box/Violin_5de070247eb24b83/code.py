import pandas as pd
# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Specifying the data
bedrock_elevation = [100, 120, 110, 130, 115, 105, 125, 135, 140, 115]
sandstone_elevation = [200, 180, 190, 210, 220, 230, 240, 200, 210, 195]
limestone_elevation = [300, 280, 270, 290, 305, 295, 310, 320, 315, 300]
shale_elevation = [150, 160, 140, 130, 145, 155, 165, 170, 175, 160]

# Preparing the data for presentation
data = [bedrock_elevation, sandstone_elevation, limestone_elevation, shale_elevation]
layers = ["Bedrock", "Sandstone", "Limestone", "Shale"]

# Creating the plot
plt.figure(figsize=(10,6))
sns.violinplot(data=data)
plt.title('Violin Plot of Geological Layer Elevations')
plt.xlabel('Geological Layers')
plt.ylabel('Elevation in meters')
plt.xticks(ticks=[0, 1, 2, 3], labels=layers)

# Updating the label of the violin that contains the center point of the bounding box
plt.setp(plt.violinplot(data, showmeans=True, showextrema=False), linestyle='dotted')

# Displaying the plot

plt.tight_layout()
plt.savefig("figure.png")