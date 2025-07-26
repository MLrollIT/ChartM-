import matplotlib.pyplot as plt

# Years
years = list(range(1, 11))

# Successful launches data
Company_X = [10, 15, 20, 18, 25, 30, 35, 40, 45, 50]
Company_Y = [15, 10, 12, 14, 18, 20, 23, 25, 28, 30]
Company_Z = [5, 8, 10, 9, 12, 15, 18, 20, 22, 25]

# Creating the stack plot
plt.stackplot(years, Company_X, Company_Y, Company_Z, 
              labels=['Company X', 'Company Y', 'Company Z'],
              colors=['blue', 'orange', 'green'])

# Providing other details
plt.title("Journey of Commercial Spaceflight over a decade")
plt.ylabel('Number of Successful Launches')
plt.xlabel('Years')
plt.legend(loc='upper left')

# Change the color of the areas that contain the center point of the bounding box to #61a887, and update their label to 'A new Label'
bbox = plt.gca().get_position().get_points()
bbox[0] = (2.5, 0.2)
bbox[1] = (3.5, 0.6)
plt.gca().add_patch(plt.Rectangle(bbox[0], bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], fill=True, color='#61a887', label='A new Label'))

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")