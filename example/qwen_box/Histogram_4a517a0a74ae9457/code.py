import matplotlib.pyplot as plt

# Sizes of Galactic Gas Clouds (in light-years)
sizes = [1000, 1500, 1200, 1350, 1400, 1250, 1300, 1550, 1100,
         1450, 1600, 1150, 1700, 1020, 1800, 1230, 1320, 1270,
         1380, 1420, 1650, 1900, 1120, 1180, 1750, 1080]

# Create histogram
plt.hist(sizes, bins='auto', color='skyblue', edgecolor='black')

# Set Labels and Title
plt.xlabel('Size of Galactic Gas Clouds (in light-years)')
plt.ylabel('Frequency')
plt.title('Distribution of Sizes of Galactic Gas Clouds')

# Add glow effect to bars that contain the center point of the bounding box
bbox = (1400, 0.2, 250, 0.8)
plt.bar([bbox[0]], [bbox[1]], color='skyblue', edgecolor='black', alpha=0.3027321156917125, label='Glow Effect')

# Ensuring all labels are readable
plt.tight_layout()
plt.savefig("figure.png")