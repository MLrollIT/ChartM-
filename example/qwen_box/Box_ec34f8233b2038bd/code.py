from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the given data
data = {'Year': [2014, 2015, 2016, 2017, 2018, 2019],
        'Organic Farming Practices': [2000, 2100, 2300, 3000, 2800, 3500]}
df = pd.DataFrame(data)

# Create a box plot of the 'Organic Farming Practices' column
fig, ax = plt.subplots(figsize =(10, 7))
bp = ax.boxplot(df['Organic Farming Practices'], patch_artist = True,
                notch = True, vert = 0, widths=0.7, sym='r+')

# Change the face color of the box
for patch in bp['boxes']:
    patch.set_facecolor('#FFFF00')

# Remove the grid
ax.grid(False)  # This line is modified to remove the grid lines

# Change the background color of the plot to white
ax.set_facecolor('white')  # This line is modified to change the background color

# Set the title and labels
ax.set_title('Organic Farming Practices Over the Years')
ax.set_xlabel('Organic Farming Practices')
ax.set_ylabel('Year')
ax.legend(['Organic Farming Practices'])

# Save the plot
plt.tight_layout()
plt.savefig('myplot.png')