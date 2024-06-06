import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi interpolasi Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (xi - x[j]) / (x[i] - x[j])
        yi += Li * y[i]
    return yi

# Fungsi interpolasi Newton
def newton_interpolation(x, y, xi):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    
    yi = coef[0,0]
    xt = 1
    for j in range(1, n):
        xt *= (xi - x[j-1])
        yi += coef[0,j] * xt
    return yi

# Testing
x_test = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_test]
y_newton = [newton_interpolation(x, y, xi) for xi in x_test]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_test, y_lagrange, '-', label='Lagrange Interpolation')
plt.plot(x_test, y_newton, '--', label='Newton Interpolation')
plt.xlabel('Tegangan')
plt.ylabel('Waktu Patah')
plt.legend()
plt.title('Interpolasi Polinom Lagrange dan Newton')
plt.show()
