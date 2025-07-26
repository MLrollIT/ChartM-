# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Defining the dataset
altitudes = ['Altitude 1000 ft', 'Altitude 2000 ft', 'Altitude 3000 ft','Altitude 4000 ft','Altitude 5000 ft']
energy_levels = [[50, 55, 52, 57, 60, 49, 53, 58, 62, 56],
[57, 61, 59, 64, 67, 55, 58, 63, 69, 60],
[62, 66, 64, 70, 73, 61, 65, 71, 75, 65],
[68, 72, 70, 77, 80, 66, 69, 76, 82, 71],
[75, 79, 77, 84, 87, 73, 78, 85, 90, 79]]

# Formatting the data for seaborn
data = {altitude: energy for altitude, energy in zip(altitudes, energy_levels)}

# Create a DataFrame from the data
import pandas as pd
df = pd.DataFrame(data)

# Create violin plot
plt.figure(figsize=(10,6))
sns.violinplot(data=df)
plt.title('Magical Energy Levels at Different Altitudes')
plt.xlabel('Altitude')
plt.ylabel('Magical Energy Levels (Mana)')

# Set the fill pattern of the violin enclosed by the bounding box to a hatch pattern, and change its color to #559e6d
plt.fill_betweenx(range(len(altitudes)), [0] * len(altitudes), [len(energy_levels[0])] * len(altitudes), color='#559e6d', hatch='/', alpha=0.5)

plt.tight_layout()
plt.savefig("figure.png")