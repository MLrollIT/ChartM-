import matplotlib.pyplot as plt

# Given data
x = [2016, 2017, 2018, 2019, 2020]
y_action = [120, 150, 140, 160, 180]
y_comedy = [80, 90, 100, 110, 120]
y_drama = [70, 60, 80, 90, 100]
y_fantasy = [60, 70, 80, 90, 100]
y_scifi = [90, 100, 110, 120, 130]

# Make plot
plt.figure(figsize=(10, 6))
plt.step(x, y_action, where='mid', label="Action")
plt.step(x, y_comedy, where='mid', label="Comedy")
plt.step(x, y_drama, where='mid', label="Drama")
plt.step(x, y_fantasy, where='mid', label="Fantasy")
plt.step(x, y_scifi, where='mid', label="Science Fiction")

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Box Office Revenue (in millions)')
plt.title('Box Office Revenue by Movie Genres (2016-2020)')

# Show legend
plt.legend()

# Set animated state of lines
for line in plt.gca().get_lines():
    line.set_animated(False)

# Set marker style and color for center point of bounding box
bbox = plt.gca().bbox_to_transform((0.5, 0.5))
plt.plot([bbox.xmin, bbox.xmax], [bbox.ymin, bbox.ymax], marker='^', color='#20de7e')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")