# Required Libraries
import matplotlib.pyplot as plt 

# Temperature Intervals
temp_intervals = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]

# Frequencies
frequencies = [5, 9, 14, 18, 20, 16, 12, 8, 6, 2]

# Plot Histogram using the plt.hist() method
plt.figure(figsize=(10, 6)) # Setting the figure size
plt.hist(temp_intervals, weights=frequencies, bins=len(temp_intervals), color='blue', edgecolor='black') 

# Setting the chart title and labels
plt.title('Distribution of Fluid Temperature levels in a Jet Engine System', fontsize=15)
plt.xlabel('Temperature (in Kelvin)', fontsize=12)
plt.ylabel('Frequency of Observations', fontsize=12)

# Ensuring the plot displays
plt.tight_layout()
plt.savefig("figure.png")

# Add a dashed outline around the bars that contain the center point of the bounding box
for i in range(len(temp_intervals)):
    if temp_intervals[i] == 1400:
        plt.bar(temp_intervals[i], frequencies[i], color='blue', edgecolor='black', linewidth=0.69, hatch='//', alpha=0.80)