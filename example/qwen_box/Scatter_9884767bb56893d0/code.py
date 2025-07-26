from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {'Year': [2016, 2017, 2018, 2019, 2020, 2021],
        'Software Sales': [10000, 12000, 14000, 10000, 12000, 16000],
        'Software Use': [20000, 18000, 15000, 10000, 20000, 25000]}
df = pd.DataFrame(data)

# Create the figure and the axes
fig, ax = plt.subplots()

# Plot the data
ax.scatter(df['Year'], df['Software Sales'], color='blue', marker='o', label='Software Sales')
ax.scatter(df['Year'], df['Software Use'], color='red', marker='o', label='Software Use')

# Annotate each line with legend label at the end of the line
ax.text(df['Year'].iloc[-1], df['Software Sales'].iloc[-1], ' Software Sales', va='center')
ax.text(df['Year'].iloc[-1], df['Software Use'].iloc[-1], ' Software Use', va='center')

# Annotate data values above the point on the chart figure
for i, txt in enumerate(df['Software Sales']):
    ax.annotate(txt, (df['Year'][i], df['Software Sales'][i]))
for i, txt in enumerate(df['Software Use']):
    ax.annotate(txt, (df['Year'][i], df['Software Use'][i]))

# Add grid, labels, title and legend
ax.grid(True)
ax.set_facecolor('lightgray')
ax.set_xlabel('Year', fontsize=14)  # Change font size of x axis label
ax.set_ylabel('Count', fontsize=14)  # Change font size of y axis label
ax.set_title('Software Sales and Use over Years', fontsize=16)  # Change font size of title
ax.legend()

# Modify the shape of the points that share the same legend as those containing the center point of the bounding box to 'star'. Also, update their edge color to #8a77f4 and set the edge width to 2.9.
ax.scatter(df['Year'][1], df['Software Sales'][1], color='blue', marker='star', edgecolor='#8a77f4', linewidth=2.9)
ax.scatter(df['Year'][1], df['Software Use'][1], color='red', marker='star', edgecolor='#8a77f4', linewidth=2.9)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")