import matplotlib.pyplot as plt

# given data
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
accidents = [1000, 850, 1200, 950]

# plot data
plt.step(seasons, accidents, where='mid')

# define labels and title
plt.xlabel('Seasons')
plt.ylabel('Accident Frequency')
plt.title('Frequency of weather-related car accidents across different seasons')

# modify the line that contains the center point of the bounding box
plt.plot([5, 5], [900, 1050], linewidth=4.3, color='#5e7579')

# display
plt.tight_layout()
plt.savefig("figure.png")