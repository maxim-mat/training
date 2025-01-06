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

theme.apply_transforms()