# import necessary library
import matplotlib.pyplot as plt

# provided salary data
salaries = [55000, 60000, 63000, 67000, 70000, 74000, 76000, 80000, 82000, 85000, 88000, 90000, 93000, 97000, 99000, 
            102000, 105000, 108000, 110000, 115000, 119000, 122000, 126000, 129000, 132000, 135000, 138000, 141000,
            144000, 148000, 151000, 155000, 159000, 162000, 165000, 168000, 172000, 175000, 179000, 183000, 187000, 
            191000, 195000, 199000, 203000, 207000, 211000, 215000, 220000]

# create histogram
plt.hist(salaries, bins=10, edgecolor='black')

# labeling
plt.xlabel("Salary ($)")
plt.ylabel("Number of Engineers")
plt.title("Salary Distribution of Software Engineers in Tech Industry")

# add glow outline to bars containing center point of bounding box
for bar in plt.gca().patches:
    if bar.get_bbox().contains(plt.gcf().bbox.get_points()[0]):
        bar.set_edgecolor('#c2c9a8')
        bar.set_linewidth(1.29)

# display plot
plt.tight_layout()
plt.savefig("figure.png")