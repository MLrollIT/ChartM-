import matplotlib.pyplot as plt

decades = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s']

vintage = [30, 20, 10, 5, 10, 15]
glamorous = [20, 40, 30, 30, 40, 30]
casual = [10, 30, 40, 10, 20, 20]
chic = [40, 10, 20, 55, 30, 35]

plt.figure(figsize=(10,6))

plt.stackplot(decades, vintage, glamorous, casual, chic,
              labels=['Vintage', 'Glamorous', 'Casual', 'Chic'],
              colors=['#6d904f', '#fc4f30', '#008fd5', '#e5ae38'], alpha=0.7)

plt.legend(loc='upper left')

plt.title('Fashion Trends over Six Decades')
plt.xlabel('Decade')
plt.ylabel('Percentage')

plt.tight_layout()

# Get the bounding box of the area containing the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)

# Get the coordinates of the center point of the bounding box
center_point = bbox.get_points()[0]

# Get the area containing the center point of the bounding box
area = plt.gca().collections[0].get_paths()[0].contains_point(center_point)

# Get the line color of the area
line_color = area.get_facecolor()

# Change the line color of the area to #498b69
area.set_facecolor('#498b69')

# Apply a stroke with a linewidth of 3.32 and a foreground color of #07765a
area.set_edgecolor('#07765a')
area.set_linewidth(3.32)

plt.savefig("figure.png")