import matplotlib.pyplot as plt
import numpy as np

square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800,
3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

plt.scatter(square_footage,selling_prices,marker='o',c='g')
plt.grid(True)
plt.xlabel("Square footage (sq. ft.)")
plt.ylabel("Sellig Price ($000s)")
plt.title("Housing Price vs Square Footage")
plt.show()