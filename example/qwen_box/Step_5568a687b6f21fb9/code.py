# Import the matplotlib library which is used for creating visualizations in Python.
import matplotlib.pyplot as plt  

# Events and intensity levels are stored in two separate lists.
events = ['Exoplanet Discovery', 'Solar Eclipse', 'Comet Visitation', 'Supernova Explosion', 'Gravitational Waves Detection']
intensity = [4.2, 5.8, 6.5, 7.3, 8.9]

# The step() function is used to create the stair plot. 
# The 'where' parameter is set to 'mid' which means that the steps change halfway between the x values.
# The color of the plot is set to be purple.
plt.step(events, intensity, where='mid', color='purple')

# The plot is given a title
plt.title('SpaceTime Exploration of Cosmic Phenomena')

# The x and y axes are labelled to give viewers an understanding of the plot.
plt.xlabel('Cosmic Events')  
plt.ylabel('Intensity Level')

# A grid is displayed to help viewers distinguish between individual values.
plt.grid(True)

# The plot is displayed.
  
plt.tight_layout()
plt.savefig("figure.png")

# The label of the step that contains the center point of the bounding box is updated to 'A new Label'
# The label is added to the legend
# The rasterized state of the label is set to True
plt.legend(['A new Label'], rasterized=True)