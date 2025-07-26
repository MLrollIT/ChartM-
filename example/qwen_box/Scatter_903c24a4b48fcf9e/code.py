import matplotlib.pyplot as plt

# Data
temperature = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28] # degrees Celsius
successful_settlements = [15, 20, 30, 40, 50, 60, 70, 80, 85, 75, 60] # percentage

# Create scatter plot
plt.scatter(temperature, successful_settlements)

# Add title and labels to the axes
plt.title('Impact of Ocean Temperatures on Coral Breeding Success')
plt.xlabel('Ocean Temperature (°C)')
plt.ylabel('Successful Coral Larval Settlements (%)')

# Modify the color and transparency of the points that contain the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.get_points()
bbox[0] = (0.5, 0.5)
bbox[1] = (0.5, 0.5)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = plt.gca().bbox_to_transform(bbox)
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.get_points()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1] + 0.05)
bbox = bbox.tolist()
bbox[0] = (bbox[0][0] - 0.05, bbox[0][1] - 0.05)
bbox[1] = (bbox[1][0] + 0.05, bbox[1][1]