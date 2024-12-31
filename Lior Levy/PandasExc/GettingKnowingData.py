import pandas as pd

#1
food = pd.read_table('en.openfoodfacts.org.products.tsv')

#2
food.head(5)

#3
food.shape[0]

#4
food.shape[1]

#5
column_names = food.columns

#6
specific_col = food.columns[104]

#7
col_type = food.dtypes['-glucose_100g']

#8
dataset_index = food.index

#9
product_name = food.at[18 , 'product_name']

