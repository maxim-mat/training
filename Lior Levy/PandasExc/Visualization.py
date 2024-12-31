import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#2
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

#3
chipo = pd.read_table(url)

#4
first_ten = chipo.head(10)

#5
top_five_items = chipo.groupby("item_name").sum().sort_values("quantity" , ascending= False).head(5)
top_five_items.drop(columns = "order_id" , inplace= True)
top_five_items.plot(kind= 'bar')

#6
orders = chipo.groupby("order_id").sum()
plt.scatter(orders["item_price"], orders["quantity"])
plt.show()
