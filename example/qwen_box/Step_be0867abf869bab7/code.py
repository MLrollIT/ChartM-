# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the data
animals = ['Cheetah', 'Gazelle']
cheetah_speeds = [50, 60, 70, 80, 90]
gazelle_speeds = [40, 45, 50, 55, 60]

# Create step plots for cheetah and gazelle speeds
plt.figure(figsize=(8, 6))
plt.step( np.arange(len(cheetah_speeds)), cheetah_speeds, where='mid', label='Cheetah', linestyle='-', linewidth=2)
plt.step( np.arange(len(gazelle_speeds)), gazelle_speeds, where='mid', label='Gazelle', linestyle='-', linewidth=2)

# Add necessary graph components
plt.xlabel('Time Interval')
plt.ylabel('Speed (km/h)')
plt.title('Speed Comparison: Cheetah vs Gazelle')
plt.legend()
# plt.show()
plt.tight_layout()
plt.savefig("figure.png")