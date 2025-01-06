import os
import pandas as pd

path = (r'C:\Users\liorl\Desktop\New folder\training\2 - Python\2.6 - Exercise\trips_data')
extension = '.csv'

files = [file for file in os.listdir(path) if file.endswith(extension)]

dfs = []
for file in files:
    df = pd.read_csv(os.path.join(path, file))

    #getting the month and year from the name of the file by splitting the name
    df['time'] = (file.split("_"))[0]
    dfs.append(df)

month_track = pd.concat(dfs, ignore_index=True)
month_track.drop_duplicates(inplace=True)

month_track.to_csv('monthTracks.csv')
