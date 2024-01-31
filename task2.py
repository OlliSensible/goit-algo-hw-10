import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

n = 10000  
x_random = np.random.uniform(0, 2, n)
y_random = np.random.uniform(0, 4, n)

under_curve = y_random < f(x_random)
integral_mc = 2 * 4 * np.sum(under_curve) / n

integral_quad, _ = spi.quad(f, 0, 2)

print(f"Метод Монте-Карло: {integral_mc}")
print(f"Функція quad: {integral_quad}")