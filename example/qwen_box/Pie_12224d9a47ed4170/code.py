from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
data = {
    "Meat Type": ["Beef", "Poultry", "Pork", "Lamb and Goat", "Fish and Seafood", "Other Meats"],
    "Percentage": [20, 30, 25, 10, 10, 5]
}

# Extracting labels and sizes from the data
labels = data["Meat Type"]
sizes = data["Percentage"]

fig, ax = plt.subplots()

# Additional parameters for pie chart
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # To highlight each section
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']  # Different colors for each section

# Plotting the pie chart
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors,
       textprops={'size': 'smaller'}, radius=0.5, shadow=True, labeldistance=1.2, pctdistance=0.7)

# Setting the title and legend
plt.title("Distribution of Meat Consumption") 
plt.legend(labels, title="Meat Types", loc="upper right") 

# Changing the figure background color
fig.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")