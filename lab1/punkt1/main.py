import matplotlib.pyplot as plt

xmin, xmax, ymin, ymax = 0, 0, 0, 0
for i in range(1, 6):
    name = "dead_moroz/00" + str(i) + ".dat"
    num = int(open(name, "r").readline())
    f = open(name).readlines()
    xmin, xmax = min([float(i.split()[0]) for i in f[1:num]]), max([float(i.split()[0]) for i in f[1:num]])
    ymin, ymax = min([float(i.split()[1]) for i in f[1:num]]), max([float(i.split()[1]) for i in f[1:num]])

for i in range(1, 6):
    name = "dead_moroz/00" + str(i) + ".dat"
    f = open(name).readlines()
    x, y = [], []
    for j in range(1, int(f[0])+1):
        s = f[j].split()
        x.append(float(s[0]))
        y.append(float(s[1]))

    fig, ax = plt.subplots()
    ax.set_xlim([-50 + xmin, xmax + 50])
    ax.set_ylim([-50 + ymin, ymax + 50])
    ax.scatter(x, y, marker='x', linestyle='-', color='red', linewidth=0.8)
    #plt.legend()
    # включаем основную сетку
    plt.grid(which='major', color='black')
    # включаем дополнительную сетку
    plt.grid(which='minor', linestyle=':', color='lightgray')
    plt.title("Count of points " + f[0])
    plt.tight_layout()
plt.show()