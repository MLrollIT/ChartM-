import matplotlib.pyplot as plt
import seaborn as sns

# Data
depths_A = [1200, 1250, 1260, 1225, 1230, 1245, 1215, 1255]
depths_B = [1400, 1375, 1420, 1385, 1360, 1435, 1390, 1415]
depths_C = [1550, 1520, 1565, 1580, 1535, 1570, 1545, 1595]
depths_D = [1320, 1305, 1340, 1365, 1350, 1335, 1310, 1380]

# Prepare data for seaborn
data = [depths_A, depths_B, depths_C, depths_D]
labels = ['Area A', 'Area B', 'Area C', 'Area D']

# Create a new figure
plt.figure(figsize=(10,6))

# Create violin plot
sns.violinplot(data=data, palette='viridis')

# Set x-axis labels
plt.xticks(range(4), labels)

# Set title and labels
plt.title("Seafloor Mapping using Sonar Data")
plt.ylabel("Depth (in meters)")
plt.xlabel("Seafloor Area")

# Set the label of the violins that contain the center point of the bounding box to 'A new Label'
plt.text(1.5, 1450, 'A new Label', fontsize=12, ha='center', va='center')

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")