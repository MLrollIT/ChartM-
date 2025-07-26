import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Define data
mangoes = [5, 4, 6, 5, 7, 4, 6, 5, 7, 4, 6, 5, 7, 4, 6, 5, 7, 4, 6, 5, 7]
papayas = [3, 4, 2, 4, 3, 5, 6, 5, 3, 2, 4, 6, 4, 5, 3, 6, 2, 5, 4, 3, 2]
bananas = [2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 2, 3, 2, 1, 3, 2, 3, 1, 2, 3, 1]

fruit_dict = {"Mangoes": mangoes, "Papayas": papayas, "Bananas": bananas}

fruit = []
ripening_time = []

for key, value in fruit_dict.items():
    for i in value:
        fruit.append(key)
        ripening_time.append(i)

data = pd.DataFrame({"Fruit": fruit, "Ripening Time": ripening_time})

# Violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Fruit", y="Ripening Time", data=data)

plt.title("Ripening Time Distributions for Tropical Fruits")
plt.xlabel("Type of Fruit")
plt.ylabel("Ripening Time (in days)")

# Change the color of the violin enclosed by the bounding box to #a43be0
plt.setp(plt.gca().violin_collection, facecolor="#a43be0")

plt.tight_layout()
plt.savefig("figure.png")