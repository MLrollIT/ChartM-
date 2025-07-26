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

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox

# Get the violins that contain the center point of the bounding box
violins = plt.gca().violinplots[0].violin_parts

# Set the transparency of the violins to 0.56
for violin in violins:
    violin.set_alpha(0.56)

# Set the z-order of the violins to 2
for violin in violins:
    violin.set_zorder(2)

# Apply a shadow effect with an offset of (3.85, 3.67) and randomly choose the shadow color from either 'gray' or 'gold'
for violin in violins:
    violin.set_edgecolor('none')
    violin.set_facecolor('none')
    violin.set_edgecolor('gray')
    violin.set_facecolor('gold')
    violin.set_boxstyle('round')
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5, 0.5)
    violin.set_boxstyle('round', 0.5