import matplotlib.pyplot as plt

# data for x-axis and y-axis
x = ['Low', 'Medium', 'High']
y = [20, 35, 45]

# creating a new figure
plt.figure()

# creating the stair plot
plt.step(x, y, where='mid')

# labeling the y-axis
plt.ylabel('Average Height of Flower Growth (cm)')
  
# labeling the x-axis
plt.xlabel('Sunlight Exposure Levels')
  
# title to be given to the plot
plt.title('Stair plot showing Flower Growth based on Sunlight Exposure Levels')
  
# function to show the plot

# plt.show()
plt.tight_layout()
plt.savefig("figure.png")