import matplotlib.pyplot as plt
import numpy as np

# Data points for fruits, ripening time intervals, and frequencies
fruits = ['Mango', 'Papaya', 'Pineapple']
ripening_time_intervals = ['1-3 days', '3-5 days', '5-7 days', '7-9 days', '9-11 days']
frequencies = np.array([[15, 20, 25, 30, 15],
                        [10, 25, 40, 30, 20],
                        [5, 15, 25, 30, 35]])

# Plotting the histogram
fig, ax = plt.subplots()
width = 0.2
x = np.arange(len(ripening_time_intervals))

for i, fruit in enumerate(fruits):
    ax.bar(x + width * i, frequencies[i], width=width, label=fruit)

# Labeling the axes
ax.set_xlabel('Ripening Time Intervals (days)')
ax.set_ylabel('Frequency')

# Setting the title
ax.set_title('Ripening Time Distribution of Tropical Fruits')

# Adding a legend
ax.legend(loc='upper right')

# Adjusting the x-axis tick labels
ax.set_xticks(x + width * (len(fruits) - 1) / 2)
ax.set_xticklabels(ripening_time_intervals)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")