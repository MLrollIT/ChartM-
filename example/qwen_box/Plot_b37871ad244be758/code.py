from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Year,Low-income countries,Middle-income countries,High-income countries
2000,50,150,500
2010,80,250,450
2020,60,300,400
""")
df = pd.read_csv(data)

# Plotting the data
fig, ax = plt.subplots()

ax.plot(df['Year'], df['Low-income countries'], marker='o', color='r', linestyle='-', linewidth=2, markersize=6, alpha=0.7, label='Low-income countries')
ax.plot(df['Year'], df['Middle-income countries'], marker='s', color='b', linestyle='--', linewidth=2, markersize=6, alpha=0.7, label='Middle-income countries')
ax.plot(df['Year'], df['High-income countries'], marker='v', color='g', linestyle=':', linewidth=2, markersize=6, alpha=0.7, label='High-income countries')

# Annotating the lines
for i, txt in enumerate(df['Low-income countries']):
    ax.annotate(txt, (df['Year'][i], df['Low-income countries'][i]))
for i, txt in enumerate(df['Middle-income countries']):
    ax.annotate(txt, (df['Year'][i], df['Middle-income countries'][i]))
for i, txt in enumerate(df['High-income countries']):
    ax.annotate(txt, (df['Year'][i], df['High-income countries'][i]))

ax.set_xlabel('Year')
ax.set_ylabel('Number')
ax.set_title('Comparison of numbers in different income countries over years')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig('myplot.png')