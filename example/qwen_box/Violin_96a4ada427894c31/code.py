# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Dataset
evs_emissions = [78, 80, 76, 79, 75, 74, 77, 81, 82, 85, 83]
gps_emissions = [170, 175, 172, 168, 173, 169, 171, 174, 176, 170, 173]

# Combine the data
data = evs_emissions + gps_emissions
types = ['EVs']*len(evs_emissions) + ['GPs']*len(gps_emissions)

# Create a DataFrame
df = pd.DataFrame({'Type': types, 'Carbon Emissions (g/km)': data})

# Create the violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='Type', y='Carbon Emissions (g/km)', data=df)
plt.title('Comparison of Carbon Emissions (g/km) of EVs vs GPs')
plt.tight_layout()

# Get the bounding box of the violin plot
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the coordinates of the center point of the bounding box
center_point = bbox.get_points()[0]

# Get the violins that contain the center point of the bounding box
violins = plt.gca().findobj(sns.axisgrid.AxesGrid._asg)
violins = [violin for violin in violins if center_point[0] in violin.get_paths()]

# Adjust the transparency and color of the violins
for violin in violins:
    violin.set_alpha(0.47)
    violin.set_facecolor('#773685')

plt.savefig("Edit_figure.png")