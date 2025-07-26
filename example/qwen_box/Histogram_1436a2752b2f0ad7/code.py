import matplotlib.pyplot as plt

# Data
plastic_waste_ppm = [14, 19, 26, 31, 38, 45, 52, 59, 66, 71, 78, 83, 89, 96, 103, 110, 
                     117, 123, 130, 137, 144, 150, 157, 164, 171, 178, 184, 191, 198, 205, 
                     212, 219, 225, 232, 239, 246, 253, 259, 266, 273, 280, 287, 293, 300, 
                     307, 314, 320, 327, 334]

# Create histogram
plt.hist(plastic_waste_ppm, bins='auto', edgecolor='black')

# Labels and title
plt.title('Distribution of Plastic Waste Levels in Ocean Water Samples')
plt.xlabel('Plastic Waste Concentration (ppm)')
plt.ylabel('Frequency')

# Define clipping box
bbox = plt.Bbox([[465, 219], [465 + 600, 219 + 664]])

# Adjust transparency of areas in the histogram that contain the center point of the bounding box
plt.fill_betweenx(range(plt.ylim()[0], plt.ylim()[1]), 0, plastic_waste_ppm, where=bbox, alpha=0.80)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")