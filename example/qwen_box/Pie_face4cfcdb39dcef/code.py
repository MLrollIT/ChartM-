from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Prepare data
age_group = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
consumption_percentage = [20, 20, 15, 15, 10, 10, 5, 5]

fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))

# Set colors
colors = ['red', 'blue', 'green', 'gold', 'purple', 'pink', 'orange', 'grey']

# Explode the first slice
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  

# Plot the pie chart
wedges, texts, autotexts = ax.pie(consumption_percentage, explode=explode, labels=age_group, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Set the title and legend
ax.set_title("Fast Food Consumption by Age Group")
ax.legend(wedges, age_group, title="Age Groups", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Set the text color to black
plt.setp(autotexts, size=8, weight="bold", color="black")

# Change the background color
ax.set_facecolor('lightgray')

# Layout adjustment
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")