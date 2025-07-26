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

# Change the line color of the bars that contain the center point of the bounding box to #b89d41
plt.bar(x[2], frequency[2], color='#b89d41', align='center', alpha=0.7)