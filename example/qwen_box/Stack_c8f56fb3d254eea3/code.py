import matplotlib.pyplot as plt

# define months
months = ['June 2017', 'July 2017', 'August 2017', 
          'June 2018', 'July 2018', 'August 2018', 
          'June 2019', 'July 2019', 'August 2019', 
          'June 2020', 'July 2020', 'August 2020']

# define rainfall data
rainfall = [2.5, 1.8, 2.1, 
            3.2, 1.4, 1.7, 
            1.7, 2.5, 2.3, 
            2.8, 1.2, 1.5]

# define umbrella sales data
umbrella_sales = [60, 75, 80, 
                  50, 70, 85, 
                  70, 65, 90, 
                  55, 85, 95]

# define labels
labels = ['Rainfall(Inches)', 'Umbrella Sales']

# create stack plot
plt.stackplot(months, rainfall, umbrella_sales, labels=labels)
plt.legend(loc='upper left')
plt.title('Monthly Rainfall vs. Summer Umbrella Sales (2017 - 2020)')
plt.xlabel('Month')
plt.ylabel('Values')

# rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# adjust transparency and z-order of the center point of the bounding box
bbox = plt.gca().get_position().box
bbox[0] = 0.1
bbox[1] = 0.1
bbox[2] = 0.1
bbox[3] = 0.1
plt.gca().set_position(bbox)
plt.gca().set_facecolor('white')
plt.gca().set_alpha(0.3804)
plt.gca().set_zorder(4)

plt.tight_layout()
plt.savefig("figure.png")