import matplotlib.pyplot as plt
ages = [20, 30, 35, 40, 45]
frequency = [5, 10, 15, 20, 25]
plt.bar(ages, frequency)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()