# Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = {
  "Species A": [50, 60, 55, 70, 65, 58, 45],
  "Species B": [85, 80, 82, 78, 79, 81, 84, 86],
  "Species C": [40, 38, 42, 37, 39, 41, 36, 43],
  "Species D": [95, 92, 97, 93, 96, 91, 94]
}

# Converting the given data to a DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Melting the DataFrame to a long form
df_melted = pd.melt(df)

# Creating the Violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x="variable", y="value", data=df_melted)
plt.xlabel("Species")
plt.ylabel("Depths (m)")
plt.title("Underwater Creatures Habitat Mapping")

# Update the linewidth of the edges of the violins that contain the center point of the bounding box to 1.1
for violin in plt.gca().violinplots()[0]:
    for patch in violin['bodies']:
        patch.set_edgecolor('black')
        patch.set_edgealpha(1)
        patch.set_linewidth(1.1)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")