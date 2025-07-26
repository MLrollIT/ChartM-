import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
Inlet = [50, 52, 48, 55, 53, 49, 51, 54, 52, 50, 45, 47, 44, 46, 43, 48, 42, 45, 49, 46]
Compressor = [200, 205, 210, 198, 202, 207, 195, 200, 203, 208, 190, 195, 198, 192, 198, 205, 187, 193, 199, 196]
Combustor = [700, 710, 695, 705, 690, 715, 685, 700, 690, 705, 680, 692, 675, 685, 670, 695, 665, 680, 685, 692]
Turbine = [400, 410, 395, 405, 390, 415, 385, 400, 395, 410, 390, 395, 390, 392, 385, 400, 382, 390, 395, 398]

# Combining the data
data = [Inlet, Compressor, Combustor, Turbine]
labels=['Inlet', 'Compressor', 'Combustor', 'Turbine']

# Creating violin plot
plt.figure(figsize=(10,6))
sns.violinplot(data=data)
plt.xticks([0, 1, 2, 3], labels)

plt.title('Fluid Dynamics in a Jet Engine')
plt.ylabel('Velocity (m/s)')
plt.xlabel('Engine Sections')

plt.tight_layout()
plt.savefig("figure.png")

# Disable animated state of violins that contain the center point of the bounding box
for i in range(len(data)):
    if i == 1:
        plt.violinplot(data[i], showmeans=False, showextrema=False, showmedians=False, widths=0.5, linewidth=4.65)
    else:
        plt.violinplot(data[i], showmeans=False, showextrema=False, showmedians=False, widths=0.5, linewidth=4.65)

plt.tight_layout()
plt.savefig("figure.png")