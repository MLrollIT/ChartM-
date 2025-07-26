import matplotlib.pyplot as plt

# X values: Frequency array (0 to 1.2 with a step size of 0.1)
x_values = [i*0.1 for i in range(13)]

# Y values: Corresponding frequencies mentioned 
y_values = [25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.figure(figsize=(10, 5))  # Create a new figure with a specific size (optional)

# Creating histogram using plt.hist() function
plt.hist(x_values[:-1], 
         bins=x_values, 
         weights=y_values, 
         alpha=0.7, 
         color='blue', 
         edgecolor='black')

plt.title('Distribution of Electron Densities in Molecular Structure') # Adding title to the plot

plt.xlabel('Electron Density (e/Å³)') # Adding x-label
plt.ylabel('Frequency of Electron Densities') # Adding y-label

plt.grid(True) # Adding a grid

plt.tight_layout()
plt.savefig("figure.png")