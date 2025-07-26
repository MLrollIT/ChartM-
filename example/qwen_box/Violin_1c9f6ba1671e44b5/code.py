import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary to hold our data
data = {
    "Bullfrog": [1.8, 3.2, 2.9, 2.5, 2.7, 2.1, 2.4, 2.8, 1.9, 2.6],
    "Red-Eyed Tree Frog": [1.2, 1.4, 1.3, 1.1, 1.5, 1.7, 1.6, 1.2, 1.3, 1.4],
    "Poison Dart Frog": [0.9, 0.8, 1.1, 0.7, 0.9, 1.0, 0.8, 0.6, 0.5, 1.0],
    "Glass Frog": [1.6, 1.5, 1.7, 1.4, 1.6, 1.3, 1.8, 1.5, 1.4, 1.7],
    "Leopard Frog": [2.1, 2.2, 1.9, 2.0, 1.8, 2.3, 1.7, 2.1, 1.9, 2.2]
}

# Create labels and dataset in the form suitable for seaborn
labels, data_set = [*zip(*data.items())]

# Create a figure and ax instance
fig, ax = plt.subplots()

# Make the violin plot
sns.violinplot(ax=ax, data=data_set, palette='pastel')

# Set the title and labels
ax.set_title('Jumping Distances of Different Frog Breeds')
ax.yaxis.grid(True)
ax.set_xlabel('Frog Breed')
ax.set_ylabel('Jumping Distance')
plt.xticks(range(len(data)), labels)

# Set the transparency of the violins that contain the center point of the bounding box to 0.51
ax.collections[0].set_alpha(0.51)

# Adjust the clip box of this portion to a bounding box defined by the bottom-left corner coordinates (134, 140), with a width of 287 and a height of 220, following the matplotlib.transforms.Bbox format
bbox = matplotlib.transforms.Bbox([[134, 140], [134 + 287, 140 + 220]])
ax.collections[0].set_clip_box(bbox)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")