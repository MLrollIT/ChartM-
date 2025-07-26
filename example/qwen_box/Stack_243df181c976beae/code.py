import matplotlib.pyplot as plt

# Define years and yield data
years = list(range(2010, 2020))
wheat = [2.5, 2.4, 2.6, 2.3, 2.2, 2.1, 2.0, 1.8, 1.7, 1.5]
rice = [3.2, 3.0, 2.8, 2.7, 2.6, 2.4, 2.3, 2.1, 2.0, 1.8]
maize = [4.0, 3.8, 3.5, 3.3, 3.0, 2.8, 2.5, 2.3, 2.2, 2.0]

# Create stack plot
plt.figure(figsize=(10,7))
plt.stackplot(years, wheat, rice, maize, labels=['Wheat', 'Rice', 'Maize'], alpha=0.7)

# Add labels and title
plt.xlabel('Years')
plt.ylabel('Crop yield (t/ha)')
plt.title('Effects of Climate Change on Global Crop Yields (2010-2019)')
plt.legend(loc='upper right')

# Set animated state of the area that contains the center point of the bounding box to True
plt.gca().collections[0].set_animated(True)

# Adjust z-order of the area to 20
plt.gca().collections[0].set_zorder(20)

# Apply a shadow effect to the area with an offset of (3.13, 3.40) and color of 'gray'
plt.gca().collections[0].set_edgecolor('gray')
plt.gca().collections[0].set_edgeoffset((3.13, 3.40))

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")