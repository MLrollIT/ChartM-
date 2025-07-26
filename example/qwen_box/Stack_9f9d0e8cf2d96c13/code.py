import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleep = [6, 7, 5, 8, 6]
eat = [2, 2, 1, 2, 1]
work = [5, 7, 10, 8, 6]
exercise = [3, 3, 0, 1, 3]

plt.stackplot(days, sleep, eat, work, exercise, labels=['Sleep','Eat','Work','Exercise'], colors=['m','c','r','k'])
plt.legend(loc='upper left')

plt.title('5 DAY ROUTINE')
plt.xlabel('Day')
plt.ylabel('Hours')

plt.tight_layout()

# Outline the area that contains the center point of the bounding box with a line width of 2.65 and a foreground color of #db2763.
bbox = plt.gca().bbox_to_transform([0.35, 0.25, 0.65, 0.7])
plt.plot([bbox[0], bbox[0]], [bbox[1], bbox[3]], color='#db2763', linewidth=2.65)
plt.plot([bbox[2], bbox[2]], [bbox[1], bbox[3]], color='#db2763', linewidth=2.65)
plt.plot([bbox[0], bbox[2]], [bbox[1], bbox[1]], color='#db2763', linewidth=2.65)
plt.plot([bbox[0], bbox[2]], [bbox[3], bbox[3]], color='#db2763', linewidth=2.65)

plt.tight_layout()
plt.savefig("figure.png")