import matplotlib.pyplot as plt

count_ranges = ['0-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000-6000', '6000-7000', '7000-8000', '8000-9000', '9000-10000']
frequencies = [150, 200, 180, 140, 120, 90, 70, 50, 30, 20]

fig, ax = plt.subplots()

ax.bar(count_ranges, frequencies)
ax.set_xlabel('Streaming Count Ranges')
ax.set_ylabel('Frequency of Days')
ax.set_title('Distribution of Daily Music Streaming Counts')
ax.set_xticks(rotation=45)

# Get the bounding box of the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), fig=fig)

# Get the bar objects that contain the center point of the bounding box
bars = ax.containers[0].collections[0].get_paths()
for bar in bars:
    if bar.contains_point(bbox.center):
        bar.set_clip_on(False)
        bar.set_edgecolor('#cadde0')

plt.tight_layout()
plt.savefig("Edit_figure.png")