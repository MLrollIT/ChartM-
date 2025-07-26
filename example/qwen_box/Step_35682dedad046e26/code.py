import matplotlib.pyplot as plt
import numpy as np

# Define the data
x_values = np.array([100, 500, 1000, 2000, 4000, 6000, 8000, 10000])
y_values = np.array([15, 20, 25, 18, 22, 10, 5, 2])

# Create the plot
plt.figure(figsize=(10, 6))
plt.step(x_values, y_values, where='post')
plt.ylim(0, max(y_values)+5)
plt.xlim(0, max(x_values)+1000)

# Label the axes and the plot
plt.title('Microbial Diversity in Deep-Sea Trenches')
plt.xlabel('Ocean Depth (meters)')
plt.ylabel('Microbial Species Richness')

# Display plot grid
plt.grid(True)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")