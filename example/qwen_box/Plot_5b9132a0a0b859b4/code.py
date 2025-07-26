from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data for plotting
data = """
Year,Pop,Rock,Jazz
2014,50,70,30
2015,55,95,32
2016,60,50,34
2017,65,105,40
2018,70,60,45
2019,73,55,70
2020,50,65,73
"""
df = pd.read_csv(StringIO(data), sep=',')
Year = df['Year']
Pop = df['Pop']
Rock = df['Rock']
Jazz = df['Jazz']

fig, ax = plt.subplots()

# Plotting the data with different styles
ax.plot(Year, Pop, linestyle='-', color='red', marker='o', markersize=5, linewidth=2, alpha=0.7, label='Pop')
ax.plot(Year, Rock, linestyle='--', color='blue', marker='v', markersize=5, linewidth=2, alpha=0.7, label='Rock')
ax.plot(Year, Jazz, linestyle='-.', color='green', marker='s', markersize=5, linewidth=2, alpha=0.7, label='Jazz')

# Setting up the labels, title
ax.set(xlabel='Year', ylabel='Genre Popularity',
       title='Popularity of Genres over the Years')
# Removed the grid with ax.grid(False) and set the background color to white with fig.set_facecolor('white')
ax.legend()

# Annotating each line
for i, txt in enumerate(Pop):
    ax.annotate('Pop', (Year[i], Pop[i]))
for i, txt in enumerate(Rock):
    ax.annotate('Rock', (Year[i], Rock[i]))
for i, txt in enumerate(Jazz):
    ax.annotate('Jazz', (Year[i], Jazz[i]))

fig.set_facecolor('white')

# Saving the figure
plt.tight_layout()
fig.savefig("myplot.png")