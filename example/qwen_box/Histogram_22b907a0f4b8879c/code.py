import matplotlib.pyplot as plt
import numpy as np

# Given Data
minerals = ['Silica', 'Iron Oxide', 'Aluminum Oxide', 'Calcium Sulfate', 'Magnesium Oxide']
frequency = [43, 29, 18, 35, 22]

# Creating an array with indices of mineral types
x = np.arange(len(minerals))

# Creating the histogram
plt.bar(x, frequency, align='center', alpha=0.7)

# Adding labels
plt.xlabel('Mineral Types')
plt.ylabel('Frequency of Mineral Occurrence')
plt.title('Martian Soil Composition Analysis')

# Displaying mineral names on the x-axis
plt.xticks(x, minerals)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")

# Apply a frosted glass effect to the bars that contain the center point of the bounding box
plt.bar(x[2], frequency[2], alpha=0.6157, edgecolor='#94d5ab', linestyle='--', linewidth=2.9)

# Displaying the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")