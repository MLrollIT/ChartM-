import matplotlib.pyplot as plt

years = list(range(2010, 2020))
region1 = [800, 850, 900, 950, 1000, 1100, 1050, 1000, 950, 900]
region2 = [600, 650, 700, 750, 800, 900, 850, 800, 750, 700]
region3 = [500, 550, 600, 650, 700, 800, 750, 700, 650, 600]
region4 = [400, 450, 500, 550, 600, 700, 650, 600, 550, 500]

plt.stackplot(years, region1, region2, region3, region4, labels=['Region1', 'Region2', 'Region3', 'Region4'])
plt.legend(loc='upper left')
plt.title('Average Rainfall (2010-2019)')
plt.xlabel('Year')
plt.ylabel('Average Rainfall (mm)')

plt.tight_layout()
plt.savefig("figure.png")