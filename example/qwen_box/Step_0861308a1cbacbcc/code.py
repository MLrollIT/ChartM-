import matplotlib.pyplot as plt

#Data
years = list(range(2010, 2021))
adoption_rates = [20, 22, 24, 28, 30, 34, 38, 40, 44, 48, 50]

#Create stair plot
plt.step(years, adoption_rates, where='post')

#Naming the x-axis, y-axis and the whole graph
plt.xlabel("Years")
plt.ylabel("Robot Adoption Rate (%)")
plt.title("Rise of Robot Adoption in Various Industries (2010-2020)")

#Plotting

plt.tight_layout()
plt.savefig("figure.png")