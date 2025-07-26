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

# Displaying the plot

plt.tight_layout()
plt.savefig("figure.png")

# Modify the color of the violins that contain the center point of the bounding box to #3aaf73
# Apply a stroke to these violins with a linewidth of 4.23 and a foreground color of #746165
# Use 'Edit_figure.png' as file name when you when you save the figure in the code.
# The code for drawing the chart based on matplotlib(this code has nothing to do with boungding box).
# Please note that it is necessary to ensure that only the parts indicated by the Instruction are modified in the rendered chart image, while other elements or parts should remain unchanged.