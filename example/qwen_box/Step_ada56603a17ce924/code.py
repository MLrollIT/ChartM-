import matplotlib.pyplot as plt
import numpy as np

# Months 
Months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Sales data
sales_A = np.array([5000, 5200, 4800, 5500, 6200, 7100, 6900, 7300, 8000, 7800, 8200, 8500])
sales_B = np.array([3000, 3200, 3500, 3800, 4000, 4300, 4800, 4700, 5000, 5100, 5400, 5600])
sales_C = np.array([1500, 1600, 1800, 1900, 2200, 2400, 2600, 2800, 2900, 3000, 3200, 3300])

# Plotting data
plt.figure(figsize=(10,7)) # Change the figure size according to your requirement
plt.step(Months, sales_A, where='mid', label='Category A')
plt.step(Months, sales_B, where='mid', label='Category B')
plt.step(Months, sales_C, where='mid', label='Category C')

plt.xlabel('Months')
plt.ylabel('Sales in USD')
plt.title('Sales performance of various product categories')
plt.legend(loc='best')
plt.grid()

plt.tight_layout()
plt.savefig("figure.png")

# Add a glowing endpoint effect to each segment of the step line that contains the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.get_window_extent().transformed(plt.gca().transAxes.inverted())
bbox = bbox.get_points()

for i in range(len(Months)):
    if bbox[i, 0] < 0.5 and bbox[i, 0] > 0.45:
        plt.plot(Months[i], sales_A[i], 'o', markersize=4.1, color='#bb8596')
        plt.plot(Months[i], sales_B[i], 'o', markersize=4.1, color='#bb8596')
        plt.plot(Months[i], sales_C[i], 'o', markersize=4.1, color='#bb8596')