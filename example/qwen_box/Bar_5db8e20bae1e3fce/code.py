from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Given data
genre = ['Rock', 'Pop', 'Country', 'Hip-hop', 'Jazz', 'Electronic', 'Classical', 'Reggae', 'Blues']
popularity = [45, 65, 30, 55, 25, 35, 20, 50, 40]

# Creating the bar chart
fig, ax = plt.subplots()
bars = ax.bar(genre, popularity, color='skyblue', edgecolor='black')

# Setting the title and labels
ax.set_title('Popularity of Music Genres')
ax.set_xlabel('Genre')
ax.set_ylabel('Popularity')

# Annotating the data value on the chart
ax.bar_label(bars)

# Adding a grid on the background
ax.grid(True)

# Changing the background color of the chart
ax.set_facecolor('gray')

# Updating the label of the bars that contain the center point of the bounding box to 'A new Label', and setting their line width to 4.75
for bar in bars:
    if bar.get_x() + bar.get_width() / 2 == 30:
        bar.set_label('A new Label')
        bar.set_edgecolor('black')
        bar.set_linewidth(4.75)

# Saving the figure
plt.tight_layout()
plt.savefig("myplot.png")