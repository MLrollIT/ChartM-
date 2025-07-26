import matplotlib.pyplot as plt
import numpy as np

# Data
data_points = np.array([1, 2, 3, 4, 5])
data1 = np.array([10, 20, 30, 40, 50])
data2 = np.array([5, 10, 15, 20, 25])
data3 = np.array([15, 25, 35, 45, 55])

# Create a Figure and an Axes with matplotlib.pyplot
fig, ax = plt.subplots()

# Stack plot
ax.stackplot(data_points, data1, data2, data3, labels=['Data1', 'Data2', 'Data3'], alpha=0.5)
ax.legend(loc='upper left')

# To convert y axis to percentage
totals = [i+j+k for i,j,k in zip(data1, data2, data3)]
data1_stacked = [i / j * 100 for i,j in zip(data1, totals)]
data2_stacked = [i / j * 100 for i,j in zip(data2, totals)]
data3_stacked = [i / j * 100 for i,j in zip(data3, totals)]
ax.stackplot(data_points, data1_stacked, data2_stacked, data3_stacked, labels=['Data1', 'Data2', 'Data3'], alpha=0.5)


# Set the clipping box for the area that contains the center point of the bounding box
bbox = matplotlib.transforms.Bbox([[4, 3], [4 + 501, 3 + 424]])
ax.clip_on()
ax.set_clip_box(bbox)

# plt.show()
plt.tight_layout()
plt.savefig("figure.png")