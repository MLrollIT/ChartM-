# Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Dataset
systolic_bp = [120, 122, 118, 125, 130, 132, 128, 134, 120, 115, 136, 128, 126, 124, 127, 130, 133, 129, 126, 122]
diastolic_bp = [80, 85, 82, 90, 88, 86, 85, 92, 81, 79, 88, 84, 86, 83, 84, 89, 90, 87, 85, 82]
labels = ['Systolic']*len(systolic_bp) + ['Diastolic']*len(diastolic_bp)
values = systolic_bp + diastolic_bp

data = pd.DataFrame({'Blood Pressure Type': labels, 'Value (mmHg)': values})

# Violin plot 
plt.figure(figsize=(10,6))
sns.violinplot(x='Blood Pressure Type', y='Value (mmHg)', data=data)
plt.title('Blood Pressure Distribution')
plt.tight_layout()
plt.savefig("figure.png")

# Modify the color of the violin that contains the center point of the bounding box to #78dd28
violin = plt.gca().violinplot(data, positions=[0.5], showmeans=True, showmedians=False, showextrema=False)
violin['bodies'][0].set_facecolor('#78dd28')