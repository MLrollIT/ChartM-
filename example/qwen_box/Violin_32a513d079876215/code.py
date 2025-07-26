# Required Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data 
temp_25 = [18, 21, 19, 22, 20, 19, 21, 20, 19, 22, 20, 19, 20, 21, 20, 19, 21, 19, 20, 21]
temp_30 = [21, 23, 22, 24, 23, 22, 23, 22, 24, 23, 23, 22, 23, 24, 22, 23, 22, 23, 24, 22]
temp_35 = [20, 19, 22, 19, 20, 21, 19, 21, 19, 22, 19, 20, 19, 21, 19, 21, 20, 21, 19, 22]

temps = ['25°C']*len(temp_25) + ['30°C']*len(temp_30) + ['35°C']*len(temp_35)
heights = temp_25 + temp_30 + temp_35

# Plot
plt.figure(figsize=(10,6))
sns.violinplot(x=temps, y=heights)
plt.title('Impact of Temperature Conditions on plant growth')
plt.xlabel('Temperature Conditions')
plt.ylabel('Plant height (cm)')
plt.tight_layout()

# Get the bounding box of the violin that contains the center point
bbox = plt.gca().get_position().bounds

# Create a new figure with the same size as the original
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Draw the violin plot with the desired hatch pattern and color
sns.violinplot(x=temps, y=heights, ax=ax, inner="quartile", color="#8f8cfa", linewidth=1, alpha=0.7, cut=0)
ax.set_title('Impact of Temperature Conditions on plant growth')
ax.set_xlabel('Temperature Conditions')
ax.set_ylabel('Plant height (cm)')
ax.set_position(bbox)

# Save the figure
plt.savefig("figure.png")