import matplotlib.pyplot as plt

# Data
drinks = ['Beer', 'Wine', 'Cocktails', 'Spirits']
percentages = [55, 30, 40, 20]

# Create figure and axes
fig, ax = plt.subplots()

# Plot the data using a step plot
ax.step(drinks, percentages, where='mid')

# Set the limits for x and y axes
ax.set_xlim(-0.5, len(drinks) - 0.5)
ax.set_ylim(0, 100)

# Label axes
ax.set_xlabel('Drink Options')
ax.set_ylabel('Percentage of Customers (%)')

# Add a title to the plot
ax.set_title('Preferred Drink Choices During Happy Hour')

# Adding grid lines
ax.grid()

# Set the label for the lines that contain the center point of the bounding box to 'A new Label' show the label as annotation and set the annotation xy = (1, 40).
ax.annotate('A new Label', xy=(1, 40), xycoords='data', xytext=(1, 40), textcoords='data', arrowprops=dict(arrowstyle="->"))

# Enable the picker state for those lines
ax.set_picker(True)

# Show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")