import matplotlib.pyplot as plt

# Months
months = [1, 2, 3, 4, 5, 6]

# Sales data
strategyA = [50000, 55000, 60000, 65000, 70000, 75000]
strategyB = [45000, 50000, 55000, 60000, 65000, 70000]
strategyC = [35000, 40000, 45000, 50000, 55000, 60000]

plt.figure(figsize=(10,7)) 
plt.stackplot(months, strategyA, strategyB, strategyC, colors=['blue', 'green', 'purple'], labels=['Strategy A','Strategy B', 'Strategy C'])

plt.title('Effectiveness of Different Marketing Strategies')
plt.xlabel('Months') 
plt.ylabel('Sales in $') 

# Adding legend
plt.legend(loc='upper left')

# Set the line color of the area that contains the center point of the bounding box to #423941
bbox = plt.gca().get_position().get_points()
bbox[1] = [0.35, 0.35]
bbox[0] = [0.35, 0.35]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2]-bbox[0], bbox[3]-bbox[1], fill=False, edgecolor='black', linewidth=2))

# Ensure that rasterization for this area is set to False
plt.gca().set_rasterization_zorder(0)

plt.tight_layout()
plt.savefig("figure.png")