import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Чтение данных
df = pd.read_csv('students.csv', sep=';', names=['prep', 'group', 'result'])
df['result'] = df['result'].astype(int)

# Группировка данных
preps = df.groupby('prep')['result'].value_counts().unstack(fill_value=0)
preps['mean'] = df.groupby('prep')['result'].mean()

groups = df.groupby('group')['result'].value_counts().unstack(fill_value=0)
groups['mean'] = df.groupby('group')['result'].mean()

grades = list(range(3, 11))


fig, axs = plt.subplots(2, 1, figsize=(12, 6))
width = 0.08

# Преподаватели
prep_names = preps.index
x_prep = np.arange(len(prep_names))

for i, grade in enumerate(grades):
    if grade in preps:
        axs[0].bar(x_prep + i * width, preps[grade], width, label=f'Result {grade}')

axs[0].set_xticks(x_prep + width * (len(grades) - 1) / 2)
axs[0].set_xticklabels(prep_names)
axs[0].set_xlabel('Preps')
axs[0].set_ylabel('Number of results')
axs[0].set_title('Results by prep')
axs[0].legend(title='Result', loc='center left', bbox_to_anchor=(1, 0.5))

# Группы
group_names = groups.index
x_group = np.arange(len(group_names))

for i, grade in enumerate(grades):
    if grade in groups:
        axs[1].bar(x_group + i * width, groups[grade], width, label=f'Result {grade}')

axs[1].set_xticks(x_group + width * (len(grades) - 1) / 2)
axs[1].set_xticklabels(group_names)
axs[1].set_xlabel('Group')
axs[1].set_ylabel('Number of results')
axs[1].set_title('Results by group')
axs[1].legend(title='Result', loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()

# Построение средних результатов
fig, axs = plt.subplots(2, 1, figsize=(12, 6))

colors_prep = [(165 / 255, 42 / 255, 42 / 255),
               (0, 128 / 255, 0),
               (0, 255 / 255, 0),
               (139 / 255, 0, 0),
               (205 / 255, 92 / 255, 0),
               (255 / 255, 140 / 255, 0),
               (173 / 255, 255 / 255, 47 / 255)]
axs[0].bar(preps.index, preps['mean'], color=colors_prep[:len(preps)])
axs[0].set_title('Mean of preps')
axs[0].set_xlabel('Prep')
axs[0].set_ylabel('Average result')

colors_group = [
    (139 / 255, 0, 0),
    (255 / 255, 99 / 255, 71 / 255),
    (255 / 255, 165 / 255, 0),
    (34 / 255, 139 / 255, 34 / 255),
    (0, 128 / 255, 0)
]
axs[1].bar(groups.index, groups['mean'], color=colors_group[:len(groups)])
axs[1].set_title('Mean of groups')
axs[1].set_xlabel('Group')
axs[1].set_ylabel('Average result')

plt.tight_layout()
plt.show()
