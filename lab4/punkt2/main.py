import scipy as sc
from scipy.linalg import solve
import numpy as np
import matplotlib.pyplot as plt
file = "data"
N = int(np.loadtxt(file, skiprows=0, max_rows=1))
# print(N)
A = np.loadtxt(file, skiprows=1, max_rows=N)
b = np.loadtxt(file, skiprows=N+1)
# print(A)
# print(b)
x = solve(A, b)
# print(x)

fig, axs = plt.subplots(figsize=(7, 5))
width = 0.1

# Преподаватели
coord = np.arange(1, N+1)

plt.bar(coord, x, width=width, color='skyblue', edgecolor='black')
axs.set_xlabel('Coordinats')
axs.set_ylabel('Value')
axs.set_title('Solution of Ax=b')
# axs.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(which='major', color='black')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':', color='lightgray')
plt.tight_layout()

plt.show()