import matplotlib.pyplot as plt

# Crater Depths (m)
depths = [103, 117, 126, 139, 147, 155, 162, 175, 182, 194, 206, 215, 223, 236, 244, 253, 262, 279,
          288, 297, 306, 312, 325, 334, 345, 356, 363, 375, 384, 392, 403, 414, 423, 435, 446, 456,
          463, 475, 484, 495, 506, 517, 525, 536, 546, 553, 565, 576, 584, 595, 606, 617, 624, 636]

# Create the Histogram
plt.hist(depths, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)

# Label the plot
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Crater Depth (m)')
plt.ylabel('Frequency')
plt.title('Distribution of Crater Depths on Martian Surface')

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform([0.5, 0.5, 0.5, 0.5])

# Get the bars that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()
bars = [bar for bar in bars if bar.contains_point(bbox.transform([0.5, 0.5]))]

# Set the face color and line color of the bars
for bar in bars:
    bar.set_facecolor('#ba5184')
    bar.set_edgecolor('#53f154')

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")