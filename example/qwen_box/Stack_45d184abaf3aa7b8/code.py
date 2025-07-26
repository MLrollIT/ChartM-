import matplotlib.pyplot as plt

# Define data for emojis
emojis = ['😂 (Laughing Face)', '❤️ (Red Heart)', '😭 (Loudly Crying Face)']
time_intervals = ['12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM', '12 AM']
emoji_data = {
    '😂 (Laughing Face)': [40, 35, 30, 25, 20, 25, 30, 35, 40, 45, 50, 45, 40],
    '❤️ (Red Heart)': [25, 30, 35, 40, 45, 40, 35, 30, 25, 20, 15, 20, 25],
    '😭 (Loudly Crying Face)': [15, 20, 25, 30, 35, 40, 45, 40, 35, 30, 25, 20, 15]
}

# Define colors for emojis
emoji_colors = ['lightyellow',  'lightcoral', 'lightblue']

# Create stack plot with custom colors
plt.figure(figsize=(10, 6))
plt.stackplot(time_intervals, [emoji_data[emoji] for emoji in emojis], labels=emojis, colors=emoji_colors)

# Customize plot
plt.title("Emoji Frequency in Text Messages (Teenagers)")
plt.xlabel("Time (12 PM - 12 AM)")
plt.ylabel("Percentage of Text Messages with Emoji")
plt.legend(loc='upper left')

# Show plot
plt.xticks(rotation=45)
# plt.show()
plt.tight_layout()
plt.savefig("figure.png")

# Modify the hatch pattern of the filled area that contains the center point of the bounding box to 'o'.
# Change the edge's linestyle to 'dashed' and set its color to #b9b64c for that same area.
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.35
bbox[1] = 0.6
bbox[2] = 0.45
bbox[3] = 0.65
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='none', edgecolor='#b9b64c', linestyle='dashed', hatch='o'))

plt.tight_layout()
plt.savefig("Edit_figure.png")