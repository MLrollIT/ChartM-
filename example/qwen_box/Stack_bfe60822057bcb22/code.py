import matplotlib.pyplot as plt

# Year data (X-axis)
years = [2016, 2017, 2018, 2019, 2020]

# Genre revenues data in million dollars (Y-axis)
action_revenues = [750, 850, 900, 950, 800]
comedy_revenues = [500, 600, 700, 750, 600]
drama_revenues  = [400, 450, 550, 600, 450]

# Create stackplot
plt.stackplot(years, action_revenues, comedy_revenues, drama_revenues, 
              labels=['Action', 'Comedy', 'Drama'], 
              colors=['blue', 'orange', 'green'])

# Define labels and titles
plt.xlabel('Years')
plt.ylabel('Revenues (in millions)')
plt.title('Annual Trend of Box Office Revenues (2016-2020)')

# Include legend
plt.legend(loc='upper left')

# Adjust the transparency of the area that contains the center point of the bounding box to 0.5097
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.5097
bbox[1] = 0.5097
bbox[2] = 0.5097
bbox[3] = 0.5097
plt.gca().set_position(bbox)

# Set the edge linewidth of this area to 1.498 and change its color to #e5a4e4
plt.gca().patch.set_edgecolor('#e5a4e4')
plt.gca().patch.set_linewidth(1.498)

# Display the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")