import pandas as pd
# Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset for Depths (in kilometers)
depths = [4.2, 3.8, 4.5, 3.9, 3.7, 4.0, 4.3, 4.1, 3.6, 4.4, 3.5, 4.2, 4.6, 3.8, 4.0]

# Create the violin plot
plt.figure(figsize=(10,6)) # adjust the size as per your needs
sns.violinplot(y=depths)

# Format the plot
plt.title('Violin plot of Ocean Floor Topography')
plt.ylabel('Depth (in kilometers)')

# Modify the transparency of the violin that contains the center point of the bounding box to 0.56
violin = plt.gca().violinplot(depths, showmeans=False, showextrema=False, showmedians=False)
violin['bodies'][0].set_alpha(0.56)

plt.tight_layout()
plt.savefig("figure.png")