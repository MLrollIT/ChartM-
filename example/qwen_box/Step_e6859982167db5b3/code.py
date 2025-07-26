from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Year': [1960, 1970, 1980, 1990, 2000],
    'Missions': [35, 28, 45, 30, 50]
}

# Create a dataframe from the data
df = pd.DataFrame(data)

# Define the x and y data
x = df['Year']
y = df['Missions']

# Create a step plot
plt.step(x, y, label='Missions', linewidth=2, color='blue', marker='o', markersize=5, alpha=0.7)

# Annotate each line
for i, txt in enumerate(y):
    plt.annotate(txt, (x[i], y[i]))

# Set the title, x-label, y-label, and legend
plt.title('Missions over the years')
plt.xlabel('Year')
plt.ylabel('Number of Missions')
plt.legend()

# Add a grid
plt.grid(axis='both', color='0.95')

# Set the background color
plt.gca().set_facecolor('lightgray')

# Save the figure
plt.tight_layout()
plt.savefig('myplot.png')