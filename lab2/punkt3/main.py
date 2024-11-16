import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df1 = pd.read_excel('students/students_info.xlsx')
df2 = pd.read_html('students/results_ejudge.html')[0]
df = pd.merge(df1, df2, left_on='login', right_on='User', how='outer')
#print(df)
# Вычисление средних значений для факультетских групп
faculty_means = (
    (df[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']] >= 10)
    .groupby(df['group_faculty'])
    .mean()
    .sum(axis=1)
    .round(1)
)

# Вычисление средних значений для групп по информатике
out_means = (
    (df[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']] >= 10)
    .groupby(df['group_out'])
    .mean()
    .sum(axis=1)
    .round(1)
)

# Построение графиков
fig, axs = plt.subplots(1, 2, figsize=(12, 6), sharey=False)

axs[0].bar(faculty_means.index.astype(str), faculty_means.values, color='skyblue')
axs[0].set_title('Faculty of group')
axs[0].set_xlabel('Group')
axs[0].set_ylabel('Mean result')

axs[1].bar(out_means.index.astype(str), out_means.values, color='lightgreen')
axs[1].set_title('Number of inf group')
axs[1].set_xlabel('Group')

plt.suptitle('Results from groups', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.subplots_adjust(wspace=0.05)
plt.show()


target = df[(df['G'] > 10) | (df['H'] > 10)]

for row in target.itertuples(index=True, name=None):
    print("User " + row[1] + " goes from faculty group " + str(int(row[2])) + " to out group " +  str(int(row[3])))
plt.show()