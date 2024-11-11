import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('students.csv')
data = []
for row in df.itertuples(index=True, name=None):
    data.append(row[1].split(';'))
for s in data:
    s[2] = int(s[2])
df = pd.DataFrame(data, columns=['prep', 'group', 'result'])
#print(df)
preps = dict()
groups = dict()
for i in df['prep']:
    preps[i] = [0,0,0,0,0,0,0,0,0]
for i in df['group']:
    groups[i] = [0,0,0,0,0,0,0,0,0]

for prep in preps:
    target = df[df['prep'] == prep]
    #print(target)
    for row in target['result']:
        #print(row)
        preps[prep][row-3] += 1
    mean = target['result'].sum() / len(target)
    preps[prep][8] = mean.round(1)
for group in groups:
    target = df[df['group'] == group]
    #print(target)
    for row in target['result']:
        #print(row)
        groups[group][row-3] += 1
    mean = target['result'].sum() / len(target)
    groups[group][8] = mean.round(1)



grades = list(range(3, 11))

fig, axs = plt.subplots(2, 1, figsize=(12, 6))
prep_names = list(preps.keys())
x_prep = np.arange(len(prep_names))
width = 0.08  # Ширина столбцов

for i, grade in enumerate(grades):
    prep_counts = [preps[prep][i] for prep in prep_names]
    axs[0].bar(x_prep + i * width, prep_counts, width, label=f'Result {grade}')

axs[0].set_xticks(x_prep + width * (len(grades) - 2) / 2)
axs[0].set_xticklabels(prep_names)
axs[0].set_xlabel('Preps')
axs[0].set_ylabel('Number of results')
axs[0].set_title('Results by prep')
axs[0].legend(title='Result', loc='center right')


group_names = list(groups.keys())
x_group = np.arange(len(group_names))

for i, grade in enumerate(grades):
    group_counts = [groups[group][i] for group in group_names]
    axs[1].bar(x_group + i * width, group_counts, width, label=f'Result {grade}')

axs[1].set_xticks(x_group + width * (len(grades) - 2) / 2)
axs[1].set_xticklabels(group_names)
axs[1].set_xlabel('Group')
axs[1].set_ylabel('Number of results')
axs[1].set_title('Result by group')
axs[1].legend(title='Result', loc='center right')

plt.tight_layout()



fig, axs = plt.subplots(2, 1, figsize=(12, 6))
categories_prep = list(preps.keys())
categories_group = list(groups.keys())
mean_prep = [preps[prep][8] for prep in preps]
mean_group = [groups[group][8] for group in groups]
#print(mean_prep)

colors_prep = [(165/255, 42/255, 42/255),
               (0, 128/255, 0),
               (0, 255/255, 0),
               (139/255, 0, 0),
               (205/255, 92/255, 0),
               (255/255, 140/255, 0),
               (173/255, 255/255, 47/255)]
axs[0].bar(categories_prep, mean_prep, color=colors_prep)
axs[0].set_title('Mean of preps')
axs[0].set_xlabel('Prep')
axs[0].set_ylabel('Average result')

colors_group = [
    (139/255, 0, 0),
    (255/255, 99/255, 71/255),
    (255/255, 165/255, 0),
    (34/255, 139/255, 34/255),
    (0, 128/255, 0)
]
axs[1].bar(categories_group, mean_group, color=colors_group)
axs[1].set_title('Mean of group')
axs[1].set_xlabel('Group')
axs[1].set_ylabel('Average result')

plt.tight_layout()
plt.show()