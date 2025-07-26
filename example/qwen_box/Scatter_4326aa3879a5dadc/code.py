import matplotlib.pyplot as plt

# ROI data
x = [[0.5, 0.7, 0.8, 1.0], 
     [0.4, 0.6, 0.7, 0.9], 
     [0.3, 0.5, 0.6, 0.8], 
     [0.2, 0.4, 0.5, 0.7], 
     [0.1, 0.3, 0.4, 0.6], 
     [0.0, 0.2, 0.3, 0.5]]     

y = [[0.3, 0.4, 0.6, 0.7], 
     [0.2, 0.3, 0.5, 0.6],
     [0.4, 0.5, 0.7, 0.8], 
     [0.1, 0.2, 0.4, 0.5], 
     [0.0, 0.1, 0.3, 0.4], 
     [0.1, 0.2, 0.4, 0.5]] 

# plotting data for each ROI
for i in range(6):
    plt.scatter(x[i], y[i], label=f'ROI {i+1}')

plt.title('Hidden Structures in Brain Activity')
plt.xlabel('Intensity of brain activity (x-axis)')
plt.ylabel('Response to visual stimuli (y-axis)')
plt.legend()

# update the color of the scatter points that share the same legend as those containing the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.get_window_extent().transformed(plt.gca().transAxes.inverted())
bbox = bbox.get_points()

for i in range(6):
    if bbox[i, 0] < 0.5 and bbox[i, 1] < 0.5:
        plt.scatter(x[i], y[i], color='#824cb0', edgecolor='#4c70d3', linewidth=2.2)

plt.tight_layout()
plt.savefig("Edit_figure.png")