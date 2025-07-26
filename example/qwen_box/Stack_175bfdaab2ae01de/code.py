import matplotlib.pyplot as plt
import numpy as np

years = ['2017', '2018', '2019', '2020']
airlines = ['Airline A', 'Airline B', 'Airline C', 'Airline D']

# Ratings data
on_time = np.array([[3.5, 4.1, 3.8, 4.3],
                    [4.2, 3.9, 4.0, 4.1],
                    [4.0, 4.3, 3.9, 4.0],
                    [3.9, 3.7, 4.2, 4.4]])

cust_service = np.array([[4.0, 3.8, 4.3, 4.2],
                         [3.5, 4.1, 4.0, 4.4],
                         [4.2, 3.9, 3.8, 4.1],
                         [4.1, 4.2, 4.1, 4.3]])

bag_handling = np.array([[3.9, 4.0, 3.8, 4.2],
                         [3.7, 4.1, 4.0, 4.3],
                         [4.2, 4.3, 3.9, 4.0],
                         [3.6, 4.2, 4.1, 4.4]])

# Plotting
fig, ax = plt.subplots()

ax.stackplot(years, on_time, cust_service, bag_handling, labels=airlines)
ax.legend(loc='upper left')
plt.xlabel("Years")
plt.ylabel("Customer Satisfaction Ratings")
plt.title("Customer Satisfaction Ratings for different airlines")
plt.tight_layout()

# Change the face color of the area that contains the center point of the bounding box to #4c6e36
bbox = ax.bbox_to_anchor([0.5, 0.5, 0.1, 0.1])
bbox_patch = plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor='#4c6e36', alpha=0.5)
ax.add_patch(bbox_patch)

plt.savefig("figure.png")