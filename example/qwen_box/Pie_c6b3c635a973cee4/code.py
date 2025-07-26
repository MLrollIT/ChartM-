from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Data from the csv file
household_types = ["Single Family Residence", "Multi Family Residence", "Apartment"]
percentages = [45, 25, 30]

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Function to calculate the absolute values
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} households)"

# Draw the pie chart
wedges, texts, autotexts = ax.pie(percentages, autopct=lambda pct: func(pct, percentages),
                                  textprops=dict(color="w"), explode=[0.05]*len(household_types), 
                                  shadow=True, startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])

# Set the legend
ax.legend(wedges, household_types,
          title="Household Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Set the title
ax.set_title("Distribution of Household Types")

# Set the properties of the autotexts
plt.setp(autotexts, size=8, weight="bold")

# Set the face color of the figure
fig.set_facecolor('lightgray')

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")