import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd

# Rainfall data for each region
North = [50, 60, 45, 35, 45, 70, 80, 85, 75, 65, 55, 50]
South = [100, 110, 90, 80, 70, 60, 50, 60, 70, 90, 100, 110]
East = [70, 75, 80, 85, 90, 95, 90, 85, 80, 75, 70, 65]
West = [120, 110, 100, 90, 80, 70, 70, 80, 90, 100, 110, 120]

# Creating a dataframe
df = pd.DataFrame({
    'North': North,
    'South': South,
    'East': East,
    'West': West
})

# Changing the structure of dataframe to create violin plot
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['North', 'South', 'East', 'West'])

# Replacing the column names
df_melt.columns = ['Month', 'Region', 'Rainfall']

# Creating violin plot
plt.figure(figsize=(10,7))
sns.violinplot(x="Region", y="Rainfall", inner="quartile", data=df_melt)
plt.title('Seasonal variation in rainfall across four different regions')
plt.tight_layout()
plt.savefig("figure.png")

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox

# Get the center point of the bounding box
center_point = (bbox.x0 + bbox.x1) / 2, (bbox.y0 + bbox.y1) / 2

# Get the violins that contain the center point of the bounding box
violins = plt.gca().violinplots[0].violin_parts

# Set the animated state of the violins to False
for violin in violins:
    if (center_point[0] - violin.get_x() < 0.05) and (center_point[0] - violin.get_x() > -0.05):
        violin.set_animated(False)

plt.savefig("figure.png")