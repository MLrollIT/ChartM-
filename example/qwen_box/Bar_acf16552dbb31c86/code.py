from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
data = {'Country': ['USA', 'China', 'UK', 'India', 'Australia'],
        '2016': [45, 110, 35, 80, 20],
        '2017': [52, 120, 32, 85, 40],
        '2018': [35, 60, 31, 95, 24]}

df = pd.DataFrame(data)

countries = df['Country'].values
years = ['2016', '2017', '2018']

fig, ax = plt.subplots()

barWidth = 0.25
r1 = np.arange(len(df['2016']))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

bars1 = ax.bar(r1, df['2016'], color='b', width=barWidth, edgecolor='grey', label='2016')
bars2 = ax.bar(r2, df['2017'], color='y', width=barWidth, edgecolor='grey', label='2017')
bars3 = ax.bar(r3, df['2018'], color='g', width=barWidth, edgecolor='grey', label='2018')

ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)
ax.bar_label(bars3, padding=3)

ax.set_title('Country Wise Data')
ax.set_xlabel('Countries', fontweight='bold')
ax.set_ylabel('Values', fontweight='bold')
ax.set_xticks([r + barWidth for r in range(len(df['2016']))])
ax.set_xticklabels(countries)
ax.legend()

ax.grid(True)
ax.set_facecolor("lightgray")

# Set the linestyle of the bars that contain the center point of the bounding box to '-.'
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.65, 0.65])
bbox = ax