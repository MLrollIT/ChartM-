# Import necessary libraries
import matplotlib.pyplot as plt

# Dataset With Alpha Helix Lengths
alpha_helix_lengths = [4.5, 7.2, 9.1, 12.3, 15.6, 18.2, 21.0, 24.5, 27.8, 30.2, 33.1, 36.7, 39.4, 
                       42.0, 45.5, 48.3, 51.6, 55.0, 58.7, 62.1, 65.6, 68.9, 71.5, 74.2, 77.8, 80.4, 
                       83.2, 86.6, 89.3, 92.1, 95.5, 98.4, 101.0, 104.5, 107.3, 110.2, 113.6, 116.7, 
                       119.3, 122.0, 125.6, 128.4, 131.0, 134.5, 137.3, 140.2, 143.6, 146.7, 149.3, 152.0, 155.6]

# Create the histogram
plt.hist(alpha_helix_lengths, bins=10, edgecolor='black')

# Set the title and labels
plt.title('Distribution of Alpha Helix Lengths in Protein Structures')
plt.xlabel('Length of Alpha Helix (Angstroms)')
plt.ylabel('Frequency')

# Modify the linewidth of the bar that contains the center point of the bounding box to 3.09 and change its line color to #15035a
plt.bar(alpha_helix_lengths[1], alpha_helix_lengths[1], color='#15035a', linewidth=3.09)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")