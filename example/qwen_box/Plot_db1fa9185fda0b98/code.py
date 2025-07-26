from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = StringIO("""
Age_Group,Hours_Weekdays,Hours_Weekends,Hours_Holidays
Under_20,30,15,45
20_to_30,35,20,60
30_to_40,40,25,55
Above_40,20,10,30
""")
df = pd.read_csv(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan']
markers = ['.', 'o', 'v', '^']

# Plot
fig, ax = plt.subplots()
for i in range(len(df)):
    ax.plot(df.columns[1:], df.loc[i, df.columns[1:]], 
            linestyle=choice(linestyles), 
            color=colors[i], 
            marker=choice(markers), 
            markersize=10, 
            alpha=0.7, 
            label=df.loc[i, 'Age_Group'])
    
    for j in range(1, len(df.columns)):
        ax.annotate(df.loc[i, df.columns[j]], 
                    (df.columns[j], df.loc[i, df.columns[j]]))

ax.set_title('Hours Spent by Age Group')
ax.set_xlabel('Time Category')
ax.set_ylabel('Hours')
ax.legend(title='Age Group:')
ax.grid(True)
fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig('myplot.png')