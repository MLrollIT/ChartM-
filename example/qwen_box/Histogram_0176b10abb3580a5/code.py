import matplotlib.pyplot as plt

# Data
genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Country', 'R&B', 'Jazz', 'Reggae', 'Classical', 'Alternative']
count = [150, 120, 80, 60, 40, 30, 20, 10, 5, 5]

# Create histogram
plt.figure(figsize=(10,6))
plt.bar(genres, count, color='blue', alpha=0.7)

# Set title and labels
plt.title('Distribution of Music Genres')
plt.xlabel('Music Genres')
plt.ylabel('Number of Songs')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Update the xlabel of the bars that contain the center point of the bounding box to 'A new Label'
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.get_points()
bbox[0] = (bbox[0][0], 0)
bbox[1] = (bbox[1][0], 0)
plt.gca().add_patch(plt.Rectangle(bbox[0], bbox[1][0] - bbox[0][0], 0, fill=False, edgecolor='black', linewidth=2))

# Set the picking state of these bars to False
plt.bar(plt.gca().get_position().get_points()[0][0], plt.gca().get_position().get_points()[0][1], color='blue', alpha=0.7, picker=False)

# Show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")