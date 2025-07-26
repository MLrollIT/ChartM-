from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    "Smartphone": np.array([600, 700, 800, 500, 700]),
    "Laptop": np.array([500, 400, 900, 850, 1000]),
    "Tablet": np.array([500, 600, 400, 800, 900]),
    "Smartwatch": np.array([400, 300, 500, 150, 400]),
    "Smart TV": np.array([700, 600, 600, 700, 600]),
}
years = ["2016", "2017", "2018", "2019", "2020"]

# Setting up the plot
fig, ax = plt.subplots()
width = 0.15
x = np.arange(len(years))

# Iterating over the data and creating bars
for i, (gadget, values) in enumerate(data.items()):
    bars = ax.bar(x + i*width, values, width, label=gadget)
    ax.bar_label(bars)

# Adjusting the axes and adding labels, title, legend
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_title('Gadget Sales Over the Years')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(years)
ax.legend()
ax.grid(True)

# Change the background color to white
ax.set_facecolor('white')  # This line has been modified

# Change the fill pattern of the bars that share the same legend as those containing the center point of the bounding box to '|', and set their edge color to '#be6205'.
for bar in ax.patches:
    if bar.get_label() == 'Smartphone':
        bar.set_facecolor('|')
        bar.set_edgecolor('#be6205')

# Saving the plot
plt.tight_layout()
plt.savefig("myplot.png")