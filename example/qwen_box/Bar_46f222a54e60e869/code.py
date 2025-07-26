from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# define the data
data = StringIO("""
Year,Asia,Europe,Americas
2000,2300,2900,2700
2005,2400,2500,2600
2010,2500,2100,2300
2015,3000,2200,2400
2020,2800,2000,2200
""")
df = pd.read_csv(data, sep=",")

# setup the plot
fig, ax = plt.subplots()

# define the width of the bars
width = 0.2

# create the bars with gradient color scheme
bars1 = ax.bar(df['Year'], df['Asia'], width, color='yellow', edgecolor='black')
bars2 = ax.bar(df['Year'] + width, df['Europe'], width, color='purple', edgecolor='black')
bars3 = ax.bar(df['Year'] + width*2, df['Americas'], width, color='cyan', edgecolor='black')

# add labels to the bars
ax.bar_label(bars1, label_type='center')
ax.bar_label(bars2, label_type='center')
ax.bar_label(bars3, label_type='center')

# set the title and labels
ax.set_title('Population by Year and Continent')
ax.set_xlabel('Year')
ax.set_ylabel('Population (in millions)')

# add a legend
ax.legend(['Asia', 'Europe', 'Americas'], loc='upper left')

# set the grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

# layout settings and save the plot
plt.tight_layout()
plt.savefig("myplot.png")