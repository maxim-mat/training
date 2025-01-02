import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = (
    load_theme("arctic_light")
    .set_grid(width=0.1)
    .set_axis_labels(size="large" ,  weight="semibold")
    .set_font(style="oblique")
    .set_legend(shadow=True)
    .set_title(weight="bold")
)

theme.apply()

#first plot
titanic = pd.read_excel(r"C:/Users/liorl/Desktop/New folder/training/2 - Python/2.5 - Visualization/titanic.xls")
titanic.age[titanic.pclass == 1].plot(kind='kde')
titanic.age[titanic.pclass == 2].plot(kind='kde')
titanic.age[titanic.pclass == 3].plot(kind='kde')
plt.xlabel("Age")
plt.title("Age Distribution within classes")
plt.legend(('1st Class', '2nd Class','3rd Class'),loc='best')
plt.show()

# second plot
first_class = titanic.groupby('age')['pclass'].apply(lambda x: (x==1).sum()).reset_index(name='count')
second_class = titanic.groupby('age')['pclass'].apply(lambda x: (x==2).sum()).reset_index(name='count')
three_class = titanic.groupby('age')['pclass'].apply(lambda x: (x==3).sum()).reset_index(name='count')

fig, ax = plt.subplots()
ax.bar(first_class["age"] , first_class["count"],
       width=0.5
       ,label='first class'
       )
ax.bar(first_class["age"] , second_class["count"] , bottom=first_class["count"],
       width=0.5
        ,label='second class'
       )

ax.bar(second_class["age"] , three_class["count"] , bottom=first_class["count"],
       width=0.5
        ,label='third class'
       )
plt.xticks(np.arange(0, titanic["age"].max() + 2, step=10))
plt.title("Age Distribution by class")
plt.xlabel("Age")
plt.ylabel("Amount of People")
plt.legend()
plt.show()
theme.apply_transforms()