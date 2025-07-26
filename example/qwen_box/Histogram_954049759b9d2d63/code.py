# Importing necessary libraries
import matplotlib.pyplot as plt

# Data for the histogram
microbe_abundance = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
frequency = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

# Create the histogram
fig, ax = plt.subplots()
ax.hist(microbe_abundance, weights=frequency, bins=10, color='c', edgecolor='black')

# Get the bounding box of the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), fig=fig)

# Adjust the clipping state of the bars that contain the center point of the bounding box to False
for bar in ax.containers[0]:
    if bar.get_bbox().contains(bbox):
        bar.set_clip_on(False)
        bar.set_linestyle('dashed')

# Set the title and labels
ax.set_xlabel('Oceanic Microbe Abundance Levels per ml')
ax.set_ylabel('Frequency of Samples with Microbe Abundance Levels')
ax.set_title('Distribution of Oceanic Microbe Abundance Levels')

# Save the figure
plt.tight_layout()
plt.savefig("Edit_figure.png")