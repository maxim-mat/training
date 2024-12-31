import pandas as pd

raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']
            }

pokemon = pd.DataFrame(raw_data)

#3
pokemon = pokemon.loc[:, ['name', 'type' , 'hp', 'evolution', 'pokedex']]

#4
place = ['place1', 'place2', 'place3', 'place4']
pokemon['place'] = place

#5
pokemon_types = pokemon.dtypes
