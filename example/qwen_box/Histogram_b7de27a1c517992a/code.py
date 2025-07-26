import matplotlib.pyplot as plt

# Define wait time intervals and their frequencies
time_intervals = ['0 - 5 minutes', '5 - 10 minutes', '10 - 15 minutes', '15 - 20 minutes', '20 - 25 minutes', '25 - 30 minutes']
frequencies = [40, 55, 30, 15, 10, 5]

plt.figure(figsize=(10,6))

# Create histogram
plt.bar(time_intervals, frequencies, color='blue', alpha=0.7)

# Add labels
plt.xlabel('Wait time intervals')
plt.ylabel('Frequency')
plt.title('Distribution of customer wait times at a popular restaurant')

# Modify the linestyle of the bars that contain the center point of the bounding box to 'dashdot', and update their line color to #051926.
bbox = dict(boxstyle='round', fc='white', ec='black', lw=1)
for i in range(len(time_intervals)):
    if time_intervals[i] == '5 - 10 minutes' or time_intervals[i] == '15 - 20 minutes':
        plt.bar(time_intervals[i], frequencies[i], color='#051926', alpha=0.7, edgecolor='black', linestyle='dashdot', linewidth=1.5, bottom=frequencies[:i].sum())

# Display the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")