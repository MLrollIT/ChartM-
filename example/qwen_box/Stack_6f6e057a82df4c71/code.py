import matplotlib.pyplot as plt 

# Age groups
age_groups = ['15-25', '26-35', '36-45', '46-55', '56 and above']

# Floral fragrances data
rose = [45, 30, 20, 15, 5]
lavender = [30, 40, 35, 20, 25]
jasmine = [10, 15, 30, 40, 40]
lily = [15, 15, 15, 25, 30]

# Create a stackplot
plt.figure(figsize=[10,6])
plt.stackplot(age_groups, rose, lavender, jasmine, lily, labels=['Rose','Lavender','Jasmine','Lily'], alpha=0.8)

plt.title('Floral Fragrance Popularity by Age')
plt.xlabel('Age Groups')
plt.ylabel('Percentage of Individuals')

# Add a legend
plt.legend(loc='upper right')


# plt.show()
plt.tight_layout()
plt.savefig("figure.png")