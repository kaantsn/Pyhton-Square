import matplotlib.pyplot as plt

# Kare çizimi için koordinatları tanımlayın.
x = [0, 1, 1, 0, 0]
y = [0, 0, 1, 1, 0]

# Grafiği çizin ve eksenleri belirleyin.
plt.plot(x, y, color='blue')
plt.axis('equal')

# Grafiği gösterin.
plt.show()
