import sympy as sp
import numpy as np

rho, lam, mu = sp.symbols('rho lambda mu')
matrix = sp.Matrix([
    [0,       0,       -1/rho, 0,       0,       0,       0, 0, 0],
    [0,       0,       0,      -1/rho,  0,       0,       0, 0, 0],
    [0,       0,       0,      0,       -1/rho,  0,       0, 0, 0],
    [-(lam+2*mu), 0,       0,      0,       0,       0,       0, 0, 0],
    [0,       -mu,     0,      0,       0,       0,       0, 0, 0],
    [0,       0,       -mu,    0,       0,       0,       0, 0, 0],
    [-lam,    0,       0,      0,       0,       0,       0, 0, 0],
    [0,       -lam,    0,      0,       0,       0,       0, 0, 0],
    [0,       0,       -lam,   0,       0,       0,       0, 0, 0],
])

# передача значения в функцию
eg_val = matrix.eigenvals()

# получение собственных значений
for item, value in enumerate(eg_val):
    print(item, "собственное значени", value)
# получение собственных векторов
#print(eg_vect)
