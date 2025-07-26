# Necessary libraries
import matplotlib.pyplot as plt

# Data
ice_thickness = [1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4, 5.7, 6.0, 6.3, 6.6, 6.9, 7.2, 7.5, 7.8, 8.1, 8.4, 8.7, 9.0, 9.3, 9.6, 9.9]
frequency = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Creating Histogram
plt.hist(ice_thickness, weights=frequency, bins=20, alpha=0.7, color='b')

# Labels and Title
plt.title('Arctic Ice Thickness Over the Past Decade')
plt.xlabel('Ice Thickness (meters)')
plt.ylabel('Frequency of Measurements')

# Show plot
plt.tight_layout()
plt.savefig("figure.png")

# Adjusting line width of the histogram that contains the center point of the bounding box
plt.plot([4.5, 4.5], [0, 20], color='black', linewidth=2.27, linestyle='-', alpha=0.7, visible=False)