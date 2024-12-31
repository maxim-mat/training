import pandas as pd

#1
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv"
drinks = pd.read_csv(url)

#2
most_beers_continent = (drinks.groupby(['continent'])['beer_servings'].mean()
                        .sort_values(ascending=False).head(1))

#3
wine_per_continent = drinks.groupby(['continent'])['wine_servings'].sum()

#4
alcohol_per_continent = (drinks.groupby(['continent'])
                         [['beer_servings'
                        , 'spirit_servings'
                        ,'wine_servings'
                        ,'total_litres_of_pure_alcohol']].mean())

#5
median_alcohol_per_continent = (drinks.groupby(['continent'])
                         [['beer_servings'
                        , 'spirit_servings'
                        ,'wine_servings'
                        ,'total_litres_of_pure_alcohol']].median())

#6
spirit_stats = drinks['spirit_servings'].agg( ['min' , 'max' , 'mean'] )

