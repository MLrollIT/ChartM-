from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
Type of Clothing,2018,2019,2020
Casual,500,2000,1000
Formal,1000,500,2000
Sportswear,3000,2000,1000
Ethnic,2000,3000,2000
Luxury,4000,2000,4000
""")

# Convert the data into a DataFrame
df = pd.read_csv(data, sep=',')

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
styles = ['-', '--', '-.', ':']
colors = ['blue', 'red', 'green', 'orange', 'purple']
markers = ['o', 'v', 's', 'p', '*']
for i, clothing_type in enumerate(df['Type of Clothing']):
    ax.plot(df.columns[1:], df.loc[i, df.columns[1:]], linestyle=styles[i%len(styles)], color=colors[i%len(colors)], 
            marker=markers[i%len(markers)], markersize=6, linewidth=2, alpha=0.7, label=clothing_type)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_title('Sales of Different Types of Clothing Over the Years')

# Add a legend
ax.legend()

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df['Type of Clothing']):
    y = line.get_ydata()[-1]
    ax.annotate(name,
                xy=(1,y),
                xytext=(6,0), 
                xycoords = ax.get_yaxis_transform(), 
                textcoords="offset points",
                size="large", 
                color=line.get_color(), 
                weight='bold')

# Remove grid
ax.grid(False)

# Set background color to white
ax.set_facecolor('white') # Changed from 'lightgray' to 'white'

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")