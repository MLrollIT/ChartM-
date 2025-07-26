import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
users = [250, 500, 800, 1000, 1300, 1600, 2000, 2300, 2600, 3000, 3500]
engagement = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

# Create stack plot
plt.figure(figsize=(10, 7))
plt.stackplot(years, users, engagement, labels=['Number of Users', 'User Engagement'], colors=['blue', 'orange'])

# Configure legend and labels
plt.legend(loc = 'upper left')
plt.title('User Growth and Engagement in Social Media Over 2010-2020')
plt.xlabel('Year')
plt.ylabel('Users (Million) / Engagement (Minutes/Day)')
plt.grid()

# Display plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the object in the chart
plt.gca().fill_betweenx([0, 3500], [2018, 2018], [2020, 2020], hatch='*', edgecolor='#123b4f', linestyle='solid')