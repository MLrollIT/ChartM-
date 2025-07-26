import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Define the data
electronics_ratings = [4, 5, 3, 4, 2, 5, 4, 3, 4, 5, 1, 3, 2, 4, 5]
clothing_ratings = [3, 4, 2, 4, 3, 1, 5, 4, 2, 3, 4, 5, 3, 4, 2]
home_goods_ratings = [5, 4, 3, 2, 5, 4, 4, 3, 5, 2, 1, 4, 3, 2, 5]

ratings_data = {
    'Electronics': electronics_ratings,
    'Clothing': clothing_ratings,
    'Home Goods': home_goods_ratings
}

# Melt the data
melted_data = pd.melt(pd.DataFrame(ratings_data), var_name='Product Category', value_name='Ratings')

# Create violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Product Category', y='Ratings', data=melted_data, inner='point')
plt.title('Product Ratings by Category')
# plt.show()
plt.tight_layout()
plt.savefig("figure.png")

# Modify the transparency of the violins that contain the center point of the bounding box to 0.5406 and fill them with a texture of 'O'.
violin = plt.gca().violinplot(melted_data, positions=[1, 3, 5], showmeans=False, showmedians=False, showextrema=False)
for violin in violin['bodies']:
    violin.set_alpha(0.5406)
    violin.set_facecolor('O')

plt.show()