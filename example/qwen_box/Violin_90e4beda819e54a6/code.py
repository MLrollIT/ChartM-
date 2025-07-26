import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary of data
caverns = {'Territory A': [50, 55, 60, 65, 70, 75, 80, 85, 90],
           'Territory B': [35, 40, 45, 50, 55, 60, 65, 70, 75],
           'Territory C': [70, 75, 80, 85, 90, 95, 100, 105, 110],
           'Territory D': [45, 50, 55, 60, 65, 70, 75, 80, 85],
           'Territory E': [60, 65, 70, 75, 80, 85, 90, 95, 100],
           'Territory F': [30, 35, 40, 45, 50, 55, 60, 65, 70]}

# Convert the dictionary into a list of tuples
data = [(k, v) for k, vals in caverns.items() for v in vals]

# Create a DataFrame
df = pd.DataFrame(data, columns=['Territory', 'Cavern Depth'])

# Create a violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Territory', y='Cavern Depth', data=df, palette='viridis')
plt.title('Distribution of Cavern Depths in Different Moon Territories')

# Set the snap state of the violins that include the center point of the bounding box to True
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.savefig("figure.png")