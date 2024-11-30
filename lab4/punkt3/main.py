import sympy as sp
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

y0 = np.sqrt(2)
t = np.linspace(0, 10, 1000)

#sympy
x = sp.Symbol('x')
y = sp.Function('y')

diff_eq = sp.Eq(y(x).diff(x), -2 * y(x))

sympy_solution = sp.dsolve(diff_eq, y(x))
C1 = sp.Symbol('C1')

start_condition = sp.Eq(sympy_solution.rhs.subs(x, 0), y0)
C1_value = sp.solve(start_condition, C1)[0]

sympy_solution = sympy_solution.subs(C1, C1_value)
sympy_function = sp.lambdify(x, sympy_solution.rhs, 'numpy')
print("Sympy solution:")
print("y(x) =", sympy_solution.rhs)


#scipy
def f(y, t):
    return -2 * y

scipy_solution = np.array(odeint(f, y0, t)).ravel()

sympy_solution = sympy_function(t)


# Построение графиков
plt.figure(figsize=(12, 6))

# (1) График обоих решений
plt.subplot(1, 2, 1)
plt.plot(t, scipy_solution, label='Sympy solution', linestyle='--')
plt.plot(t, sympy_solution, label='Scipy solution', linestyle='-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Sympy and Scipy solutions')
plt.legend()
plt.grid(True)

# (2) График разницы решений
plt.subplot(1, 2, 2)
difference = np.abs(sympy_solution - scipy_solution)
plt.plot(t, difference, label='|Sympy - Scipy|', color='red')
plt.xlabel('x')
plt.ylabel('Difference')
plt.title('Difference between Sympy and Scipy')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
