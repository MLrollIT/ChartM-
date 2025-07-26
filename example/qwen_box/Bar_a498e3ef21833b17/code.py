from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dataframe from given data
data = {'Retail Sector': ['Clothing', 'Electronics', 'Groceries', 'Furniture', 'Cosmetics'],
        'Q1': [100, 150, 200, 120, 90],
        'Q2': [80, 70, 180, 110, 60],
        'Q3': [90, 160, 210, 105, 55],
        'Q4': [70, 140, 220, 130, 80]}
df = pd.DataFrame(data)

# Set variables for chart
quarters = df.columns[1:]
sectors = df['Retail Sector']
bar_width = 0.15
bar_positions = np.arange(len(quarters))

# Create chart
fig, ax = plt.subplots()

for i, sector in enumerate(sectors):
    ax.bar(bar_positions - bar_width/2 + i*bar_width, df.loc[i, quarters], bar_width, label=sector, edgecolor='black')

# Add labels, title, and legend
ax.set_xlabel('Quarters')
ax.set_ylabel('Sales')
ax.set_title('Sales by Retail Sector per Quarter')
ax.set_xticks(bar_positions)
ax.set_xticklabels(quarters)
ax.legend(loc='upper left', ncol=1)

# Remove grid and set background color to white
ax.grid(False) # This line removes the gridlines
ax.set_facecolor('white') # This line changes the background color to white

# Annotate the data value on the chart
for rect in ax.containers:
    ax.bar_label(rect)

plt.tight_layout()
plt.savefig("myplot.png")