import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Physics', 'Chemistry', 'Biology']
grades_extracurriculars = [80, 75, 90, 85]
grades_no_extracurriculars = [70, 65, 80, 75]

plt.figure(figsize=[10,5])

# For students participating in extracurricular activities
plt.step(subjects, grades_extracurriculars, where='mid', label='Participation in Extracurriculars')

# For students not participating in extracurricular activities
plt.step(subjects, grades_no_extracurriculars, where='mid', label='No Participation in Extracurriculars')

plt.ylim(0, 100) # Scale of grades

plt.title('Comparison of Academic Performance in STEM')
plt.xlabel('Subjects')
plt.ylabel('Average Grades')

plt.legend()
plt.tight_layout()
plt.savefig("figure.png")