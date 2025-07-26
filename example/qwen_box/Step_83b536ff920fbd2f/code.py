import matplotlib.pyplot as plt
import numpy as np

# Define the levels of engagement and conversion rates
levels_of_engagement = ['Low', 'Moderate', 'High', 'Very High', 'Extreme']
conversion_rates = np.array([25, 40, 55, 70, 85])

# Enlarge the plot size
plt.figure(figsize=(10,7))

# Generate the stair plot
plt.step(levels_of_engagement, conversion_rates, where='mid')

# Label the axes
plt.xlabel("Level of Social Media Engagement")
plt.ylabel("Customer Conversion Rate (%)")
plt.title("Stair Plot of Social Media Engagement vs Conversion Rate")

# Change the edge color of the points that contain the center point of the bounding box to #083d38, and set the marker size for those same points to 13.07.
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 0.05, bbox[1] + 0.05, bbox[2] - 0.1, bbox[3] - 0.1]
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], 'k', linewidth=2)
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], 'k', linewidth=2)
plt.plot([