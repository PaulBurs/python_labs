import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 4):
  data = np.loadtxt(f'signals/signal0{i}.dat')
  update_data = np.zeros(len(data))
  step = 10

  cumsum = np.cumsum(data)
  for item in range(0, 11):
    start = max(0, item - step)
    end = min(len(data), item + step + 1)
    update_data[item] = np.mean(data[start:end])

  update_data[10:] = (cumsum[10:] - cumsum[:-10]) / 10

  fig, ax = plt.subplots(1, 2, figsize=(8, 6))

  ax[0].plot(data)
  ax[0].set_title('Сырой сигнал')
  ax[0].grid(True, which='both', linestyle='--', linewidth=0.5)
  ax[0].minorticks_on()

  ax[1].plot(update_data)
  ax[1].set_title('Сигнал после обработки')
  ax[1].grid(True, which='both', linestyle='--', linewidth=0.5)
  ax[1].minorticks_on()

  plt.savefig(f'{i}_array', dpi=300)
plt.show()


