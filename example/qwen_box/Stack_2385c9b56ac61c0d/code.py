import matplotlib.pyplot as plt

# Data
months = [1, 2, 3, 4, 5, 6]
facebook_users = [120, 110, 105, 95, 90, 85]
twitter_users = [80, 85, 90, 95, 100, 105]
instagram_users = [100, 105, 110, 115, 120, 125]

# Stack plot
plt.stackplot(months, facebook_users, twitter_users, instagram_users, 
              labels=['Facebook', 'Twitter', 'Instagram'], 
              colors=['blue', 'green', 'purple'], alpha=0.6)

# X and Y labels
plt.xlabel('Month')
plt.ylabel('Number of Users (in millions)')

# Title
plt.title('User Trends of Social Media Platforms over Six Months')

# Legend
plt.legend(loc='upper left')

# Set the z-order of the area that contains the center point of the bounding box to 18
area = plt.gca().collections[18]
area.set_zorder(18)

# Add a shadow effect to this area with an offset of (2.83, 3.52) and shadow color purple
area.set_edgecolor('none')
area.set_facecolor('none')
area.set_alpha(0.5)
area.set_zorder(18)
area.set_transform(plt.gca().transData)
area.set_clip_path(plt.gca().patch, clip_on=False)

# Adjust the transformation of the area containing the center point of the bounding box to use the data coordinate system
area.set_transform(plt.gca().transData)

# Display the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")