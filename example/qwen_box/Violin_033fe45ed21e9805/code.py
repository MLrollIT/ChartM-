import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# depths of underwater caves in different oceans
pacific_ocean = [45, 50, 48, 52, 47, 46, 49, 51, 50, 48]
atlantic_ocean = [35, 40, 38, 42, 36, 39, 37, 43, 41, 39]
indian_ocean = [55, 60, 58, 62, 57, 56, 59, 61, 60, 58]

# compile data into a list of lists
data = [pacific_ocean, atlantic_ocean, indian_ocean]

# create figure and axes
fig, ax = plt.subplots()

# create violin plot
sns.violinplot(data=data, ax=ax)

# set title and labels
ax.set_title('Depth Distributions of Underwater Caves in Different Oceans')
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean'])
ax.set_ylabel('Depth (in meters)')

# hide lines in the violin that is associated with the center point of the bounding box
violin = ax.collections[0]
violin.set_edgecolor('none')
violin.set_facecolor('none')

# set z-order to 6 for the same violin's box part
violin.set_zorder(6)

# add shadow effect to the violin's box part
violin.set_edgecolor('none')
violin.set_facecolor('none')
violin.set_edgecolor('blue')
violin.set_facecolor('blue')
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle('round', 0.1, 0.1)
violin.set_boxstyle