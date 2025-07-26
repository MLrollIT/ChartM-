# Import necessary library
import matplotlib.pyplot as plt

# Specify the growth stages
growth_stages = ['Seedling', 'Sapling', 'Mature', 'Old']

# Provide the heights for each tree at different growth stages
oak_heights = [0.5, 1.5, 5.0, 10.0]
willow_heights = [0.3, 1.0, 4.0, 8.5]
pine_heights = [0.2, 0.8, 3.0, 7.0]

# Create a stack plot
plt.stackplot(growth_stages, oak_heights, willow_heights, pine_heights, labels=['Oak', 'Willow', 'Pine'])

# Add labels and title
plt.xlabel('Growth Stages')
plt.ylabel('Tree Heights (m)')
plt.title('Mystical Forest Growth Exploration')

# Add a legend
plt.legend(loc='upper left')

# Modify the edge color of the area that contains the center point of the bounding box to #ebe1d8, and set its alpha blending mode to 0.8244
bbox = plt.gca().bbox_to_transform((0.3, 0.3, 0.4, 0.4))
plt.gca().add_patch(plt.Rectangle((0.3, 0.3), 0.4, 0.4, edgecolor='#ebe1d8', alpha=0.8244))

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")