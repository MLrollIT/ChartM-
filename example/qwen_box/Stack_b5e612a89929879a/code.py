import matplotlib.pyplot as plt

# Time Intervals
time = [1, 2, 3, 4, 5]

# Galactic Nebula Formation Stages
gas_accumulation   = [10, 15, 20, 25, 30]
compression       = [5, 10, 15, 20, 25]
igniting_stars    = [2, 5, 10, 15, 20]

# Create a stackplot
plt.stackplot(time, gas_accumulation, compression, igniting_stars, labels=['Gas Accumulation','Compression','Igniting Stars'], colors=['r','g','b'])

plt.xlabel('Time Intervals')
plt.ylabel('Units')
plt.title('Stages of Galactic Nebula Formation Simulation')

# Add a legend
plt.legend(loc='upper left')

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")

# Modify the area that contains the center point of the bounding box
bbox = plt.gca().collections[0].get_paths()[0].vertices
bbox[2] = [bbox[2][0], bbox[2][1], 0.442, 0.442]
plt.gca().collections[0].set_paths([plt.Polygon(bbox)])

plt.tight_layout()
plt.savefig("Edit_figure.png")