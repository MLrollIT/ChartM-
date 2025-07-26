import matplotlib.pyplot as plt

# Age Group
age_group = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70']

# Males %
males = [40, 45, 55, 48, 51, 46, 43]

# Females %
females = [60, 55, 45, 52, 49, 54, 57]

plt.figure(figsize=(10,7))

# Stackplot
plt.stackplot(age_group, males, females, colors=['blue', 'pink'], labels=['Males', 'Females'])

plt.legend(loc='upper left')

plt.title('Gender Distribution in Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Percentage (%)')

# Set the transparency of the area that contains the center point of the bounding box to 0.97
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.35
bbox[1] = 0.2
bbox[2] = 0.45
bbox[3] = 0.3
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='pink', alpha=0.97, edgecolor='none'))

plt.tight_layout()
plt.savefig("figure.png")