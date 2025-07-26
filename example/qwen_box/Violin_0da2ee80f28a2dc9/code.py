# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
LEO = [10, 12, 15, 11, 14, 13, 12, 16, 11, 10, 15, 14, 13, 12]
MEO = [8, 11, 9, 10, 12, 8, 9, 10, 11, 10, 12, 8, 9, 10]
GEO = [6, 7, 5, 8, 6, 7, 5, 8, 7, 6, 5, 8, 7, 6]

data = pd.DataFrame(list(zip(LEO+MEO+GEO, ['LEO']*len(LEO) + ['MEO']*len(MEO) + ['GEO']*len(GEO))), 
                    columns=['Size (cm)', 'Orbit'])

# Create violin plot
plt.figure(figsize=(9, 6))
sns.violinplot(x='Orbit', y='Size (cm)', data=data)

# Set title and labels
plt.title('Space Debris Size Distribution at Different Orbital Altitudes')
plt.xlabel('Orbital Altitudes')
plt.ylabel('Size of Debris (in cm)')

# Modify the linewidth and linestyle of the violins that contain the center point of the bounding box
for violin in plt.gca().violinplots()[0]:
    if violin.get_label() == 'MEO':
        violin.set_edgecolor('black')
        violin.set_linewidth(3.67)
        violin.set linestyle('dashdot')

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")