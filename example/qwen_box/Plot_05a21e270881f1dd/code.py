import matplotlib.pyplot as plt
import pandas as pd

# data points
time = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
planets = ['Earth', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
values = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0.384, 0.384, 0.384, 0.384, 0.384, 0.384, 0.384, 0.384],
    [155, 155, 155, 155, 155, 155, 155, 155],
    [236, 235, 229, 215, 195, 169, 138, 101],
    [78, 79, 82, 86, 91, 97, 104, 111],
    [628, 630, 633, 638, 644, 652, 661, 673],
    [1275, 1277, 1279, 1285, 1295, 1307, 1322, 1338],
    [2735, 2731, 2727, 2719, 2706, 2688, 2667, 2643],
    [4355, 4348, 4340, 4324, 4300, 4270, 4231, 4186]
]

# creating data frame
df = pd.DataFrame(values, columns=time, index=planets)

# plot lines
plt.figure(figsize=(15,10))
for planet in planets:
    plt.plot(time, df.loc[planet, :], label=planet)

plt.xlabel('Time of the day')
plt.ylabel('Distance from Earth (million km)')
plt.title('Movements of celestial bodies over a 24-hour period')
plt.legend()
plt.grid()

# Set the thickness of the line that contains the center point of the bounding box to 2
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = plt