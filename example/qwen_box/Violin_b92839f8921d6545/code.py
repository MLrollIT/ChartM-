import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
meningioma_vol = [45, 50, 47, 55, 52, 60, 48, 53, 50, 58]
glioblastoma_vol = [75, 80, 82, 78, 85, 79, 76, 81, 83, 77]
pituitary_adenoma_vol = [30, 35, 32, 38, 37, 33, 36, 34, 39, 31]
astrocytoma_vol = [65, 70, 68, 72, 69, 67, 73, 71, 66, 74]
hemangioblastoma_vol = [40, 42, 45, 44, 48, 47, 43, 46, 41, 49]

data = [meningioma_vol, glioblastoma_vol, pituitary_adenoma_vol, astrocytoma_vol, hemangioblastoma_vol]
labels = ["Meningioma", "Glioblastoma", "Pituitary Adenoma", "Astrocytoma", "Hemangioblastoma"]

# Create violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data)
plt.xticks([0, 1, 2, 3, 4], labels)
plt.title("Brain Tumor Volume Analysis")
plt.ylabel("Tumor Volume (cc)")

# Adjust transparency and clipping state of violins containing the center point of the bounding box
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 0.05, bbox[1] + 0.05, bbox[2] - 0.1, bbox[3] - 0.1]
plt.gca().violinplot(data=data, showmeans=True, showextrema=False, showmedians=False, widths=0.5, clip_on=False, clip_limit=bbox, alpha=0.36)

plt.tight_layout()
plt.savefig("figure.png")