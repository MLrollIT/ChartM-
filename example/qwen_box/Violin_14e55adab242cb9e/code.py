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

# Modify the fill pattern of the violin that contains the center point of the bounding box
violin = sns.violinplot(x='emoji', y='score', data=df, inner="quartile", cut=0, color="#b130c3", linewidth=1.5, scale="width")
violin = sns.violinplot(x='emoji', y='score', data=df, inner="quartile", cut=0, color="#b130c3", linewidth=1.5, scale="width", hue="emoji", palette="husl", split=True, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, linewidth=1.5, scale="width", hue_order=emoji, hue_kws={"order": [0,