from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO('''Year,Smartphone Usage
2016,60
2017,65
2018,130
2019,70
2020,80
2021,40
2022,90
2023,45
2024,75
2025,105
2026,50
2027,35
2028,65
2029,75
''')

df = pd.read_csv(data)

fig, ax = plt.subplots()

# Draw the bar chart
bars = ax.bar(df['Year'], df['Smartphone Usage'], color='skyblue', edgecolor='black')

# Setting labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Smartphone Usage')
ax.set_title('Smartphone Usage Over the Years')

# Annotate the data value on the chart 
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', fontsize=8)

# Adding grid and setting background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the fill pattern of the bars that contain the center point of the bounding box to '|', and update their edge color to '#0aa992'
bbox = (2018, 130, 2022, 90)
for bar in bars:
    if bar.get_x() + bar.get_width()/2 in bbox:
        bar.set_facecolor('|')
        bar.set_edgecolor('#0aa992')

plt.tight_layout()
plt.savefig("Edit_figure.png")