from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
data = StringIO("""
Platform,Year 1,Year 2,Year 3,Year 4,Year 5,Year 6,Year 7,Year 8,Year 9
Facebook,5000,5500,3000,3500,4000,6000,6500,3000,3500
Twitter,3000,3500,4000,3000,2500,2000,1500,1000,500
Instagram,2000,4500,5000,5500,5000,4500,4000,8500,8000
Snapchat,1000,2000,3000,2000,1000,800,600,400,200
LinkedIn,2000,2500,3000,3500,4000,4500,5000,5500,6000
""")
df = pd.read_csv(data)

# Plotting the data
fig, ax = plt.subplots()

platforms = ['Facebook', 'Twitter', 'Instagram', 'Snapchat', 'LinkedIn']
# Updated color palette for better contrast and visual appeal
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
linestyles = ['-', '--', '-.', ':', '-']
markers = ['o', 's', 'v', '^', 'd']

for i, platform in enumerate(platforms):
    ax.plot(df.columns[1:], df.loc[i, df.columns[1:]],
            marker=markers[i], color=colors[i], linestyle=linestyles[i], linewidth=2, markersize=6, alpha=0.7, label=platform)
    for j, txt in enumerate(df.loc[i, df.columns[1:]]):
        ax.annotate(txt, (df.columns[1:][j], txt))

ax.set_xlabel('Year')
ax.set_ylabel('Number of Users')
ax.set_title('Number of Users per Social Media Platform Over the Years')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

# Set the marker face color of the lines that contain the center point of the bounding box to #8fc8ba
bbox = ax.bbox_to_transform((0.5, 0.5))
ax.plot(df.columns[1:], df.loc[i, df.columns[1:]],
        marker=markers[i], color=colors[i], linestyle=linestyles[i], linewidth=2, markersize=6, alpha=0.7, label=platform, transform=bbox, markerfacecolor="#8fc8ba")

ax.annotate('5500', (df.columns[1:][j], df.loc[i, df.columns[1:]][j]), transform=bbox, color="#8fc8ba")

plt.tight_layout()
plt.savefig('myplot.png')