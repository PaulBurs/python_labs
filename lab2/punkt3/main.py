import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df1 = pd.read_excel('students/students_info.xlsx')
df2 = pd.read_html('students/results_ejudge.html')[0]
df = pd.merge(df1, df2, left_on='login', right_on='User', how='outer')
group_faculty = dict()
group_out = dict()
#print(df)
for i in df['group_faculty']:
    if i >= 0:
        group_faculty[i] = 0
for i in df['group_out']:
    if i >= 0:
        group_out[i] = 0
#print(group_faculty)

for group in group_faculty:
    target = df[df['group_faculty'] == group]
    #print(target)
    mean = (target[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']] > 0).sum().sum() / len(target)
    #print(mean.round(1))
    group_faculty[group] = mean.round(1)

for group in group_out:
    target = df[df['group_out'] == group]
    #print(target)
    mean = (target[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']] > 0).sum().sum() / len(target)
    #print(mean.round(1))
    group_out[group] = mean.round(1)

#print(group_faculty)
#Создаем фигуру с тремя подграфиками
fig, axs = plt.subplots(2, 1, figsize=(12, 6))
categories_faculty = list(group_faculty.keys())
categories_out = list(group_out.keys())
mean_faculty = [group_faculty[group] for group in group_faculty]
mean_out = [group_out[group] for group in group_out]

axs[0].bar(categories_faculty, mean_faculty, color='skyblue')
axs[0].set_title('Mean of faculty group')
axs[0].set_xlabel('Faculty group')
axs[0].set_ylabel('Average number of completed tasks')

axs[1].bar(categories_out, mean_out, color='lightgreen')
axs[1].set_title('Mean of out group')
axs[1].set_xlabel('Out group')
axs[1].set_ylabel('Average number of completed tasks')

plt.tight_layout()


target1 = df[df['G'] > 10]
target2 = df[df['H'] > 10]
target = pd.merge(target1, target2, how='outer')
#print(target)
for row in target.itertuples(index=True, name=None):
    print("User " + row[1] + " goes from faculty group " + str(int(row[2])) + " to out group " +  str(int(row[3])))
plt.show()