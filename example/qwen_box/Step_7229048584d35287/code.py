import matplotlib.pyplot as plt

# Age Groups
age_groups = ["Children (5-12 years)", "Teenagers (13-19 years)", "Young Adults (20-30 years)", "Adults (31-50 years)", "Seniors (51+ years)"]
  
# Time spent playing games per week 
hours = [2, 4, 6, 3, 1] 

plt.step(age_groups, hours, where='mid')

plt.xlabel('Age Groups') 
plt.ylabel('Hours spent playing pixel puzzle games per week') 
plt.title('Popularity of Pixel Puzzle Games among Different Age Groups') 

# Overlay a dashed step line on the part of the step chart that contains the center point of the bounding box to create a glowing effect
plt.plot([age_groups[2], age_groups[2]], [hours[2], hours[2]], dashes=[15, 10], color='#33c018', alpha=0.5)

plt.tight_layout()
plt.savefig("Edit_figure.png")