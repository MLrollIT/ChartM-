from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

csv_data = StringIO("""
Entertainment Form,Popularity Index
Cinema,55
Online Gaming,80
Music Concerts,35
Sporting Events,75
TV Series,90
Book Reading,25
""")

data = pd.read_csv(csv_data)

fig, ax = plt.subplots()

bars = ax.bar(data['Entertainment Form'], data['Popularity Index'], color='skyblue', edgecolor='black')

ax.set_title('Popularity Index of Different Entertainment Forms')
ax.set_xlabel('Entertainment Form')
ax.set_ylabel('Popularity Index')
ax.grid(False)  # Remove grid lines by setting to False.
ax.set_facecolor('white')  # Change the background color to white.

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') # va: vertical alignment

plt.tight_layout()
plt.savefig("myplot.png")