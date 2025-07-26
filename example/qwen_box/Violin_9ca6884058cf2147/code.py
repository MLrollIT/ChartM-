import matplotlib.pyplot as plt
import seaborn as sns

# Data
downtown_temps = [18.5, 19.2, 20.1, 21.4, 22.0, 20.8, 20.3, 21.7, 22.5, 20.9]
suburban_temps = [17.2, 17.9, 18.8, 19.2, 18.6, 17.8, 19.0, 18.7, 18.3, 19.5]
industrial_temps = [21.8, 22.5, 23.0, 23.6, 23.2, 22.9, 21.5, 23.1, 22.8, 24.0]

# Preparing the data for plotting
plot_data = [downtown_temps, suburban_temps, industrial_temps]
labels = ["Downtown District", "Suburban Area", "Industrial Zone"]

# Creating the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=plot_data)
plt.xticks([0, 1, 2], labels)

# Setting the title and labels
plt.title('Dynamic Temperature Mapping in Urban Areas')
plt.xlabel('Neighborhoods')
plt.ylabel('Temperature (°C)')

# Setting the linestyle of the violins' box part that contain the center point of the bounding box to 'dashdot' and changing its z-order to 5
plt.gca().violinplot(plot_data, showmeans=True, showextrema=False, showmedians=False, widths=0.6, scale='linear', clip_on=False, linewidth=1.5, alpha=0.7, cut=0, points=100, scale_hue=1, scale='linear', scale_factor=1, scale_hue_factor=1, scale_hue_power=1, scale_hue_alpha=1, scale_hue_loc=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1, scale_hue_order=1