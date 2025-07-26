import matplotlib.pyplot as plt

# Confirmed COVID-19 cases in each state
cases = [65000, 8500, 134000, 45000, 550000, 80000, 60000, 18000, 450000, 220000, 6000, 
         35000, 300000, 105000, 45000, 30000, 35000, 95000, 7500, 95000, 200000, 160000,
         55000, 58000, 90000, 7000, 25000, 70000, 9000, 280000, 32000, 450000, 140000,
         7000, 130000, 65000, 25000, 135000, 23000, 125000, 9000, 145000, 500000, 66000,
         1500, 130000, 80000, 6000, 75000, 5000]

# States in the USA 
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 
          'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 
          'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
          'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 
          'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

plt.figure(figsize=[20,10]) # Increase the size of the plot
plt.bar(states, cases, align='center', color='blue', edgecolor='black')
plt.xticks(rotation=90) 
plt.xlabel('States')
plt.ylabel('Confirmed COVID-19 Cases')
plt.title('Distribution of Confirmed COVID-19 Cases across the States in the USA') 
plt.tight_layout()

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox

# Get the center point of the bounding box
center = bbox.get_width()/2, bbox.get_height()/2

# Get the bars that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()[0].contains_point(center)

# Apply a stroke to the bars that contain the center point of the bounding box
for bar in bars:
    bar.set_edgecolor('#fff893')
    bar.set_linewidth(4.27)

# Update the linewidth of these bars
for bar in bars:
    bar.set_linewidth(2.96)

plt.savefig("figure.png")