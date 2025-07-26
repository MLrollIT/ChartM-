# import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# given data
pH_level = ['4.5', '6.5', '8.5']
growth_rates = [[0.4, 0.5, 0.3, 0.6, 0.7, 0.5, 0.4, 0.6, 0.7, 0.4], 
                [0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.7, 0.9, 0.8, 0.7], 
                [0.3, 0.2, 0.4, 0.3, 0.5, 0.4, 0.5, 0.4, 0.3, 0.2]]

# preparing data for plotting
data = []
for i in range(len(pH_level)):
    for rate in growth_rates[i]:
        data.append([pH_level[i], rate])

df = pd.DataFrame(data, columns=["Soil pH Level", "Growth Rates of Plant Species"])

# creating violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x="Soil pH Level", y="Growth Rates of Plant Species", data=df, inner="quartile")
plt.title("Growth Rate of Different Plant Species Across Various Soil pH Levels")
plt.tight_layout()

# set the face color of the violin that contains the center point of the bounding box to #3d54c4
violin = plt.gca().violinplot(df, positions=[6.5], showmeans=True, showextrema=False)
violin["bodies"][0].set_facecolor("#3d54c4")

# transform the whole violin to align with the axes' coordinate system
violin = plt.gca().violinplot(df, positions=[6.5], showmeans=True, showextrema=False)
violin["bodies"][0].set_transform(violin["bodies"][0].get_transform().rotate_deg(90))

plt.savefig("figure.png")