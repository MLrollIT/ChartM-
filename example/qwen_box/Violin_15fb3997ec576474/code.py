# Necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Specifying data
age_groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70+']
deaths = [[10, 12, 15, 8, 14, 13, 9, 11, 10, 12, 13, 8, 15, 16, 14, 13, 12, 11, 10, 9],
          [5, 7, 6, 9, 8, 7, 6, 4, 9, 12, 7, 6, 8, 5, 10, 8, 9, 7, 6, 7],
          [15, 12, 10, 13, 16, 18, 19, 14, 17, 15, 12, 10, 13, 16, 18, 19, 14, 17, 15, 12],
          [21, 20, 23, 22, 20, 19, 25, 24, 22, 21, 20, 23, 22, 20, 19, 25, 24, 22, 21, 20],
          [18, 15, 16, 20, 22, 21, 19, 20, 18, 15, 16, 20, 22, 21, 19, 20, 18, 15, 16, 18],
          [25, 24, 22, 20, 25, 23, 22, 21, 24, 22, 20, 25, 23, 22, 21, 24, 22, 20, 25, 23],
          [18, 17, 16, 19, 21, 20, 18, 22, 17, 16, 19, 21, 20, 18, 22, 17, 16, 19, 21, 20],
          [30, 32, 29, 27, 31, 33, 28, 29, 30, 32, 29, 27, 31, 33, 28, 29, 30, 32, 29, 30]]

# Transforming the data into a suitable format
data = []
for age_group, death_values in zip(age_groups, deaths):
    for value in death_values:
        data.append([age_group, value])

# Converting data to pandas DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=['Age Group', 'Number of Deaths'])

# Creating the violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Age Group', y='Number of Deaths', data=df)
plt.title('Distribution of Deaths Across Age Groups')
plt.tight_layout()

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the coordinates of the center point of the bounding box
center_point = bbox.center

# Get the violins that contain the center point of the bounding box
violins = plt.gca().violinplot.get_paths()

# Set the color of the violins that contain the center point of the bounding box to #3b6e71
for violin in violins:
    if violin.contains_point(center_point):
        violin.set_facecolor('#3b6e71')
        violin.set_edgecolor('#3b6e71')
        violin.set_linestyle('dashdot')

plt.savefig("figure.png")