from io import StringIO
import numpy as np

from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = StringIO("""
Year,Home Cooking,Takeout Meals,Meals at Restaurants
2017,74,50,90
2018,72,55,85
2019,75,60,75
""")

df = pd.read_csv(data)

years = df['Year']
home_cooking = df['Home Cooking']
takeout_meals = df['Takeout Meals']
meals_at_restaurants = df['Meals at Restaurants']

y = np.arange(len(years))
height = 0.2

fig, ax = plt.subplots()

bars1 = ax.bar(y - height, home_cooking, height, label='Home Cooking', color='lightgreen', edgecolor='green')
bars2 = ax.bar(y, takeout_meals, height, label='Takeout Meals', color='skyblue', edgecolor='blue')
bars3 = ax.bar(y + height, meals_at_restaurants, height, label='Meals at Restaurants', color='pink', edgecolor='red')

ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)
ax.bar_label(bars3, padding=3)

ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Comparison of Home Cooking, Takeout Meals, and Meals at Restaurants (2017-2019)')
ax.set_xticks(y)
ax.set_xticklabels(years)
ax.legend(loc='upper right')
ax.grid(visible=True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")