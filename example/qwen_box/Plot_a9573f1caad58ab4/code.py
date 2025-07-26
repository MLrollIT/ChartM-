from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = '''Year,Artificial Intelligence,Robotics,Quantum Computing,Blockchain
2000,50,70,10,5
2001,55,65,12,7
2002,60,55,15,10
2003,65,50,20,20
2004,70,60,25,40
2005,75,55,40,30
2006,80,60,60,25
2007,85,70,80,20
2008,90,50,100,23
2009,100,60,50,27
2010,150,70,60,30
2011,140,80,70,35
2012,130,100,80,40
2013,170,120,90,45
2014,200,140,110,50
2015,230,160,120,55
2016,260,180,70,60
2017,290,200,75,65
2018,320,220,80,70
2019,350,240,85,75
2020,380,260,90,80'''

df = pd.read_csv(StringIO(data))

# Plotting the data
fig, ax = plt.subplots()

ax.plot(df['Year'], df['Artificial Intelligence'], marker='o', color='r', linestyle='-', linewidth=2, markersize=6, alpha=0.7, label='Artificial Intelligence')
ax.plot(df['Year'], df['Robotics'], marker='s', color='b', linestyle='--', linewidth=2, markersize=6, alpha=0.7, label='Robotics')
ax.plot(df['Year'], df['Quantum Computing'], marker='v', color='g', linestyle='-.', linewidth=2, markersize=6, alpha=0.7, label='Quantum Computing')
ax.plot(df['Year'], df['Blockchain'], marker='^', color='y', linestyle=':', linewidth=2, markersize=6, alpha=0.7, label='Blockchain')

# Annotating the lines
for i, txt in enumerate(df['Artificial Intelligence']):
    ax.annotate(txt, (df['Year'][i], df['Artificial Intelligence'][i]))
for i, txt in enumerate(df['Robotics']):
    ax.annotate(txt, (df['Year'][i], df['Robotics'][i]))
for i, txt in enumerate(df['Quantum Computing']):
    ax.annotate(txt, (df['Year'][i], df['Quantum Computing'][i]))
for i, txt in enumerate(df['Blockchain']):
    ax.annotate(txt, (df['Year'][i], df['Blockchain'][i]))

ax.set_xlabel('Year')
ax.set_ylabel('Number of Developments')
ax.set_title('Number of Developments in Different Tech Fields Over the Years')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig('myplot.png')