from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Category,Percentage
"Groceries","30%"
"Eating Out","20%"
"Entertainment","15%"
"Clothing","25%"
"Transportation","5%"
"Savings","5%"
""")

df = pd.read_csv(data, sep=",")
df['Percentage'] = df['Percentage'].str.replace('%','').astype(float)

# Create pie chart
labels = df['Category']
sizes = df['Percentage']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%', textprops={'size': 'smaller'}, radius=0.5, 
       explode=[0.1, 0, 0, 0, 0, 0], labeldistance=1.2, shadow=True, pctdistance=0.8, 
       colors=['#8B0000','#FFD700','#228B22','#00008B', '#FF4500','#6A5ACD']) # Modified colors

# Set chart attributes
plt.title("Distribution of Expenses") # Add title
plt.legend(labels, title="Categories", loc="upper right") # Add legend
fig.patch.set_facecolor('lightgrey') # Change the background color

plt.tight_layout()
plt.savefig("myplot.png")

# Set animated state of the slice that contains the center point of the bounding box to False
ax.pie(sizes, labels=labels, autopct='%.0f%%', textprops={'size': 'smaller'}, radius=0.5, 
       explode=[0.1, 0, 0, 0, 0, 0], labeldistance=1.2, shadow=True, pctdistance=0.8, 
       colors=['#8B0000','#FFD700','#228B22','#00008B', '#FF4500','#6A5ACD']) # Modified colors

# Set animated state of the slice that contains the center point of the bounding box to False