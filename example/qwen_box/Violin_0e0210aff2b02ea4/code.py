import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data 
string1 = [23.5, 23.8, 24.0, 24.2, 23.7, 24.1, 23.8, 24.3]
string2 = [23.9, 24.2, 24.5, 24.0, 24.4, 24.1, 24.3, 24.2]
string3 = [24.1, 23.7, 24.3, 23.9, 24.5, 24.0, 24.2, 23.8]
string4 = [23.8, 24.0, 23.9, 24.2, 24.3, 23.7, 24.1, 24.4]
string5 = [24.0, 24.3, 24.2, 24.1, 23.8, 24.5, 23.9, 24.0]

# Consolidate the data into a list of lists
data = [string1, string2, string3, string4, string5]

# Create a figure and axis
fig, ax = plt.subplots()

# Create the violin plot
sns.violinplot(data=data, ax=ax)

# Set the x-tick labels to be the string numbers
ax.set_xticklabels(['String 1', 'String 2', 'String 3', 'String 4', 'String 5'])

# Set the y label 
ax.set_ylabel('String Lengths (in inches)')

# Set the title
ax.set_title("Distribution of Guitar String Lengths Among a Sample of Musicians")

# Update the label of the violin that contains the center point of the bounding box to 'A new Label'
ax.collections[0].label = 'A new Label'

# Make sure that this violin is not rasterized by setting its rasterized state to False
ax.collections[0].set_rasterized(False)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")