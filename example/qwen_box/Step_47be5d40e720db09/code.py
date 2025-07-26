import matplotlib.pyplot as plt

# Given data
transport_modes = ['Walking', 'Bicycling', 'Public Transportation', 'Carpooling', 'Private Vehicle']
students_percentage = [30, 15, 20, 10, 25]

# Creation of step plot
plt.step(transport_modes, students_percentage, where='mid')

# Setting labels and title
plt.xlabel('Mode of Transportation')
plt.ylabel('Percentage of Students (%)')
plt.title('Mode of Transportation used by School Students')

# Set the color of the lines that contain the center point of the bounding box to #6198a9
bbox = plt.gca().get_position().get_points()
bbox[1] = [0.5, 0.5]
bbox[0] = [0.5, 0.5]
plt.gca().add_patch(plt.Rectangle(bbox[0], bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], fill=False, edgecolor='#6198a9', linewidth=2))

plt.grid(True)
plt.tight_layout()
plt.savefig("figure.png")