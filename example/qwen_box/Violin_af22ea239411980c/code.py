import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the dataset
region_a = [2.3, 2.6, 2.1, 2.8, 2.5, 3.0, 2.7, 2.4, 2.9, 2.2]
region_b = [1.9, 1.7, 1.5, 1.8, 2.0, 1.6, 1.4, 1.9, 2.1, 1.6]
region_c = [3.5, 3.2, 3.6, 3.8, 3.3, 3.1, 3.9, 3.7, 3.4, 3.0]
region_d = [4.2, 4.5, 4.1, 4.3, 4.6, 4.0, 4.4, 4.7, 4.8, 4.2]

# Create a data structure that includes list name (the region)
nebula_masses = [('region_a', mass) for mass in region_a] + \
                [('region_b', mass) for mass in region_b] + \
                [('region_c', mass) for mass in region_c] + \
                [('region_d', mass) for mass in region_d]

# Transform into DataFrame
df = pd.DataFrame(nebula_masses, columns=['Region', 'Simulated Nebula Masses'])

# Create a violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Region", y="Simulated Nebula Masses", data=df)

# Show the plot with title and labels
plt.title('Violin Plots of Simulated Nebula Masses in Different Galactic Regions')

# Get the bounding box of the violin plot
bbox = plt.gca().get_position()

# Adjust the transform of the box part of the violin that contains the center point of the bounding box
bbox.x0 += 0.05
bbox.width *= 0.9

# Apply the adjusted transform to the violin plot
plt.gca().set_position(bbox)

plt.tight_layout()
plt.savefig("figure.png")