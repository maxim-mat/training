import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = (
    load_theme("boxy_light")
    .set_grid(width=0.4)
    .set_axis_labels(size="large", weight="semibold")
    .set_font(style="oblique")
    .set_legend(shadow=True)
    .set_title(weight="bold")
)
theme.apply()

titanic = pd.read_excel(r"C:/Users/liorl/Desktop/New folder/training/2 - Python/2.5 - Visualization/titanic.xls")

# first plot
titanic['AgeGroup'] = 0
age_groups = ['1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
titanic['AgeGroup'] = pd.cut(titanic['age'], range(0, 90, 10), labels=age_groups)


def age_group_summary(df, age_groups):
    age_survival = df[['AgeGroup', 'survived']].groupby('AgeGroup').agg(['mean', 'count', 'sum'])
    age_survival = age_survival.reindex(age_groups)

    age_survival.columns = age_survival.columns.droplevel()
    age_survival.columns = ['survival rate', 'total', 'survived']
    age_survival['died'] = age_survival['total'] - age_survival['survived']

    return age_survival


age_survival = age_group_summary(titanic, age_groups)

ind = np.arange(len(age_survival))
width = 0.4
fig, ax = plt.subplots()

survived = age_survival['survived'].values
bar1 = ax.bar(ind, survived, width=width, label='Survived')

died = age_survival['died'].values
bar2 = ax.bar(ind + width, died, width=width,
              label='Died')
ax.set(xlabel='age', xticks=(ind + width), xticklabels=age_groups, ylabel='Number of passengers',
       title='Survival by age group')
plt.legend()
plt.show()

# second plot
pclass_survival = titanic[['pclass', 'survived']].groupby(['pclass']).mean()

ind = np.arange(len(pclass_survival))
width = 0.8
fig, ax = plt.subplots()

ax.bar(ind, pclass_survival['survived'], width)
ax.set(xlabel='Pclass', xticks=(ind + width / 2), xticklabels=np.arange(1, 4), ylabel='Survival rate',
       title='Survival by Pclass')

plt.show()
theme.apply_transforms()
