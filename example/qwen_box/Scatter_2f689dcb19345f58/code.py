import matplotlib.pyplot as plt

# Social Media Users Data in millions
facebook_users = [2100, 2150, 2130, 2170, 2120, 2075, 2050, 2090, 2125, 2105, 2080, 2060]
instagram_users = [1000, 1050, 1080, 1060, 1100, 1085, 1095, 1120, 1112, 1135, 1160, 1140]
twitter_users = [600, 620, 630, 610, 590, 600, 595, 605, 610, 615, 600, 590]

# Months
months = list(range(1, 13))

# Creating scatter plot
plt.scatter(months, facebook_users, label='Facebook')
plt.scatter(months, instagram_users, label='Instagram')
plt.scatter(months, twitter_users, label='Twitter')

# Adding title and labels
plt.title('Active Users Trends on Social Media Platforms')
plt.xlabel('Months')
plt.ylabel('Users in Millions')

# Displaying legend
plt.legend()

# Adjusting the size of the points that share the same legend as those containing the center point of the bounding box
plt.scatter(months, facebook_users, label='Facebook', s=20, edgecolor='red', linewidth=0.8)
plt.scatter(months, instagram_users, label='Instagram', s=20, edgecolor='red', linewidth=0.8)
plt.scatter(months, twitter_users, label='Twitter', s=20, edgecolor='red', linewidth=0.8)

# Displaying the plot

plt.tight_layout()
plt.savefig("figure.png")