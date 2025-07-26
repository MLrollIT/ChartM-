import matplotlib.pyplot as plt

years = [2016, 2017, 2018, 2019, 2020]
preferences = [30, 40, 55, 65, 70]

plt.step(years, preferences, where='post')
plt.xlabel('Year')
plt.ylabel('Consumers Preferences for Plant-Based Food (%)')
plt.title('Consumer Preferences for Plant-Based Food Over the Years')
plt.ylim(bottom=0, top=100)
plt.grid(True)

# Change the marker style for the points at the center of the bounding box to '<'
plt.plot([2019, 2019], [60, 70], marker='<', markersize=10, color='black')

plt.tight_layout()
plt.savefig("figure.png")