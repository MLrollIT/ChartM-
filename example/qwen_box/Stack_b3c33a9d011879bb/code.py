# Import necessary libraries
import matplotlib.pyplot as plt

# Define distance ranges and number of clusters
distance_ranges = ['0-100', '100-300', '300-600', '600-1000', '1000-1500']
num_clusters = [120, 80, 60, 40, 20]

# Convert number of clusters list to 2D list for stackplot function
num_clusters = [[i] for i in num_clusters]

# Define colors for each distance range
colors = ['purple', 'blue', 'green', 'yellow', 'red']

# Generate the stack plot
plt.stackplot(distance_ranges, num_clusters, labels=distance_ranges, colors=colors)

# Define labels and title
plt.xlabel('Distance from Earth (Mpc)')
plt.ylabel('Number of Galaxy Clusters')
plt.title('Galaxy Clusters Distribution in the Observable Universe')

# Display the legend
plt.legend(loc='upper right')

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")