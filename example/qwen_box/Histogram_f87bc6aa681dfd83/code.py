import matplotlib.pyplot as plt

# Heights in inches (converted from feet and inches to inches)
heights_inches = [
    60, 61, 62, 63, 64, 65, 66, 67, 67, 68, 69, 70, 71, 72, 72, 73, 74, 74, 75, 75, 76, 76, 77, 78, 79, 79, 80, 81, 81, 82, 82, 82, 83, 83, 84, 84, 85, 86, 86, 87, 87, 88, 89, 89, 90, 90, 91, 92, 93, 96, 96, 97
]

# Create a histogram of the heights
plt.hist(heights_inches, bins=range(59, 99,2), edgecolor='black', alpha=0.75)
plt.title('Comic Book Characters Height Distribution')
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.grid(True)

# Add a shadow effect to the bars that contain the center point of the bounding box
bbox = (67, 70, 72, 75)
shadow_offset = (4.00, 3.90)
shadow_color = 'gold'
linewidth = 4.58
foreground_color = '#c364b5'

# Get the bar objects
bars = plt.gca().containers[0]
for bar in bars:
    if bar.get_bbox().contains(bbox):
        bar.set_facecolor(shadow_color)
        bar.set_edgecolor('black')
        bar.set_linewidth(linewidth)
        bar.set_foreground(foreground_color)
        bar.set_zorder(2)

# Show the plot
# plt.show()
plt.tight_layout()
plt.savefig("figure.png")