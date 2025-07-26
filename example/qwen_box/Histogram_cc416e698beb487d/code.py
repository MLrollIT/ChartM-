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

# Set the clipping box for the bars that contain the center point of the bounding box
bbox = plt.Bbox([[83, 355], [83 + 668, 355 + 399]])
plt.bar([83, 83 + 668], [1, 1], clip_on=False, alpha=0.75, edgecolor='black', width=668, height=399, animated=False)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")