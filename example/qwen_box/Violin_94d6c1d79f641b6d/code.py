import pandas as pd
# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data
North_America = [150, 175, 160, 180, 165, 170, 185, 200, 190, 195]
South_America = [120, 130, 140, 125, 135, 145, 128, 132, 138, 142]
Europe = [100, 110, 105, 115, 108, 112, 120, 118, 125, 122]
Africa = [80, 85, 82, 88, 87, 84, 90, 86, 92, 89]
Asia = [70, 75, 72, 78, 73, 77, 71, 76, 74, 79]
Australia = [60, 65, 62, 68, 63, 67, 61, 66, 64, 69]

data = [North_America, South_America, Europe, Africa, Asia, Australia]
labels = ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia']

# Create a figure instance
plt.figure(figsize=(10, 6))

# Create violinplot
sns.violinplot(data=data)

# Giving the plot a title
plt.title('Distribution and Size Variation of Impact Craters')

# Giving labels to the x and y axes
plt.xlabel('Region')
plt.ylabel('Crater Diameter (in meters)')

# defining the labels for the xaxis
plt.xticks(range(len(labels)), labels)

# Modify the color of the violin that contains the center point of the bounding box to #cf0548 and set its transparency to 0.65
violin = plt.gca().violinplot(data, labels=labels, showmeans=True, showextrema=False, showmedians=False)
violin['bodies'][0].set_facecolor('#cf0548')
violin['bodies'][0].set_alpha(0.65)

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")