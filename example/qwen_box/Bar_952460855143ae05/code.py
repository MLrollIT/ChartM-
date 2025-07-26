from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
City,Recycling Rate (%)
New York,12
San Francisco,18
Chicago,20
Dallas,25
Los Angeles,30
""")

df = pd.read_csv(data)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(df['City'], df['Recycling Rate (%)'], color='skyblue', edgecolor='black')

# Set title, x-label and y-label with updated font size
ax.set_title('Recycling Rate in Different Cities', fontsize=14)
ax.set_xlabel('City', fontsize=14)
ax.set_ylabel('Recycling Rate (%)', fontsize=14)

# Set tick labels font size
ax.tick_params(axis='both', labelsize=14)

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend with updated font size
ax.legend(["Recycling Rate (%)"], loc='upper right', fontsize=14)

# Add the corresponding value at the end of each bar
ax.bar_label(bars)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")