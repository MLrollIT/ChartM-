import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
eventide = [1200, 1180, 1220, 1215, 1190, 1175, 1225, 1205]
quasarus = [1350, 1360, 1370, 1340, 1335, 1355, 1365, 1345]
singulon = [1400, 1390, 1385, 1410, 1380, 1405, 1395, 1375]

# Combine all data into a list of tuples with category
data = [('Eventide', freq) for freq in eventide] + [('Quasarus', freq) for freq in quasarus] + [('Singulon', freq) for freq in singulon]

# Transform your data into DataFrame (DataFrame is better to visualize with seaborn)
df = pd.DataFrame(data, columns=['Black Hole', 'Frequency'])

# Visualize the violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Black Hole', y='Frequency', data=df)
plt.title('Gravitational Wave Frequencies')

# Set the clipping state of the violins that contain the center point of the bounding box to False
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
plt.gca().violinplot([eventide, quasarus, singulon], showmeans=True, showextrema=False, showmedians=False, widths=0.6, clip_on=False, linewidth=2.21, bbox_to_anchor=bbox)

plt.tight_layout()
plt.savefig("figure.png")