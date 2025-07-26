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

# Add a glowing outline to the bars that contain the center point of the bounding box
bbox = (70, 20, 75, 25)
plt.bar([bbox[0]], [bbox[1]], color='black', edgecolor='black', linewidth=0.98, alpha=0.75, label='Center Point')
plt.bar([bbox[0]], [bbox[1]], color='black', edgecolor='black', linewidth=0.98, alpha=0.75, label='Center Point')

# Show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")