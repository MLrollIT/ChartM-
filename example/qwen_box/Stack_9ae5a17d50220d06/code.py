import matplotlib.pyplot as plt

days = ["Day1", "Day2", "Day3", "Day4", "Day5"]
study_hours = [7, 8, 6, 11, 7]
playing_hours = [8, 5, 7, 8, 13]

# Create stackplot
plt.stackplot(days, study_hours, playing_hours, labels=['Study_hours','Playing_hours'])

plt.legend(loc='upper left')
plt.title('Distribution of Study and Playing Hours Over Five Days')
plt.xlabel('Days')
plt.ylabel('Hours')

# Set clipping box for the areas containing the center point of the bounding box
bbox = plt.Bbox([[34, 117], [34 + 388, 117 + 175]])
plt.gca().set_clip_path(bbox.transform(fig.transFigure))

# Apply 'dashdot' linestyle to the areas
plt.stackplot(days, study_hours, playing_hours, labels=['Study_hours','Playing_hours'], linestyle='dashdot')

plt.legend(loc='upper left')
plt.title('Distribution of Study and Playing Hours Over Five Days')
plt.xlabel('Days')
plt.ylabel('Hours')

# plt.show()
plt.tight_layout()
plt.savefig("Edit_figure.png")