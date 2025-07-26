import matplotlib.pyplot as plt

# Years for X-axis
years = [2020, 2021, 2022]

# Popularity Percentages for Y-axis
classic = [20, 18, 15]
streetwear = [25, 30, 35]
bohemian = [15, 13, 15]
minimalist = [10, 12, 15]
sporty = [8, 10, 8]
glamorous = [7, 6, 5]
retro = [5, 4, 4]
eclectic = [5, 4, 3]
ethnic = [5, 3, 3]
others = [0, 0, 2]

# Plotting stack plot
plt.figure(figsize=(10,8))
plt.stackplot(years, classic, streetwear, bohemian, minimalist, sporty, glamorous, retro, eclectic, ethnic, others, 
              labels=['Classic','Streetwear','Bohemian','Minimalist','Sporty','Glamorous','Retro','Eclectic','Ethnic','Other'])

# Legends, titles and labels
plt.legend(loc='upper left')
plt.title('Trending Fashion Styles Worldwide (2020-2022)')
plt.xlabel('Year')
plt.ylabel('Popularity (%)')

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the area that contains the center point of the bounding box
bbox = plt.gca().get_position()
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.in