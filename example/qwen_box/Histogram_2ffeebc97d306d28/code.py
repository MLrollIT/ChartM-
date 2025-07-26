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

# Add a shadow effect to the bars that contain the center point of the bounding box
bbox = (3.61, 3.92)
shadow_offset = (3.61, 3.92)
shadow_color = 'gray'
line_width = 2.84

# Get the patches of the bars that contain the center point of the bounding box
patches = plt.gca().patches
for patch in patches:
    if patch.get_bbox().center() == bbox:
        patch.set_facecolor('none')
        patch.set_edgecolor('none')
        patch.set_linewidth(line_width)
        patch.set_alpha(0.7)
        patch.set_zorder(10)
        patch.set_path_effects([plt.PathEffects.withStroke(linewidth=line_width, foreground=shadow_color)])

# Display the histogram
plt.tight_layout()
plt.savefig("figure.png")