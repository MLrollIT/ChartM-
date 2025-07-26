import matplotlib.pyplot as plt

# The x values are the names of the plant species
plant_species = ['Epiphytes', 'Orchids', 'Bromeliads', 'Ferns']

# The y values are the quantities of each plant species in each canopy layer 
canopy_layer_1 = [20, 10, 15, 25]
canopy_layer_2 = [15, 8, 12, 20]
canopy_layer_3 = [10, 5, 8, 15]
canopy_layer_4 = [5, 3, 4, 10]

# Stack plot
plt.figure(figsize=(10,7))
plt.stackplot(plant_species, canopy_layer_1, canopy_layer_2, canopy_layer_3, canopy_layer_4, 
              colors=['green', 'purple', 'red', 'blue'])

# Adding the necessary labels
plt.xlabel('Plant Species')
plt.ylabel('Quantities in Canopy Layers')

# Title of the plot
plt.title('Organic Growth Patterns in Rainforest')

# Adding the legend
plt.legend(['Canopy Layer 1', 'Canopy Layer 2', 'Canopy Layer 3', 'Canopy Layer 4'], loc='upper right')

# Set the picker state of the areas that contain the center point of the bounding box to True
plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick_event', lambda event: plt.gcf().canvas.mpl_connect('pick