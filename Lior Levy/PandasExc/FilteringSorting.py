import pandas as pd

#1
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

army = pd.DataFrame(raw_data)

#2
army.set_index('origin' , inplace=True)

#3
army_vets = army[['veterans' , 'deaths']]

#4
column_names = army.columns

#5
vets_in_loc = army.loc[['Maine', 'Alaska'] ,  ['deaths', 'size', 'deserters']]

#6
vets_range = army.iloc[2:7 , 2:6]

#7
vets_from_fourth = army.iloc[3:]

#8
vets_before_fourth = army.iloc[:3]

#9
vets_range_2 = army.iloc[: , 2:7]

#10
death_rows = army.loc[army['deaths'] >= 50]

#11
complex_condition = army[(army['deaths'] > 500) | (army['deaths'] < 50)]

#12
not_dragoons = army.loc[army['regiment'] != 'Dragoons']

#13
vets_in_loc_2 = army.loc[['Texas', 'Arizona']]

#14
vets_in_loc_3 = army.loc[['Arizona'] , army.columns[2]]

#15
vets_in_loc_4 = army.loc[:, 'deaths'].iloc[2]
