import matplotlib.pyplot as plt

# Age Groups
age_groups = ["Children (5-12 years)", "Teenagers (13-19 years)", "Young Adults (20-30 years)", "Adults (31-50 years)", "Seniors (51+ years)"]
  
# Time spent playing games per week 
hours = [2, 4, 6, 3, 1] 

plt.step(age_groups, hours, where='mid')

plt.xlabel('Age Groups') 
plt.ylabel('Hours spent playing pixel puzzle games per week') 
plt.title('Popularity of Pixel Puzzle Games among Different Age Groups') 

# Change the color of the points that contain the center point of the bounding box to #1665e2, and set their marker size to 17.66.
plt.scatter([3], [4], color='#1665e2', s=17.66)

plt.tight_layout()
plt.savefig("figure.png")