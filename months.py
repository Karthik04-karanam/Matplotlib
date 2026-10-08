import matplotlib.pyplot as plt
months = ['September', 'October', 'November', 'December']
sales_2025 = [1002, 150, 200, 250]
sales_2026 = [1200, 180, 240, 300]

plt.bar(months, sales_2025, label='2025')
plt.bar(months, sales_2026, label='2026')

plt.title("Sales Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()