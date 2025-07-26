import matplotlib.pyplot as plt

# years from 2017 to 2021
years = [2017, 2018, 2019, 2020, 2021]

# corresponding college acceptance rates in percentage
acceptance_rate = [40, 35, 32, 28, 30]

plt.figure(figsize=(9,6))

# plotting a step or stair plot
plt.step(years, acceptance_rate, where='mid', color='blue', linewidth=2)

plt.ylim(0, 50)  # Set y axis limits
plt.ylabel('Acceptance Rate (%)')  # Add a label to the y axis
plt.xlabel('Years')  # Add a label to x axis
plt.title('College Admission Statistics Over \n a Five-Year Period')  # Add a title to the plot

# modifying y ticks to display values up to 50 in increments of 10
plt.yticks(ticks=range(0,51,10))

plt.grid(True)  # Display gridlines on the plot

# modifying the line containing the center point of the bounding box
bbox = plt.Bbox([[271, 373], [271 + 183, 373 + 766]])
plt.plot([271, 271 + 183], [373, 373 + 766], color='blue', linewidth=3.1768, linestyle='-', transform=plt.gca().transData, clip_on=True, bbox=bbox)

# plt.show()
plt.tight_layout()
plt.savefig("figure.png")