import matplotlib.pyplot as plt

# Time Intervals
time_intervals = ['T1', 'T2', 'T3', 'T4', 'T5']

# Concentrations in ppm
carbon_dioxide = [200, 180, 150, 130, 100]
water_vapor = [120, 110, 100, 90, 80]
nitrogen_oxides = [30, 35, 40, 45, 50]
sulfur_dioxide = [10, 8, 6, 4, 2]

# Create stackplot
plt.figure(figsize=(10,6))
plt.stackplot(time_intervals, carbon_dioxide, water_vapor, nitrogen_oxides, sulfur_dioxide, labels=['Carbon Dioxide','Water Vapor','Nitrogen Oxides','Sulfur Dioxide'])

# Customize the plot
plt.legend(loc='upper right')
plt.title('Vibrant Flame Dynamics in Combustion Processes')
plt.xlabel('Time Intervals')
plt.ylabel('Concentrations (ppm)')

# Set animated state of the area containing the center point of the bounding box to False
plt.gca().collections[3].set_animated(False)

# Change linestyle and color of the area
plt.gca().collections[3].set_linestyle('-.')
plt.gca().collections[3].set_color('red')

# Show plot
plt.tight_layout()
plt.savefig("figure.png")