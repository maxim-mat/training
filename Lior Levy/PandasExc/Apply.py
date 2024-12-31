import pandas as pd

#1
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)

#2
data_types = crime.dtypes

#3
crime['Year'] = pd.to_datetime(crime['Year'] , format='%Y')

#4
crime.set_index('Year' , inplace=True)

#5
crime = crime.drop('Total', axis=1)

#6
result = crime.groupby(pd.Grouper(freq='10YE'))[[
'Violent' ,
'Property'  ,
'Murder'    ,
'Forcible_Rape' ,
'Robbery'  ,
'Aggravated_assault' ,
'Burglary'  ,
'Larceny_Theft' ,
'Vehicle_Theft']].sum()

#7
most_dangerous_decade = result.sum(axis=1, numeric_only=True).sort_values(ascending=False).head(1)


