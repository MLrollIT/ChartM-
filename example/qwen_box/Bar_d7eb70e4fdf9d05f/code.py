from io import StringIO
import numpy as np

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The given data
data = '''\
"Disorder","2017","2018","2019"
"Depression",350,400,375
"Anxiety",450,425,475
"Bipolar disorder",250,300,250
"Schizophrenia",150,250,150
"ADHD",200,250,350
'''
# Read the data
df = pd.read_csv(StringIO(data))

# Create the figure and the axes
fig, ax = plt.subplots()

# Plot the data
width = 0.25
years = ['2017', '2018', '2019']
x = np.arange(len(years))

for i, disorder in enumerate(df['Disorder']):
    values = df.loc[i, years].values
    ax.bar(x - width/2 + i*width, values, width, label=disorder, edgecolor="black")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Number of Cases')
ax.set_title('Number of Cases per Disorder from 2017 to 2019')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

# Add a grid
ax.grid(True)
ax.set_facecolor('lightgray')

# Add value annotations on each bar
bars = ax.containers
for bar in bars:
    ax.bar_label(bar, label_type='edge')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the transparency of the bars that share the same legend as those containing the center point of the bounding box to 0.533.
for bar in bars:
    if bar.get_label() == 'Anxiety':
        bar.set_alpha(0.533)