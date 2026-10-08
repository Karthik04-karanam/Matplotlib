import matplotlib.pyplot as plt
x=[2023, 2024, 2025, 2026, 2027]
y=[210, 4000, 606, 908, 4610]  
plt.plot(x, y,linestyle='dashed', marker='X')
plt.title("Productivity Plot")
plt.xlabel("Years")    
plt.ylabel("Sales")
plt.grid(True)
plt.show()