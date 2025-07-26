from matplotlib.transforms import Bbox
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Plot the data
for i, tech in enumerate(data["Technology"]):
    ax.plot(years, df.loc[i, years], linestyle=linestyles[i], color=colors[i], marker=markers[i],
            linewidth=2, markersize=10, alpha=0.8, label=tech)
    ax.text(2, df.loc[i, "2019"], tech, va='center')

# Set the clip box for the plot
bbox = Bbox([[195, 175], [195 + 221, 175 + 286]])
ax.add_patch(Rectangle(bbox, 221, 286, facecolor='none', edgecolor='black', linewidth=1, zorder=7))

# Apply a shadow effect
ax.annotate("", xy=(195 + 221 / 2, 175 + 286 / 2), xycoords='data',
             xytext=(195 + 221 / 2 + 3.98, 175 + 286 / 2 + 3.11), textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", linewidth=2, color='black', zorder=7))

ax.grid()
ax.set_facecolor('#ADD8E6')  # Light blue background color

ax.set(xlabel='Year', ylabel='Units sold (in million)',
       title='Technology Sales Overview from 2017 to 2019')
ax.legend()

plt.tight_layout()
fig.savefig("Edit_figure.png")