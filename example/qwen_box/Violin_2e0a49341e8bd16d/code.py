code:
import pandas as pd
# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Microbial data for each site
site_A = [200, 180, 220, 210, 190, 195, 205, 215, 190, 200]
site_B = [150, 160, 170, 165, 175, 155, 145, 180, 185, 170]
site_C = [120, 130, 110, 140, 125, 135, 115, 130, 145, 120]

# Combine the different site data into one list
data = [site_A, site_B, site_C]
# Give names to the datasets
names = ["Site A", "Site B", "Site C"]

# Create a violin plot
sns.violinplot(data=data)

# Customize the axis labels
plt.xlabel('Sites')
plt.ylabel('Microbial Counts (in cells/ml)')
plt.xticks([0, 1, 2], names)

# Title of the plot
plt.title('Microbial Abundance in Martian Underground Water Samples')

# Modify the color of the violin that contains the center point of the bounding box to #005c60
sns.violinplot(data=data, inner="point", color="#005c60")

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")