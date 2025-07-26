from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data
data = {"Year": ["2014", "2015", "2016", "2017", "2018", "2019", "2020"],
        "Number of Visits": [5000, 4600, 4700, 4400, 7000, 6900, 4500],
        "Number of Books Borrowed": [7000, 6000, 9000, 6500, 8000, 12000, 7000]}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create figure and axes
fig, ax = plt.subplots()

# Create scatter plot for Number of Visits
visits = ax.scatter(df["Year"], df["Number of Visits"], marker="o", color="blue", label="Visits")

# Create scatter plot for Number of Books Borrowed
books = ax.scatter(df["Year"], df["Number of Books Borrowed"], marker="x", color="red", label="Books Borrowed")

# Set labels and title
ax.set_xlabel("Year")
ax.set_ylabel("Count")
ax.set_title("Number of Visits and Books Borrowed Over Years")

# Annotate data points
for i, txt in enumerate(df["Number of Visits"]):
    ax.annotate(txt, (df["Year"][i], df["Number of Visits"][i]))

for i, txt in enumerate(df["Number of Books Borrowed"]):
    ax.annotate(txt, (df["Year"][i], df["Number of Books Borrowed"][i]))

# Add grid and legend
ax.grid(True)
ax.legend()

# Change background color
ax.set_facecolor('gray')

# Save the plot
plt.tight_layout()
plt.savefig("myplot.png")