from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = """
Gadgets,Usage
Smartphones,3500
Tablets,3000
Laptops,4000
Smart Watches,2500
VR Headsets,1500
Game Consoles,3500
Drones,2000
Wireless Headphones,3000
"""
df = pd.read_csv(StringIO(data))

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple']
markers = ['.', 'o', 'v', '^', 's', 'p', '*', 'h']

# Plot
fig, ax = plt.subplots()
ax.plot(df['Gadgets'], df['Usage'], 
        linestyle=choice(linestyles), 
        color=choice(colors), 
        marker=choice(markers), 
        markersize=10, 
        alpha=0.7, 
        linewidth = 2)

ax.annotate(df.loc[df.index[-1], 'Gadgets'], 
            (df.index[-1], df.loc[df.index[-1], 'Usage']))

ax.set_title('Gadget Usage')
ax.set_xlabel('Gadgets')
ax.set_ylabel('Usage')
ax.grid(False)  # Disable gridlines
fig.set_facecolor('white')  # Change background to white

plt.tight_layout()
plt.savefig('myplot.png')