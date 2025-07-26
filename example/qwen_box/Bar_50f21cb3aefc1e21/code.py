from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
data = StringIO("""Genre,2000,2010,2020
Rock,100,85,70
Pop,80,90,60
Jazz,50,75,80
Country,70,65,90
Classical,60,45,65""")

# Load the data into a DataFrame
df = pd.read_csv(data)

# Define the genres and the years
genres = df['Genre']
years = df.columns[1:]

# Define the Figure and Axes objects
fig, ax = plt.subplots()

# Define the bottom for the stacked bar chart
bottom = np.zeros(len(genres))

# Plot each year's data
for year in years:
    values = df[year]
    bars = ax.bar(genres, values, label=year, bottom=bottom, color=np.random.rand(3,), edgecolor='black')
    ax.bar_label(bars, label_type='center')
    bottom += values

# Add the title and labels
ax.set_title('Music Genre Popularity Over Time')
ax.set_xlabel('Genre')
ax.set_ylabel('Popularity')

# Add a legend
ax.legend(loc="upper right")

# Add a grid
ax.grid(True)

# Set the background color to white
ax.set_facecolor('white')  # This line was modified

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")