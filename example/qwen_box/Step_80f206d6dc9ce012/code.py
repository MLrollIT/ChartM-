import matplotlib.pyplot as plt

# data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
height = [5, 8, 11, 18, 24, 30]

# create a new figure
plt.figure()

# create a step plot
plt.step(months, height, where='post', label='Plant Height (cm)')

# add a plot title and labels for the x-axis and y-axis
plt.title('Growth of Plants Infused with Pixie Dust Over Six Months')
plt.xlabel('Months')
plt.ylabel('Plant Height (cm)')

# add a legend 
plt.legend()

# modify the color of the step line that contains the center point of the bounding box to '#41a7ff'
plt.step(months, height, where='center', label='Plant Height (cm)', color='#41a7ff')

# show the plot

plt.tight_layout()
plt.savefig("Edit_figure.png")