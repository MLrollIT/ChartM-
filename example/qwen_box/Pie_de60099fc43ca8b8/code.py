from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Given data
game_type = ["Action", "Adventure", "Role-Playing", "Sports", "Strategy", "Simulation", "Puzzle", "Others"]
percentage = [25, 15, 20, 10, 10, 10, 5, 5]

fig, ax = plt.subplots()
fig.set_facecolor('lightgray') # Set the background color

# Define the explode parameter
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # Only "explode" the 1st slice (i.e. 'Action')

# Here we set the fontsize for the labels and the autopct
ax.pie(percentage, explode=explode, labels=game_type, autopct='%1.1f%%',
       shadow=True, startangle=90, pctdistance=0.85, textprops={'fontsize': 14})

#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Here we set the fontsize for the title
plt.title("Distribution of Game Types", fontsize=14) # Add title

# Here we set the fontsize for the legend
plt.legend(game_type, title="Game Types", loc="upper right", title_fontsize=14) # Add legend

plt.tight_layout()
plt.savefig("myplot.png")