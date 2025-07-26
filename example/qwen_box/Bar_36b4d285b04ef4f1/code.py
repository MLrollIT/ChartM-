from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.cm import get_cmap

# Define csv data
data = StringIO("""
Genre,2005,2010,2015
Action,50,70,30
Adventure,60,75,90
Comedy,80,110,60
Drama,100,60,100
Horror,30,40,45
Romance,60,30,70
""")

# Read csv data into a pandas DataFrame
df = pd.read_csv(data, sep=",")

# Create a figure and axis
fig, ax = plt.subplots()

# Generate a color map of blue colors
cmap = get_cmap('Blues')
colors = cmap(np.linspace(0.2, 1.0, df['Genre'].nunique()))

# Create a bar chart with a gradient of blue colors
bars = ax.bar(df['Genre'], df['2005'], color=colors, edgecolor='black', tick_label=df['Genre'])

# Set labels and title
ax.set_xlabel('Genre')
ax.set_ylabel('Sales')
ax.set_title('Sales by Genre in 2005')

# Add legend with gradient colors
ax.legend(bars, df['Genre'], title='Genre')

# Add data values on each bar
ax.bar_label(bars, label_type='center')

# Set grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Save the figure
plt.tight_layout()
plt.savefig("myplot_gradient.png")