from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given CSV data
data = {'Year': [2014, 2015, 2016, 2017, 2018, 2019],
        'AI_Research': [500, 480, 460, 550, 530, 510],
        'Robotics': [700, 680, 660, 750, 730, 710],
        'Neural_Networks': [1000, 900, 800, 1050, 950, 925],
        'Data_Mining': [1200, 1100, 1000, 1250, 1150, 1125]}
df = pd.DataFrame(data)

# Set up the figure and axis
fig, ax = plt.subplots()

# Define a monochrome blue color scheme
blue_shades = ['#003f5c', '#2f4b7c', '#665191', '#a05195']

ax.plot('Year', 'AI_Research', data=df, marker='o', color=blue_shades[0], linewidth=2, linestyle='-', markersize=5, alpha=0.7, label='AI Research')
ax.plot('Year', 'Robotics', data=df, marker='v', color=blue_shades[1], linewidth=2, linestyle='--', markersize=5, alpha=0.7, label='Robotics')
ax.plot('Year', 'Neural_Networks', data=df, marker='s', color=blue_shades[2], linewidth=2, linestyle='-.', markersize=5, alpha=0.7, label='Neural Networks')
ax.plot('Year', 'Data_Mining', data=df, marker='D', color=blue_shades[3], linewidth=2, linestyle=':', markersize=5, alpha=0.7, label='Data Mining')

# Annotate each line at the end of the line with the corresponding legend label
for i, txt in enumerate(df['AI_Research']):
    ax.annotate('AI Research', (df['Year'][i], df['AI_Research'][i]))
for i, txt in enumerate(df['Robotics']):
    ax.annotate('Robotics', (df['Year'][i], df['Robotics'][i]))
for i, txt in enumerate(df['Neural_Networks']):
    ax.annotate('Neural Networks', (df['Year'][i], df['Neural_Networks'][i]))
for i, txt in enumerate(df['Data_Mining']):
    ax.annotate('Data Mining', (df['Year'][i], df['Data_Mining'][i]))

ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.set_title('Trends in AI Research, Robotics, Neural Networks, and Data Mining')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')

plt.tight_layout()
plt.savefig("myplot.png")