import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
fruits = ['Apple', 'Banana', 'Cherry', 'Grapefruit', 'Kiwi', 'Lemon', 'Mango', 'Orange', 'Pineapple', 'Watermelon']
sugar_content = [[10.3, 10.8, 11.2, 11.5, 11.3, 10.9, 11.7, 11.1, 11.9, 11.4],
                 [16.3, 15.7, 16.1, 16.4, 16.2, 16.6, 15.5, 15.9, 16.2, 16.7],
                 [8.9, 9.2, 9.4, 9.1, 9.7, 9.6, 9.8, 9.3, 9.5, 9.9],
                 [6.4, 6.1, 5.7, 6.3, 6.0, 6.6, 5.9, 5.8, 6.2, 6.5],
                 [8.3, 8.1, 8.6, 8.2, 8.5, 8.9, 8.7, 8.4, 8.8, 8.0],
                 [2.5, 2.2, 2.4, 2.6, 2.3, 2.9, 2.7, 2.8, 2.6, 2.5],
                 [14.3, 14.9, 14.6, 14.2, 15.1, 14.8, 14.4, 14.7, 14.5, 15.2],
                 [8.7, 8.5, 8.9, 9.4, 8.6, 8.3, 8.8, 9.3, 8.4, 8.2],
                 [8.4, 8.7, 8.2, 7.9, 8.6, 8.3, 9.0, 8.8, 8.5, 8.9],
                 [6.2, 6.0, 6.4, 5.9, 6.1, 5.8, 6.3, 5.7, 6.5, 6.7]]

# Prepare data for seaborn
data = []
for fruit, values in zip(fruits, sugar_content):
    for value in values:
        data.append({"Fruit": fruit, "Sugar Content (g/100g)": value})

# Create DataFrame
df = pd.DataFrame(data)

# Create Violin Plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Fruit", y="Sugar Content (g/100g)", data=df)
plt.title('Sugar Content Composition of Various Fruits')

# Set the fill pattern of the violin that contains the center point of the bounding box to a hatch pattern, using the color #cb579d
violin = plt.gca().violinplot(df, positions=[5], showmeans=True, showextrema=False)
violin["bodies"][0].set_facecolor("#cb579d")
violin["bodies"][0].set_hatch("/")

plt.tight_layout()
plt.savefig("figure.png")