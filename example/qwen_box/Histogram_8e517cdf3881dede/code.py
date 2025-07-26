# Required Libraries
import matplotlib.pyplot as plt

# Data
rock_diameters = ["10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90-100"]
frequency = [15, 12, 9, 7, 5, 3, 2, 1, 1]

# Creating histogram
plt.figure(figsize=[10,8])
plt.bar(rock_diameters, frequency,color='blue', alpha=0.7)

# Labels
plt.xlabel("Rock Diameter Ranges (in cm)", fontsize=12)
plt.ylabel("Frequency of Rock Diameters", fontsize=12)
plt.title("Histogram of Rock Diameters encountered by Alien Rover", fontsize=16)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")