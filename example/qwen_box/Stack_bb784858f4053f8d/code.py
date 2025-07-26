import matplotlib.pyplot as plt

# positions along the DNA strand
positions = [1, 2, 3, 4, 5]

# counts of each nucleotide base pair at each position
adenine = [15, 18, 20, 22, 25]
thymine = [20, 22, 25, 28, 30]
cytosine = [10, 12, 15, 18, 20]
guanine = [5, 8, 10, 12, 15]

# create a figure and a set of subplots
fig, ax = plt.subplots()

# stackplot
ax.stackplot(positions, adenine, thymine, cytosine, guanine, labels=['Adenine (A)','Thymine (T)','Cytosine (C)','Guanine (G)'])

# legend
ax.legend(loc='upper left')

# labels
plt.xlabel('Position along the DNA strand')
plt.ylabel('Count of each nucleotide base pair')
plt.title('Microscopic Analysis of DNA Structure')


# Set the clipping box for the areas that contain the center point of the bounding box to a defined rectangle with the bottom-left corner at (175, 168), a width of 196, and a height of 135, following the matplotlib.transforms.Bbox pattern.
bbox = plt.Bbox([[175, 168], [175 + 196, 168 + 135]])
ax.set_clip_path(bbox)

# Enable the snap state for the areas by setting it to True for the same coordinates.
ax.set_snap(True, bbox)

plt.tight_layout()
plt.savefig("figure.png")