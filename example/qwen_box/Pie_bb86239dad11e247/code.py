from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO('''Decade,Trend Percentage
"1960s","30%"
"1980s","35%"
"2000s","35%"''')

# Read the csv data
df = pd.read_csv(data, sep=",")
df['Trend Percentage'] = df['Trend Percentage'].str.rstrip('%').astype('float')

# Labels and sizes
labels = df['Decade'].tolist()
sizes = df['Trend Percentage'].tolist()

# Create figure and axis
fig, ax = plt.subplots()

# Plot pie chart
ax.pie(sizes, labels=labels, autopct='%.0f%%', explode=(0.1, 0, 0), 
       textprops={'size': 'smaller'}, radius=0.5, shadow=True, pctdistance=1.2, 
       colors=['#ff9999','#66b3ff','#99ff99'])

# Set title and legend
plt.title("Trend Percentage by Decade")
plt.legend(labels, title="Decades", loc="upper right")

# Set figure background color
fig.set_facecolor("lightgray")

# Layout setting and save figure
plt.tight_layout()
plt.savefig("myplot.png")