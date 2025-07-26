import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Order fulfillment time data for each store
store_A = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
store_B = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
store_C = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
store_D = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
store_E = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

# Combining the data
data = store_A + store_B + store_C + store_D + store_E
store = ['Store A']*10 + ['Store B']*10 + ['Store C']*10 + ['Store D']*10 + ['Store E']*10

df = pd.DataFrame({'Store': store, 'Order Fulfillment Time': data})

# Making the plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Store', y='Order Fulfillment Time', data=df)

plt.title('Comparison of Order Fulfillment Times Across Various Stores')
plt.tight_layout()

# Set the line style of all the elements in the violin that contains the center point of the bounding box to 'dashed'
violin = plt.gca().violinplot(data, positions=[4.5], showmeans=True, showextrema=False)
for element in violin['bodies']:
    element.set linestyle('dashed')

# Adjust the transformation of its box part to align with the axes' coordinate system
violin = plt.gca().violinplot(data, positions=[4.5], showmeans=True, showextrema=False)
for element in violin['bodies']:
    element.set_transform(element.get_transform().rotate_deg(90))

plt.savefig("figure.png")