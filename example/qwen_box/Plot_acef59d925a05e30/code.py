from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

data = StringIO("""
Year,Meat Consumption
2010,50
2011,52
2012,80
2013,55
2014,70
2015,40
2016,75
""")

df = pd.read_csv(data)

fig, ax = plt.subplots(facecolor='grey')

ax.plot(df['Year'], df['Meat Consumption'], label="Meat Consumption", color="blue", linewidth=2, linestyle='-', marker='o', markersize=8, alpha=0.8)

for x, y in zip(df['Year'], df['Meat Consumption']):
    ax.text(x, y, str(y))

ax.set_title('Yearly Meat Consumption')
ax.set_xlabel('Year')
ax.set_ylabel('Meat Consumption')
ax.legend(loc='upper left', shadow=True)

ax.grid(True)
plt.tight_layout()
plt.savefig("myplot.png")