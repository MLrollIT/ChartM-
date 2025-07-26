import matplotlib.pyplot as plt

# Depth zones for the x-axis
depth_zones = ['Shallow', 'Mid', 'Deep']

# Number of species for different depth zones in different regions
atlantic = [500, 300, 100]
pacific = [450, 250, 80]
indian = [400, 200, 70]
arctic = [350, 150, 50]

# Initial plot
plt.figure(figsize=(10, 7))

# Adding the values to the stack plot
plt.stackplot(depth_zones, atlantic, pacific, indian, arctic, labels=['Atlantic','Pacific', 'Indian', 'Arctic'], alpha=0.8)

# Adding legend at the upper left corner
plt.legend(loc='upper left')

# Labels for x-axis and y-axis
plt.xlabel("Depth Zones")
plt.ylabel("Number of Species")

# Title of the plot
plt.title("Oceanic Biodiversity Stack Plot")

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")