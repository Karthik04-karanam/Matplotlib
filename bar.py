import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [20, 4, 6, 8, 10]

plt.barh(x, y)

plt.title("Productivity Plot")
plt.xlabel("Years")
plt.ylabel("Sales")

plt.show()