import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
temps = [21, 23, 20, 19, 22, 24, 25]

plt.plot(days, temps)
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over a Week')
plt.show()
