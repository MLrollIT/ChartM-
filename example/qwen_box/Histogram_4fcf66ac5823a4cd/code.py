import matplotlib.pyplot as plt

# Dataset
weights = [
    5.2, 6.9, 7.1, 4.8, 8.5, 7.9, 9.2, 6.4, 5.7, 5.3, 8.1, 7.6, 6.3, 8.4, 7.2, 
    6.1, 4.9, 7.5, 7.3, 8.2, 7.8, 6.2, 5.9, 6.5, 5.6, 7.4, 6.6, 9.5, 5.4, 8.9, 
    7.7, 7.0, 6.7, 5.1, 7.8, 6.0, 8.3, 7.6, 9.4, 5.8, 6.8, 5.0, 6.4, 7.5, 7.9, 
    8.6, 7.1, 6.6, 8.7, 7.2, 5.2, 6.3, 8.0, 4.7, 9.9
]

# Create a histogram with 'auto' bins
plt.hist(weights, bins='auto', edgecolor='black')

# Set the title and labels
plt.title('Body Weight Distribution of Feline Friends')
plt.xlabel('Weight (pounds)')
plt.ylabel('Frequency')

# Add grid and adjust layout
plt.grid(True)
plt.tight_layout()

# Save the figure with the specified file name
plt.savefig("figure.png")

# Modify the linewidth of the histogram containing the center point of the bounding box
plt.hist(weights, bins='auto', edgecolor='black', linewidth=0.87)

# Set the snap state to True for the same points
plt.hist(weights, bins='auto', edgecolor='black', snap=True)

# Save the modified figure with the specified file name
plt.savefig("figure.png")