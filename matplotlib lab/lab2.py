import numpy as np
import matplotlib.pyplot as plt

income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]


plt.pie(monthly_income,labels=income_sources,autopct='%1.1f%%',counterclock=True,wedgeprops={'alpha': 0.6},startangle=140 )
plt.title("Distributio of monthly income by source")
plt.show()