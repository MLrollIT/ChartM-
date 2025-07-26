from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Create a figure object
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set the background color of the figure
fig.set_facecolor('gray')

# Given data
profession_data = {
    "Healthcare Workers": 15,
    "Teachers": 14,
    "Engineers": 13,
    "Lawyers": 12,
    "Artists": 16,
    "Retail Workers": 10,
    "IT Professionals": 10,
    "Unemployed": 10
}

labels = list(profession_data.keys())
data = list(profession_data.values())

# Function to calculate the percentage and absolute value
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

# Define new colors for the wedges
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CCE5FF', '#FF6666', '#FFD700', '#A0A0A0']

# Create a pie chart with the new colors
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"),
                                  colors=colors)  # <-- Add the 'colors' parameter here

# Create a legend
ax.legend(wedges, labels,
          title="Professions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Set the title of the chart
ax.set_title("Professions Distribution")

# Set the font size and weight of the text inside the pie chart
plt.setp(autotexts, size=8, weight="bold")

# Layout adjustment
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")