# Required Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Elevation Data
mars_elevation = [1200, 1300, 1100, 1400, 1250, 1350]
venus_elevation = [900, 950, 870, 920, 880, 930]
titan_elevation = [1600, 1550, 1650, 1500, 1620, 1560]

# Creating DataFrame
data = pd.DataFrame({
    'Planet': ['Mars'] * len(mars_elevation) + ['Venus'] * len(venus_elevation) + ['Titan'] * len(titan_elevation),
    'Elevation': mars_elevation + venus_elevation + titan_elevation
})

# Plotting
plt.figure(figsize=(9, 6))
sns.violinplot(x='Planet', y='Elevation', data=data)
plt.title('Planet Surface Elevation Mapping')
plt.xlabel('Planet')
plt.ylabel('Elevation (in meters)')

# Set the clipping box for the violins that contain the center point of the bounding box
bbox = plt.Bbox([[194, 60], [194 + 292, 60 + 611]])
plt.violinplot([mars_elevation, venus_elevation, titan_elevation], positions=[0, 1, 2], widths=0.8, clip_on=False, rasterized=True, showmeans=False, showextrema=False, showmedians=False, bivariate=True, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale_h=1, scale_v=1, scale='linear', scale