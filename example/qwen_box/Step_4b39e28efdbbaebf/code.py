import matplotlib.pyplot as plt

# Decades (X-axis)
decades = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Percent of listeners per genre (Y-axis)
pop_music = [20, 30, 35, 45, 50, 60, 70, 75]
rock_music = [80, 75, 65, 60, 50, 30, 25, 20]
hip_hop_music = [5, 10, 25, 40, 60, 80, 85, 90]
electronic_music = [0, 2, 5, 10, 15, 25, 40, 65]

plt.figure(figsize=[10,8])

plt.step(decades, pop_music, where='mid', label='Pop Music')
plt.step(decades, rock_music, where='mid', label='Rock Music')
plt.step(decades, hip_hop_music, where='mid', label='Hip Hop Music')
plt.step(decades, electronic_music, where='mid', label='Electronic Music')

plt.ylim([0, 100])
plt.title('Music Genre Preferences Over Time')
plt.xlabel('Decades')
plt.ylabel('Percentage of Listeners')
plt.legend(loc='best')  
plt.grid(True)

# Set the clipping state of the lines that contain the center point of the bounding box to True
bbox = plt.gca().bbox_to_transform((0.5, 0.5))
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.get_window_extent().transformed(plt.gcf().transFigure.inverted())
bbox = bbox.get_points()

# Apply a stroke with a linewidth of 4.455 and a foreground color of #4ff741
for line in plt.gca().lines:
    line.set_clip_on(True)
    line.set_linewidth(4.455)
    line.set_color('#4ff741')

# plt.show()
plt.tight_layout()
plt.savefig("figure.png")