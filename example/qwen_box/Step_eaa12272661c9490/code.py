# importing matplotlib library
import matplotlib.pyplot as plt

# years data
years = [2015, 2016, 2017, 2018, 2019]

# population count data
population = [8500, 9200, 9600, 10200, 11000] 

# creating the plot
plt.step(years, population, where='post')

# add title and labels to the plot
plt.xlabel('Years')
plt.ylabel('Population Count')
plt.title('Population data over years')

# updating the marker edge color for the points that contain the center point of the bounding box to #310564, and ensuring their rasterized state is set to True
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.get_window_extent().transformed(plt.gca().transAxes.inverted())
bbox = bbox.get_points()
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] + (bbox[1] - bbox[0]) / 2
bbox = bbox[0] +