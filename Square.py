import matplotlib.pyplot as plt

# Kare çizimi için koordinatları tanımlayın
a = [0, 1, 1, 0, 0]
b = [0, 0, 1, 1, 0]

# Grafiği çizin ve eksenleri belirleyin
plt.plot(a, b, color='blue')
plt.axis('equal')

# Grafiği gösterin
plt.show()
