import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = (
    load_theme("arctic_dark")
    .set_grid(width=0.1)
    .set_axis_labels(size="large", weight="semibold")
    .set_font(style="oblique")
    .set_legend(shadow=True)
    .set_title(weight="bold")
)

summary = pd.read_csv(r"summary.csv")

driver_group = summary.groupby(['driver_id' , 'vetek'])['total_km'].sum().reset_index(name="sum")
plt.bar(driver_group["vetek"], driver_group["sum"]
        , label='month'
        )
plt.title("km by vetek")
plt.xlabel("vetek")
plt.ylabel("km")
plt.show()

summary.age.plot(kind='kde')
plt.xlabel("Age")
plt.title("Age Distribution Within Drivers")
plt.show()

bins = np.arange(10, 100, 10)

summary['category'] = np.digitize(summary.age, bins, right=True)

counts = summary.groupby(['category', 'gender']).age.count().unstack()

ax = counts.plot(kind='bar',stacked = False, colormap = 'Paired')

for p in ax.patches:
        ax.annotate(np.round(p.get_height(),decimals=0).astype(np.int64), (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='center', xytext=(2, 10), textcoords='offset points')

plt.xlabel ('Age Group')
plt.ylabel ('Co-Occurences ')
plt.title('Comparison Of Occurences  In An Age Group',fontsize=20)
plt.show()
theme.apply_transforms()
