import matplotlib.pyplot as plt

# Combined box office earnings data
earnings = [250, 400, 300, 500, 350, 150, 200, 300, 250, 400, 100, 150, 200, 250, 300, 300, 350, 400, 450, 500, 200, 250, 300, 350, 400]

# Create the histogram
plt.figure(figsize=(8, 6))
plt.hist(earnings, bins=10, edgecolor='black')
plt.xticks(range(0, 601, 100))  # Adjust the X-axis tick intervals as needed
plt.xlabel('Box Office Earnings ($ millions)')
plt.ylabel('Frequency')
plt.title('Distribution of Box Office Earnings')

# Add a soft glow effect to the bars that contain the center point of the bounding box
glow_intensity = 0.5866
glow_color = '#a6ef8b'
bbox_points = [(250, 200), (300, 300), (400, 400)]
for points in bbox_points:
    x, y = points
    bar = plt.bar(x, y, color='blue', edgecolor='black', alpha=0.8)
    glow_bar = plt.bar(x, y, color=glow_color, edgecolor='black', alpha=glow_intensity, bottom=y, width=0.8)

# Reduce the height of these bars to 60% of their original height
for bar, glow_bar in zip(bar, glow_bar):
    height = bar.get_height()
    glow_bar.set_height(height * 0.6)

plt.tight_layout()
plt.savefig("Edit_figure.png")