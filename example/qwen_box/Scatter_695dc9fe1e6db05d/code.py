# Importing necessary libraries
import matplotlib.pyplot as plt

# Data
microbial_size = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
microbial_abundance = [750, 600, 450, 400, 350, 300, 250, 200, 150, 100]

# Creating scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(microbial_size, microbial_abundance, c='blue')

# Setting the title and labels
plt.title("Relationship between Microbial Size and its Abundance")
plt.xlabel("Microbial Size (µm)")
plt.ylabel("Microbial Abundance (cells/mL)")

# Adjusting the size and color of the scatter points
plt.scatter(3.0, 400, s=46, c="#799e08")

# Displaying the plot

plt.tight_layout()
plt.savefig("figure.png")