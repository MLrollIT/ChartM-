import matplotlib.pyplot as plt

# defining the data
smileys = [':)', ':D', ';)', ':P', ':O']
frequency = [500, 450, 400, 350, 300]

# creating a figure and a subplot
fig, ax = plt.subplots()

# plotting the stair plot
ax.step(smileys, frequency, where='mid')

# setting title and labels
ax.set_title('Top 5 Smileys Used Online Based on Their Popularity')
ax.set_xlabel('Smileys')
ax.set_ylabel('Frequency of usage on different social media platforms')

# modifying the label of the line that contains the center point of the bounding box
ax.set_ylabel('Frequency of usage on different social media platforms', labelpad=10)

# displaying the plot

plt.tight_layout()
plt.savefig("figure.png")