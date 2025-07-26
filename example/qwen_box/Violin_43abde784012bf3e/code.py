import pandas as pd
# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Area measurements of tumor regions for each patient.
patient_1 = [5.2, 4.8, 5.0, 5.1, 4.9, 5.3, 5.1, 4.7, 5.2, 4.8]
patient_2 = [6.5, 6.3, 6.7, 6.4, 6.2, 6.6, 6.3, 6.8, 6.5, 6.7]
patient_3 = [7.1, 7.3, 7.0, 7.2, 7.4, 7.1, 7.3, 7.0, 7.2, 7.4]

# Consolidate all measurements and corresponding patient labels into lists.
areas = patient_1 + patient_2 + patient_3
patients = ['Patient 1']*len(patient_1) + ['Patient 2']*len(patient_2) + ['Patient 3']*len(patient_3)

# Create a DataFrame from this data.
data = pd.DataFrame({'Patient': patients, 'Tumor Region Area (mm²)': areas})

# Create the violin plot.
plt.figure(figsize=(10,6))
sns.violinplot(x='Patient', y='Tumor Region Area (mm²)', data=data)
plt.title('Tumor Region Areas Identified in Histopathological Imaging Analysis')

# Change the line color of the violins that contain the center point of the bounding box to #007bfb, and set the line style to 'dotted' for those same points.
violin = plt.gca().violinplot(data, showmeans=True, showextrema=False)
for patch in violin['bodies']:
    patch.set_edgecolor('#007bfb')
    patch.set_linestyle('dotted')

plt.tight_layout()
plt.savefig("figure.png")