import matplotlib.pyplot as plt

# Students
students = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Social media usage (in hours per day)
social_media_usage = [2, 3, 1, 4, 3.5, 2.5, 1.5, 1.5, 2, 3]

# Sleep patterns (in hours per night)
sleep_patterns = [7, 6, 8, 5, 6.5, 7.5, 8.5, 8, 7.5, 6.5]

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(social_media_usage, sleep_patterns, color='blue')

# Label points
for i in range(len(social_media_usage)):
    plt.text(social_media_usage[i], sleep_patterns[i], students[i])

# Set x and y axis labels
plt.xlabel('Social Media Usage (Hours/Day)')
plt.ylabel('Sleep Patterns (Hours/Night)')

# Set title
plt.title('The Relationship between Social Media Usage and Sleep Patterns among College Students')

plt.grid(True)

# Get the bounding box of the first bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)

# Get the center point of the bounding box
center_point = bbox.get_points()[0]

# Change the color of the scatter points that contain the center point of the bounding box to #8e8705, and adjust their shape to a 'diamond'
for i in range(len(social_media_usage)):
    if plt.gca().bbox_to_transform(plt.gca().bbox).contains(plt.gca().bbox_to_transform([social_media_usage[i], sleep_patterns[i]])):
        plt.scatter(social_media_usage[i], sleep_patterns[i], color='#8e8705', marker='diamond')

plt.tight_layout()
plt.savefig("Edit_figure.png")