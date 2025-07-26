import matplotlib.pyplot as plt

# Given data
social_media_usage_hours = ['0-1 hour', '1-2 hours', '2-3 hours', '3-4 hours', '4-5 hours']
mental_health_scores = [8, 7, 6, 5, 4]

# Plotting
plt.figure(figsize=(10, 6))
plt.step(social_media_usage_hours, mental_health_scores, where='mid', label='mental health scores')

# Axis labels
plt.xlabel('Daily Social Media Usage')
plt.ylabel('Mental Health Scores')

# Title
plt.title('Impact of Social Media Usage on Teenagers\' Mental Health')

# Legend
plt.legend()

# Set the clip box for the lines that contain the center point of the bounding box
clip_box = plt.Bbox([[276, 363], [276 + 816, 363 + 596]])
plt.clipbox(clip_box)

# Change the marker face color of the lines associated with the center point of the bounding box
plt.plot(social_media_usage_hours, mental_health_scores, marker='o', markersize=10, color='#1eae9c')

# Show plot
plt.tight_layout()
plt.savefig("figure.png")