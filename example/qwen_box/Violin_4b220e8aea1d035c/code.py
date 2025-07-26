import matplotlib.pyplot as plt
import seaborn as sns

# User session durations
durations = [10, 7, 12, 15, 21, 18, 13, 11, 9, 8, 10, 12, 15, 13, 14, 19, 16, 20, 8, 11, 13, 17, 14, 12, 9, 10, 15, 16, 11, 13, 18, 19, 16, 14, 13, 12, 10, 11, 9, 17, 8, 12, 15, 16, 18, 14, 13, 19, 11, 10, 9, 17, 12, 15, 16, 13, 18, 14, 11, 13, 12, 15, 17, 19, 14]

# Create the violin plot
plt.figure(figsize=(9, 6))
sns.violinplot(y=durations, inner="stick")
plt.title('Violin plot of user session durations')
plt.ylabel('Session duration (in minutes)')

# Update the linewidth of the part that contains the center point of the bounding box to 4.57
plt.gca().spines['left'].set_linewidth(4.57)

plt.tight_layout()
plt.savefig("figure.png")