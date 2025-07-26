import matplotlib.pyplot as plt

# Create lists to store the months and infection rates
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
infection_rate = [200, 150, 100, 80, 70, 60, 50, 40, 30, 20, 20, 10]

# Create a new figure
plt.figure(figsize=(10, 6))

# Plot the data with a step plot
plt.step(months, infection_rate, where='mid', label='Infection rates')

# Set the titles for the x and y axes
plt.title('Impact of vaccination on global COVID-19 infection rates (per million)')
plt.xlabel('Months in 2021')
plt.ylabel('Infection rate')

# Display the legend
plt.legend()

# Set the clip box for the steps that contain the center point of the bounding box
bbox = plt.Bbox([[25, 486], [25 + 198, 486 + 864]])
plt.clipbox.set_snap(bbox)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")