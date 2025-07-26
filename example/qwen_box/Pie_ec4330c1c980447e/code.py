from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2001-2003", "2004-2006", "2007-2010"]
percentage = [30, 35, 35]

# Figure and Axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Pie chart with new color scheme
shades_of_blue = ['#add8e6', '#87cefa', '#4169e1']  # Lightest to darkest blue
wedges, texts, autotexts = ax.pie(percentage, explode=(0.1, 0, 0), labels=years, autopct='%1.1f%%',
                                   shadow=True, startangle=90, colors=shades_of_blue)

# Draw white circle in the middle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Title
ax.set_title("Percentage Distribution Over Years")

# Save figure
plt.tight_layout()
plt.savefig("myplot.png")