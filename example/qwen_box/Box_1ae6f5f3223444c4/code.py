import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    '18-24 years': [500, 550, 600, 580, 560, 590, 630, 650, 680, 670, 630, 660],
    '25-34 years': [800, 850, 870, 900, 950, 930, 910, 920, 940, 980, 1000, 970],
    '35-44 years': [400, 420, 430, 380, 410, 410, 390, 400, 380, 360, 370, 380],
    '45-54 years': [250, 240, 260, 280, 290, 300, 310, 320, 310, 290, 280, 300],
    '55+ years': [150, 140, 130, 140, 160, 170, 180, 190, 200, 210, 220, 230]
}

# DataFrame
df = pd.DataFrame(data)

# Box Plot
plt.figure(figsize=(10, 5))
plt.boxplot([df[c] for c in df], labels=[c for c in df])
plt.title('Trends in Online Dating Behavior Among Different Age Groups During the COVID-19 Pandemic')
plt.xlabel('Age Group')
plt.ylabel('Number of Online Dating App Downloads per Month')
plt.grid(True)
plt.tight_layout()

# Modify the box that contains the center point of the bounding box
box = plt.gca().get_children()[1]
box.set_facecolor('#288a4b')
box.set_edgecolor('#fc54cc')
box.set_capstyle('round')
box.set_boxstyle('round,pad=0.5,rounding_size=5')

plt.savefig("Edit_figure.png")