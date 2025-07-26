from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = """
Genre,Popularity
Rock,80
Pop,90
Jazz,50
Country,70
"""
df = pd.read_csv(StringIO(data))

# Plot
fig, ax = plt.subplots()
for column in df.columns[1:]:
    ax.plot(df['Genre'], df[column], marker='o', linestyle='-.', color='b', linewidth=2.0, markersize=10, alpha=0.7, label=column)
    for x, y in zip(df['Genre'], df[column]):
        ax.text(x, y, str(y), size=10, va="bottom", ha="center")

# Annotations
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Genre')
ax.set_ylabel('Popularity')
ax.set_title('Popularity of Different Music Genres')
ax.legend()

# Changed background to white and removed gridlines
ax.grid(False)
ax.set_facecolor('white')  # Change background to white

plt.tight_layout()
plt.savefig('myplot.png')