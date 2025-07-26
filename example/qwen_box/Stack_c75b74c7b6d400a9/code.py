import matplotlib.pyplot as plt

# Days
days = [1, 2, 3, 4, 5]

# Data
geeks1 = [1, 1, 2, 3, 5]
geeks2 = [0, 4, 2, 6, 8]
geeks3 = [1, 3, 5, 7, 9]

# Stack plot
plt.stackplot(days, geeks1, geeks2, geeks3, labels=['Geeks1', 'Geeks2', 'Geeks3'])

plt.legend(loc='upper left')

# Labels and title
plt.xlabel("Days")
plt.ylabel("Units")
plt.title("Stack Plot of Geeks 1,2 & 3")

# Apply stroke to the area that contains the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt.gca().transFigure.inverted())
bbox = bbox.transformed(plt.gca().transAxes.inverted())
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.transformed(plt