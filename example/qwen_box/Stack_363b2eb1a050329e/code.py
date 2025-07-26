import matplotlib.pyplot as plt

years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']

# Percentages of market shares
apple = [40, 35, 30, 28, 25]
samsung = [30, 28, 25, 24, 23]
xiaomi = [15, 20, 22, 20, 18]
huawei = [10, 12, 13, 15, 17]
others = [5, 5, 10, 13, 17]

# Stacking each brand's market share on top of the other
plt.stackplot(years, apple, samsung, xiaomi, huawei, others, 
              colors=['green','blue','orange','red','gray'], 
              labels=['Apple', 'Samsung', 'Xiaomi', 'Huawei', 'Others'])

# Title and labels
plt.title('Market Share of Top-Selling Smartphone Brands Over Five Years')
plt.xlabel('Year')
plt.ylabel('Market Share (%)')

# Positioning the legend
plt.legend(loc='upper left')

# Modify the color of the area that contains the center point of the bounding box to #4bdba6 and update the linestyle to 'dotted'
bbox = plt.gca().bbox_to_transform((0.35, 0.25, 0.45, 0.35))
plt.fill_betweenx([0, 100], bbox, color='#4bdba6', linestyle='dotted')

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")