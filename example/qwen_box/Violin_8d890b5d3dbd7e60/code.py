# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
altitude_0_1 = [380, 385, 382, 378, 381, 379, 383, 386, 384, 380]
altitude_1_3 = [372, 370, 375, 373, 376, 371, 368, 374, 372, 377]
altitude_3_5 = [365, 363, 362, 366, 360, 364, 368, 367, 363, 361]
altitude_5_10 = [350, 355, 353, 358, 352, 357, 354, 356, 359, 351]

# Create DataFrame from data
df = pd.DataFrame({
    'CO2 Concentration (ppm)': altitude_0_1 + altitude_1_3 + altitude_3_5 + altitude_5_10,
    'Altitude (km)': ['0-1']*len(altitude_0_1) + 
                     ['1_3']*len(altitude_1_3) + 
                     ['3_5']*len(altitude_3_5) + 
                     ['5_10']*len(altitude_5_10)
})

# Create violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Altitude (km)', y='CO2 Concentration (ppm)', data=df)

# Show the plot
plt.title('Distribution of CO2 Concentration at Different Altitudes')

# Get the bounding box of the center point of the violin plot
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the center point of the bounding box
center_point = bbox.center

# Get the violins that contain the center point of the bounding box
violins = plt.gca().findobj(sns.axisgrid.AxesGrid._violinplot_violins)
violins = [violin for violin in violins if center_point[0] in violin.get_paths()]

# Change the animated state of the violins to False
for violin in violins:
    violin.set_animated(False)

# Set the face color of the violins to #a72daa
for violin in violins:
    violin.set_facecolor('#a72daa')

plt.tight_layout()
plt.savefig("figure.png")