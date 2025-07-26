from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Year,Anxiety Disorders,Depression
2012,7.8,6.6
2013,7.4,6.3
2014,7.1,5.9
2015,6.8,8.2
2016,6.5,7.8
2017,6.2,7.5
2018,5.9,7.1
2019,5.6,6.9
2020,5.2,11.4
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Anxiety Disorders'].values, df['Depression'].values]
labels = ['Anxiety Disorders', 'Depression']
colors = ['#1f77b4', '#aec7e8']  # Changed colors to different shades of blue

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Prevalence of Anxiety Disorders and Depression Over The Years')
ax.set_xlabel('Mental Health Conditions')
ax.set_ylabel('Prevalence (%)')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")