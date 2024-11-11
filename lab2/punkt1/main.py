import pandas as pd
data = pd.read_csv('transactions.csv')
#print(data)
target = data.loc[data['STATUS'] == 'OK']
target = target.sort_values(by='SUM', ascending=False)
print("3 самых крупных платежа из реально проведённых (статус OK)")
print(target.sort_values(by='SUM', ascending=False)[:3])
print("===============================")
target = target.loc[target['CONTRACTOR'] == 'Umbrella, Inc']
print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc")
print(target['SUM'].sum())