import matplotlib.pyplot as plt

# Time points and corresponding units for each amino acid
time_points = ["T0", "T1", "T2"]
alanine = [12, 10, 14]
glutamine = [8, 6, 9]
lysine = [14, 16, 12]
proline = [6, 7, 5]

fig, ax = plt.subplots()

ax.stackplot(time_points, alanine, glutamine, lysine, proline, labels=['Alanine','Glutamine','Lysine','Proline'])

ax.legend(loc='upper left')
ax.set_title('Molecular Dance of Protein Structures')
ax.set_xlabel('Time Points')
ax.set_ylabel('Total Units of Amino Acids')

# Adjust the transparency of the area that contains the center point of the bounding box to 0.77, and change its color to #228a0b for those specific points.
bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[1][0] = 0.5
bbox_points[1][1] = 0.5
bbox.set_points(bbox_points)
bbox.set_facecolor('#228a0b')
bbox.set_alpha(0.77)

plt.tight_layout()
plt.savefig("figure.png")