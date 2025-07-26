from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

data = {
    "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    "Phishing Attacks": [12000, 11000, 18000, 16000, 20000, 15000, 22000, 19000],
    "Malware Attacks": [25000, 20000, 22000, 18000, 24000, 15000, 30000, 32000],
    "Ransomware Attacks": [3500, 4000, 9000, 8500, 6000, 10000, 12000, 14000]
}

fig, ax = plt.subplots()

# the label locations
y = np.arange(len(data["Year"]))
# the height of the bars
height = 0.25

for i, (attack_type, values) in enumerate(list(data.items())[1:]):
    offset = height * i
    bars = ax.barh(y + offset, values, height, label=attack_type, color=['red', 'green', 'blue'][i], edgecolor='black')
    ax.bar_label(bars, padding=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of Attacks')
ax.set_ylabel('Year')
ax.set_title('Cyber Attacks by Year')
ax.set_yticks(y + height)
ax.set_yticklabels(data["Year"])
ax.legend(loc='upper right', ncol=1)
ax.grid(True)
ax.set_facecolor('gray')
ax.invert_yaxis()  # labels read top-to-bottom

plt.tight_layout()
plt.savefig("myplot.png")