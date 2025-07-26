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

# Set the color of the violins that contain the center point of the bounding box to #56d9e2
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor="#56d9e2", alpha=0.5))

# Change the face color of those violins to #0e1046
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor="#0e1046", alpha=0.5))

plt.tight_layout()
plt.savefig("figure.png")