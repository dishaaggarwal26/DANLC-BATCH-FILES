import matplotlib.pyplot as plt

segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

plt.figure(figsize=(8, 6))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', 
        startangle=140, wedgeprops={'edgecolor': 'black','alpha': 0.6})

plt.title("Company Revenue Distribution by Business Segment", fontsize=14)
plt.show()
