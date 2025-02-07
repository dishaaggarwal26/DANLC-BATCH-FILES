import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000,
                              36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000,
                           23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000,
                              25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000,
                                  19000, 20000, 21000, 22000, 23000])

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Monthly Sales Performance by Product Category", fontsize=16)

axes[0, 0].plot(months, electronics_sales, marker='o', linestyle='-', color='b', label="Electronics")
axes[0, 0].set_title("Electronics")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales ($)")
axes[0, 0].grid(True)

axes[0, 1].plot(months, clothing_sales, marker='o', linestyle='-', color='r', label="Clothing")
axes[0, 1].set_title("Clothing")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Sales ($)")
axes[0, 1].grid(True)

axes[1, 0].plot(months, home_garden_sales, marker='o', linestyle='-', color='g', label="Home & Garden")
axes[1, 0].set_title("Home & Garden")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Sales ($)")
axes[1, 0].grid(True)

axes[1, 1].plot(months, sports_outdoors_sales, marker='o', linestyle='-', color='m', label="Sports & Outdoors")
axes[1, 1].set_title("Sports & Outdoors")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales ($)")
axes[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
