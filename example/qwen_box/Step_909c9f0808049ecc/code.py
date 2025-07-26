import matplotlib.pyplot as plt

# Data
years = list(range(1990, 2021))
marathon_times = [2.08, 2.07, 2.06, 2.05, 2.04, 2.03, 2.02, 2.01, 2.00, 1.59, 1.58, 1.57, 1.56, 1.55, 
                  1.54, 1.53, 1.52, 1.51, 1.50, 1.49, 2.10, 2.11, 2.09, 2.08, 2.07, 2.06, 2.05, 2.04, 2.03, 
                  2.02, 2.01]

# Plot
plt.figure(figsize=(10,6))
plt.step(years, marathon_times, where='post')

plt.xlabel('Year')
plt.ylabel('Fastest Marathon Time (hr)')
plt.title('Fastest Marathon Times by Year (1990-2020)')

plt.grid(True)

# Add data point annotations to the step line that contains the center point of the bounding box
bbox = plt.gca().get_position().get_points()
bbox = bbox[0] + 0.5, bbox[1][1]
plt.annotate('1.59', xy=bbox, xycoords='data', fontsize=11, color='#8c79b2')

plt.tight_layout()
plt.savefig("figure.png")