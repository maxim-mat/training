import pandas as pd
import matplotlib.pyplot as plt
from aquarel import load_theme

def extract_last_name(x):
    return x.split(",")[0].strip()

theme = (
    load_theme("arctic_dark")
    .set_grid(width=0.1)
    .set_axis_labels(size="large" ,  weight="semibold")
    .set_font(style="oblique")
    .set_legend(shadow=True)
    .set_title(weight="bold")
)

titanic = pd.read_excel(r"C:/Users/liorl/Desktop/New folder/training/2 - Python/2.5 - Visualization/titanic.xls")
titanic["lastName"] = titanic["name"].apply(extract_last_name)

#first plot
titanic["familyGroup"] = titanic["pclass"].astype(str) + " - " + titanic["ticket"].str[:-1] + " - " + titanic["embarked"] + " - " + titanic["fare"].astype(str)
family_losses = titanic.groupby(['familyGroup' , 'lastName'])['survived'].apply(lambda x: (x==0).sum()).reset_index(name='count')
family_losses = family_losses.sort_values(by='count' , ascending=False)
family_losses = family_losses.head(10)

theme.apply()
fig, ax = plt.subplots()
ax.barh(family_losses["lastName"] , family_losses["count"]
       ,label='first class'
       )
plt.title("Losses by Family")
plt.xlabel("Family")
plt.ylabel("Amount of Members Lost")
plt.show()

#second plot
titanic['FamilySize'] = titanic['sibsp'] + titanic['parch'] + 1
pd.crosstab(titanic['FamilySize'], titanic['survived']).plot(kind='bar', stacked=True, title="Survived by family size")
plt.show()
theme.apply_transforms()