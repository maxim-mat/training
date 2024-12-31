import pandas as pd

#2
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

#3
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

#4
all_data = pd.concat([data1 , data2])

#5
all_data_col = pd.concat([data1 , data2] , axis="columns")

#6
print(data3)

#7
merge_data =  pd.merge(all_data , data3 , on=["subject_id"])

#8
merge_data2 =  pd.merge(all_data , data3 , how="inner" ,on=["subject_id"])

#9
merge_data3 =  pd.merge(all_data , data3 , how="outer" ,on=["subject_id"])