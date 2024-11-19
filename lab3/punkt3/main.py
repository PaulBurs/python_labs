import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def update(frame, u, line):
    line.set_data(np.arange(len(u[frame])), u[frame])  # Обновляем данные для линии
    return line,

u_0 = np.loadtxt("data")
size = len(u_0)
A = np.eye(size) - np.roll(np.eye(size), 1, axis=0)
u = np.zeros((256, size))
u[0] = u_0

evolution_matrix = np.eye(size) - 0.5 * A

# Вычисление всех шагов эволюции
powers = np.zeros((256, size, size))
#powers = np.array([np.linalg.matrix_power(evolution_matrix, i) for i in range(256)])
powers[0] = np.eye(size)
for i in range(1, 256):
    powers[i] = (powers[i-1] @ evolution_matrix)
u = np.tensordot(powers, u_0, axes=(2, 0))

# Создание фигуры и осей для графика
fig, ax = plt.subplots()
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.minorticks_on()
ax.set_ylim(0, 10)
ax.set_xlim(0, size)
ax.set_title("u(x, n)")
ax.set_xlabel("x")
ax.set_ylabel("u(x)")

# Создаем пустую линию
line, = ax.plot([], [], lw=2, color='blue')

# Настройка анимации
anim = FuncAnimation(fig, update, fargs=(u, line),
                     frames=len(u), interval=100)

# Сохранение анимации
anim.save('u_evolution.gif', writer='pillow', fps=10)
plt.show()
