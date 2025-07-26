import matplotlib.pyplot as plt

time_intervals = ['0-10 mins', '10-20 mins', '20-30 mins', '30-40 mins', '40-50 mins']

cells_G1_Phase = [20, 18, 16, 14, 12]
cells_S_Phase = [15, 17, 19, 18, 20]
cells_G2_Phase = [10, 12, 14, 16, 18]
cells_Prophase = [5, 6, 7, 8, 9]
cells_Metaphase = [3, 5, 6, 7, 8]
cells_Anaphase = [2, 3, 4, 5, 6]
cells_Telophase = [1, 2, 3, 4, 5]
cells_Cytokinesis = [0, 1, 2, 3, 4]

plt.stackplot(time_intervals, cells_G1_Phase, cells_S_Phase, cells_G2_Phase, cells_Prophase, cells_Metaphase, cells_Anaphase, cells_Telophase, cells_Cytokinesis, labels=['G1 Phase','S Phase','G2 Phase','Prophase', 'Metaphase', 'Anaphase', 'Telophase', 'Cytokinesis'])

plt.legend(loc='upper left')
plt.xlabel("Time Intervals (minutes)")
plt.ylabel("Number of Cells")
plt.title("Number of Cells at Different Phases of Cell Cycle Over Time")

plt.tight_layout()

# Set the picker state of the areas that contain the center point of the bounding box to True
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
plt.gca().set_picker(True)
plt.gca().picker(5)

plt.savefig("Edit_figure.png")