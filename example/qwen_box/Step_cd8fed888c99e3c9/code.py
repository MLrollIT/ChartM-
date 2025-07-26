import matplotlib.pyplot as plt

# Data points
dog_owners = [8, 7, 6, 9, 8, 9, 9]
cat_owners = [6, 5, 7, 5, 6, 7, 7]

# Creating lists to hold X-axis labels
x = list(range(1,len(dog_owners)+1))
label=['Dog Owners']*len(dog_owners)+['Cat Owners']*len(cat_owners)

# Draws the stair plot
plt.step(x*2, dog_owners+cat_owners, where='mid')

# Adds title and labels to our plot
plt.title('Comparison of Happiness Levels between Dog Owners and Cat Owners')
plt.xlabel('Pet Owners')
plt.ylabel('Happiness Level [0-10]')

# set the limits for X and Y axis
plt.xlim([0.5, len(dog_owners)+0.5])
plt.ylim([0,10])

# set the X-ticks labels and make it vertical
plt.xticks(x*2, label, rotation='vertical')

# Displays the plot
plt.tight_layout()
plt.savefig("figure.png")