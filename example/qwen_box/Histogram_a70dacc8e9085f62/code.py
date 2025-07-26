# First, we import the necessary library for data visualization - matplotlib.pyplot
import matplotlib.pyplot as plt

# Next, we establish our data. 
# The depths of the underwater features (our bins for the histogram) are stored in bin_ranges.
# The corresponding frequencies of these depth measurements are stored in frequency.
bin_ranges = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
frequency = [15, 23, 32, 27, 18, 12, 8, 5, 2]

# We then create a new figure for the plot with a specified size.
plt.figure(figsize=(10, 6))

# The hist() function is called to create the histogram. 
# We use the bin_ranges (minus the last item) as the data, the full bin_ranges for the bins, and the corresponding frequencies as the weights.
# The edgecolor parameter sets the color of the line between bins, and the alpha parameter sets the transparency.
plt.hist(bin_ranges[:-1], bins=bin_ranges, weights=frequency, edgecolor='black', alpha=0.7)

# We label our x and y-axes and give our histogram a title.
plt.xlabel('Depth of underwater features (meters)')
plt.ylabel('Frequency of Depth Measurements')
plt.title('Histogram of Seafloor Mapping Sonar Data')

# Finally, we insert a grid for easier visualization and display the plot.
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("figure.png")