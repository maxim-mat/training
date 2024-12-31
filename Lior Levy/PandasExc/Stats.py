#1
import pandas as pd

#2
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv"

#3
baby_names = pd.read_csv(url)

#4
first_ten = baby_names.head(10)

#5
baby_names.drop(columns=['Unnamed: 0', 'Id'] , inplace=True)

#6
most_by_gender = baby_names.Gender.value_counts()

#7
names = baby_names.groupby('Name').sum()
names.sort_values("Count", ascending = 0).head()

#8
num_of_names = len(baby_names["Name"].unique())

#9
most_occurred_name = names.max()

#10
least_occurred_name = names.count().sort_values("Count")
names_least_occurred = least_occurred_name['Count'].value_counts().get(least_occurred_name['Count'].min(), 0)

#11
median_name = names.Count.median()

#12
names_std = names.Count.std()

#13
stats = names.describe()
