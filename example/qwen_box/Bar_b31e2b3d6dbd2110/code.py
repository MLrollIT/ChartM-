from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO("""
Demographics,Hours of Sleep,Anomalies
Young Adults,6.5,Sudden Spike
Middle-Aged Adults,7.2,Bimodal Trend
Seniors,5.8,Decline with Sudden Jump
""")

df = pd.read_csv(data)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(df['Demographics'], df['Hours of Sleep'], color='skyblue', edgecolor='black')

# Set title, x-label and y-label
ax.set_title('Sleep Hours by Demographics')
ax.set_xlabel('Demographics')
ax.set_ylabel('Hours of Sleep')

# Add grid and set the background color of the plot
ax.grid(True)
ax.set_facecolor('lightgray')

# Add labels to the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval,1), ha='center', va='bottom')

# Add legend
ax.legend(["Hours of Sleep"], loc='upper right')

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")