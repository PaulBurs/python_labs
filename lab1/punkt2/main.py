import matplotlib.pyplot as plt
import imageio
import os

# Создание папки для временных изображений
os.makedirs('img', exist_ok=True)


# Функция для создания кадра
def create_frame(t):
    plt.savefig(f'./img/img_{t}.png', transparent=False, facecolor='white')
    plt.close()


# Чтение данных
f = open("data").readlines()
x_m, y_m = [], []
for j in range(len(f)):
    s = f[j].split()
    if j % 2 == 0:
        x_m.append([float(a) for a in s])
    else:
        y_m.append([float(a) for a in s])

# Создание графиков и сохранение их как изображений
frames = []
xmin = 0
xmax = 0
ymin = 0
ymax = 0
for i in range(len(x_m)):
    x = x_m[i]
    xmin = min(min(x), xmin)
    xmax = max(max(x), xmax)
    y = y_m[i]
    ymin = min(min(y), ymin)
    ymax = max(max(y), ymax)

for i in range(len(x_m)):
    x = x_m[i]
    y = y_m[i]
    fig, ax = plt.subplots()
    ax.set_xlim([-1 + xmin, xmax+1])
    ax.set_ylim([-1 + ymin, ymax+1])
    ax.scatter(x, y, marker='x', color='blue', linewidth=1)
    ax.plot(x, y, linestyle='-', color='blue', linewidth=1)

    # Добавляем заголовок и сетку
    plt.title("Frame " + str(i))
    plt.grid(which='major', color='black')
    plt.grid(which='minor', linestyle=':', color='lightgray')
    plt.tight_layout()

    # Сохраняем кадр как изображение
    create_frame(i)
    frames.append(imageio.imread(f'./img/img_{i}.png'))

# Создание GIF-файла из изображений
imageio.mimsave('./example.gif', frames, fps=5)

# Удаление временных файлов изображений
for i in range(len(x_m)):
    os.remove(f'./img/img_{i}.png')

print("GIF создан успешно.")
