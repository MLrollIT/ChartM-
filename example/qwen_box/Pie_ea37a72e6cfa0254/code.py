from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

data = {
    "Cactus": 20,
    "Rose": 25,
    "Succulent": 15,
    "Orchid": 10,
    "Bamboo": 20,
    "Fern": 10
}

labels = list(data.keys())
sizes = list(data.values())

fig, ax = plt.subplots()
fig.set_facecolor('gray')  # Set the background color of the chart figure to gray

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # only "explode" each slice for visibility

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       textprops={'size': 'medium'}, radius=0.5, shadow=True, startangle=90)

plt.title("Popularity of Different Types of Plants", fontsize='medium')  # Add title with medium font size
ax.set_xlabel("Types of Plants", fontsize='medium')  # Add x-axis label with medium font size
ax.set_ylabel("Percentage", fontsize='medium')  # Add y-axis label with medium font size

plt.legend(labels, title="Types of Plants", loc="upper right", fontsize='medium')  # Add legend with medium font size

plt.tight_layout()
plt.savefig("myplot.png")