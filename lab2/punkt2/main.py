import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('flights.csv')
company = dict()
for i in data['CARGO']:
    company[i] = (0, 0, 0)
#print(company)
for cargo in company:
    #print(cargo)
    target = data[data['CARGO'] == cargo]
    counter = len(target)
    price = target['PRICE'].sum()
    weight = target['WEIGHT'].sum()
    company[cargo] = (counter, price, weight)


categories = list(company.keys())
counts = [company[cat][0] for cat in categories]
prices = [company[cat][1] for cat in categories]
weights = [company[cat][2] for cat in categories]

# Создаем фигуру с тремя подграфиками
fig, axs = plt.subplots(2, 2, figsize=(12, 6))

axs[0][0].bar(categories, counts, color='skyblue')
axs[0][0].set_title('Count of flights')
axs[0][0].set_xlabel('Company')
axs[0][0].set_ylabel('Count')

axs[0][1].bar(categories, prices, color='salmon')
axs[0][1].set_title('Price of flights')
axs[0][1].set_xlabel('Company')
axs[0][1].set_ylabel('Price')

axs[1][0].bar(categories, weights, color='lightgreen')
axs[1][0].set_title('Weight of flights')
axs[1][0].set_xlabel('Company')
axs[1][0].set_ylabel('Weight')

fig.delaxes(axs[1][1])
plt.tight_layout()
plt.show()