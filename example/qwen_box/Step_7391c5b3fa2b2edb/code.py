import matplotlib.pyplot as plt
import pandas as pd

# Creating the DataFrame
data = {
    'Toppings': ['Pepperoni', 'Mushrooms', 'Onions', 'Extra Cheese', 'Olives', 'Pineapple', 'Others'],
    'Northeast': [35, 20, 15, 10, 10, 5, 5],
    'Midwest': [30, 15, 10, 15, 20, 5, 5],
    'Southwest': [25, 5, 5, 20, 15, 25, 5],
    'West Coast': [15, 10, 5, 25, 10, 10, 25]
}
df = pd.DataFrame(data)

# Setting the plot size
fig, ax = plt.subplots(figsize=(10, 6))

# Drawing the step plot for each region
for region in ['Northeast', 'Midwest', 'Southwest', 'West Coast']:
    ax.step(df['Toppings'], df[region], where='mid', label=region)

# Setting the plot title and labels
plt.title('Distribution of Popular Pizza Toppings in Different Regions')
plt.xlabel('Toppings')
plt.ylabel('Percentage of Customers (%)')

# Adding a legend
plt.legend()

# Setting the clip box for the line that contains the center point of the bounding box
bbox = plt.Bbox([[373, 175], [373 + 771, 175 + 279]])
ax.clip_on()
ax.set_clip_box(bbox)

# Adjusting the marker edge width for the same line
ax.step(df['Toppings'], df['Northeast'], where='mid', label='Northeast', marker='o', markersize=10, markeredgewidth=0.96)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")