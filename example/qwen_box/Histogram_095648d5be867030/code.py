import matplotlib.pyplot as plt

# Goals and their frequencies
goals = list(range(0, 11))
matches = [3, 8, 12, 9, 5, 2, 1, 0, 0, 0, 1]

# Create the histogram
plt.hist(goals, weights=matches, bins=range(11), alpha=0.7, rwidth=0.85, color='blue', edgecolor='black')

# Set the title and labels
plt.title('Football Team Performance Analysis')
plt.xlabel('Number of Goals Scored')
plt.ylabel('Frequency of Matches')

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform((0.35, 0.25, 0.65, 0.75))

# Get the bars that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()[0].vertices

# Set the stroke line width to 2.07 and the foreground color to #1abbd1
for bar in bars:
    if bbox.contains(bar):
        bar.set_edgecolor('#1abbd1')
        bar.set_linewidth(2.07)

# Change the line color of these bars to #7fab17
for bar in bars:
    if bbox.contains(bar):
        bar.set_facecolor('#7fab17')

# Display the histogram
plt.tight_layout()
plt.savefig("figure.png")