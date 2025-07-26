# Required libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data 
emoji = ['😊', '😂', '😍', '🔥', '😎', '🤔', '❤️', '👍', '😭', '🙏']
scores = [[0.8, 0.7, 0.9, 0.6, 0.8],
[0.9, 0.8, 0.7, 0.5, 0.9],
[0.7, 0.6, 0.8, 0.9, 0.7],
[0.6, 0.9, 0.7, 0.8, 0.7],
[0.5, 0.8, 0.9, 0.6, 0.8],
[0.4, 0.7, 0.5, 0.8, 0.6],
[0.9, 0.8, 0.9, 0.7, 0.5],
[0.8, 0.9, 0.8, 0.7, 0.6],
[0.7, 0.9, 0.4, 0.8, 0.5],
[0.6, 0.5, 0.7, 0.9, 0.8]]

# Prepare data for plotting:
emoji_scores = []
for e, s in zip(emoji, scores):
    emoji_scores.extend([(e, sv) for sv in s])
df = pd.DataFrame(emoji_scores, columns=['emoji', 'score'])

# Set the plot style 
sns.set(style="whitegrid")

# Create a violin plot
plt.figure(figsize=(10,8))
violin = sns.violinplot(x='emoji', y='score', data=df)
plt.title('Sentiment Distribution for Emojis')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the color of the violin that contains the center point of the bounding box to #ea003e and set its transparency to 0.43.
violin.collections[1].set_facecolor('#ea003e')
violin.collections[1].set_alpha(0.43)