import matplotlib.pyplot as plt

years      = [2015, 2016, 2017, 2018, 2019, 2020]

social_media_usage = [45, 50, 52, 55, 60, 65]
mental_health_issues = [30, 32, 35, 37, 41, 45]

labels = ['Social Media Usage (%)', 'Mental Health Issues (%)']

plt.stackplot(years, social_media_usage, mental_health_issues, labels = labels)
plt.legend(loc = 'upper left')

plt.title('Relation between Social media usage and Mental health issues')
plt.xlabel('Years')
plt.ylabel('Percentage (%)')

plt.tight_layout()
plt.savefig("figure.png")

# Update the linewidth of the area that contains the center point of the bounding box to 1.05.
plt.gca().patch.set_linewidth(1.05)
plt.savefig("Edit_figure.png")