import matplotlib.pyplot as plt

for i in range(1, 6):
    name = "dead_moroz/00" + str(i) + ".dat"
    f = open(name).readlines()
    x, y = [], []
    for j in range(1, int(f[0])+1):
        s = f[j].split()
        x.append(float(s[0]))
        y.append(float(s[1]))

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='x', linestyle='-', color='red', linewidth=0.8)
    #plt.legend()
    # включаем основную сетку
    plt.grid(which='major', color='black')
    # включаем дополнительную сетку
    plt.grid(which='minor', linestyle=':', color='lightgray')
    plt.title("Count of points " + f[0])
    plt.tight_layout()
plt.show()