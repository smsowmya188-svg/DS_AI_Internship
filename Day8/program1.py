import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 27, 30, 32, 31, 29, 28, 27, 26, 24, 22]
plt.plot(months, temperature, marker="o")
plt.title("Monthly Temperatures")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

