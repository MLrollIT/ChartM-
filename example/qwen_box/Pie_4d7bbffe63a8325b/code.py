from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Given data
workout = ["Yoga", "Weightlifting", "Cardio", "HIIT", "Pilates"]
percentage = ["30%", "25%", "20%", "15%", "10%"]

# Convert the percentage into float for pie chart
data = [float(p.strip('%')) for p in percentage]

# Figure and axis setup
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
ax.set_facecolor('lightgray')

# Function to format the percentage on the pie chart
def func(pct, allvals):
    absolute = int(round(pct))
    return "{:.1f}%\n({:d})".format(pct, absolute)

# Explode parameter for pie chart
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Yoga')

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(data, explode=explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), pctdistance=0.85, shadow=True)

# Draw a circle at the center (for 'donut' style)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Legend, title and labels
ax.legend(wedges, workout, title="Workout Regime", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax.set_title("Distribution of Workout Regimes")
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")