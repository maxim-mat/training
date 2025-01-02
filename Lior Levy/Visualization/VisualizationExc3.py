import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = (
    load_theme("boxy_light")
    .set_grid(width=0.4)
    .set_axis_labels(size="large" ,  weight="semibold")
    .set_font(style="oblique")
    .set_legend(shadow=True)
    .set_title(weight="bold")
)

titanic = pd.read_excel(r"C:/Users/liorl/Desktop/New folder/training/2 - Python/2.5 - Visualization/titanic.xls")

#first plot
survived = titanic.groupby('age')['survived'].apply(lambda x: (x==0).sum()).reset_index(name='count')
not_survived = titanic.groupby('age')['survived'].apply(lambda x: (x==1).sum()).reset_index(name='count')

theme.apply()
fig, ax = plt.subplots()
ax.bar(survived["age"] , survived["count"],
       width=0.5
       ,label='lived'
       )
ax.bar(survived["age"] , not_survived["count"] , bottom=survived["count"],
       width=0.5
        ,label='died'
       )
plt.xticks(np.arange(0, titanic["age"].max(), step=10))
plt.title("Age Distribution by Survivability")
plt.xlabel("Age")
plt.ylabel("Amount of People")
plt.legend()
plt.show()

#second plot
survived = titanic[titanic["survived"] == 1]
non_survived = titanic[titanic["survived"] == 0]

class_1 = titanic[titanic["pclass"] == 1]
class_2 = titanic[titanic["pclass"] == 2]
class_3 = titanic[titanic["pclass"] == 3]

Female = titanic[titanic["sex"] == "female"]
Male = titanic[titanic["sex"] == "male"]

fig, ax = plt.subplots(figsize=(10,5),nrows=1,ncols=3)
ax[0].hist(survived["age"],bins=15, alpha=0.5)
ax[0].hist(non_survived["age"],bins=15, alpha=0.5)
ax[0].set_xlabel("age")
ax[0].set_ylabel("quantity")
ax[0].legend(["survived","unsurvived"])

ax[1].hist(class_1["age"],bins=15,alpha=0.5)
ax[1].hist(class_2["age"],bins=15,alpha=0.5)
ax[1].hist(class_3["age"],bins=15,alpha=0.5)
ax[1].set_xlabel("Age")
ax[1].set_ylabel("Quantity")
ax[1].legend(["Pclass 1","Pclass 2", "Pclass 3"])

ax[2].hist(Female["age"],bins=15, color="darkred",alpha=0.5)
ax[2].hist(Male["age"],bins=15, color="darkblue",alpha=0.5)
ax[2].set_xlabel("Age")
ax[2].set_ylabel("Quantity")
ax[2].legend(["female","male"])

fig.suptitle("The Distribution of Survival and Pclass/Sex According to Age")
plt.show()

theme.apply_transforms()