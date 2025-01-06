import pandas as pd
import numpy as np


def check_outlier_iqr(col_to_check, dataset):
    Q1 = col_to_check.quantile(0.25)
    Q3 = col_to_check.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outlier = dataset[(col_to_check < lower_bound) | (col_to_check > upper_bound)]
    return outlier


# cleaning all the data -

taarif = pd.read_csv(r"C:\Users\liorl\Desktop\New folder\training\2 - Python\2.6 - Exercise\taarif.csv")

# Starting by understanding the structure of the dataset
# Display the first few rows of the dataset
print(taarif.head())

# statistics summary
print(taarif.describe())

# info about dataset
print(taarif.info())

# after looking at the data we can see that there are nan rows and missing values
# in addition we can see that the weekend bonus is abnormally large compared to the night bonus
# so it might be worth to check if that was done on purpose or not

# handling missing values
print(taarif.isnull().sum())

# dropping completely empty rows
taarif.dropna(how='all', inplace=True)

# filling in missing values in bonus rows with 0.0 , we can assume that if the bonuses are nan
# than there aren't bonuses
taarif[['night_bonus', 'weekend_bonus']] = taarif.loc[:, ['night_bonus', 'weekend_bonus']].fillna(value=0)

# we can also assume that the basic taarif and extra miles will not be 0
# so we will replace them with the column mean
taarif.fillna({'basic_taarif': np.round(taarif['basic_taarif'].mean())}, inplace=True)
taarif.fillna({'extra_milage': np.round(taarif['extra_milage'].mean())}, inplace=True)

# now lets check if there are duplicates in the dataset
print(taarif.duplicated().sum())
# there are none so we continue

# earlier we so that there is an outlier in the weekend-bonus column
# now lets handle the outlier - to do that we will use the IQR method which I found
print(check_outlier_iqr(taarif["weekend_bonus"], taarif))

# we can see that there are two outliers one is 500 and the other 70000
# we can assume the 500 is intentional but we cant do the same for the 70000
# lets say it was a typo and change it to 70
taarif.loc[11, 'weekend_bonus'] = 70

taarif.to_csv('taarif.csv')
# nice job! seems like this dataset is clean and we are ready to move on to the rest of the datasets :)
# lets go over the same process
kviut_drivers = pd.read_csv(
    r"C:\Users\liorl\Desktop\New folder\training\2 - Python\2.6 - Exercise\Drivers_with_kviut.csv")

print(kviut_drivers.head())
print(kviut_drivers.describe())
print(kviut_drivers.info())

# some conclusions we can already get-
# the birthdate column is of type string and not datetime
# there is an unnamed column which is unnecessary
# in the gender column some values are in caps some not
# we dont know if the vetek column is in years or months or whatever
# we have missing values in the birthdate and gender columns

# lets start by removing the irrelevant column
kviut_drivers = kviut_drivers.loc[:, ~kviut_drivers.columns.str.contains('^Unnamed')]
kviut_drivers.dropna(how='all', inplace=True)

# lets check what different ways to write gender we got
print(kviut_drivers['gender'].value_counts())
kviut_drivers['gender'].replace(['male', 'boy', 'm'], 'M', inplace=True)
kviut_drivers['gender'].replace(['female', 'girl', 'woman'], 'F', inplace=True)
kviut_drivers['gender'].replace(['none'], 'unknown', inplace=True)

# lets the deal with the string date column
kviut_drivers['birthdate'] = pd.to_datetime(kviut_drivers['birthdate'], format='mixed', dayfirst=True , errors='coerce')

# now that we can work with the dataset lets continue with the previous process
print(kviut_drivers.isnull().sum())
kviut_drivers['gender'] = kviut_drivers.loc[:, ['gender']].fillna(value='unknown')

print(kviut_drivers['id'].duplicated().sum())

print(check_outlier_iqr(kviut_drivers["vetek"], kviut_drivers))
# no outlier! and that means we are done with another dataset and we can move on to the next one
new_drivers = pd.read_csv(r"C:\Users\liorl\Desktop\New folder\training\2 - Python\2.6 - Exercise\new_drivers.csv")

print(new_drivers.head())
print(new_drivers.describe())
print(new_drivers.info())

# omg! what's going on here!
# let's fix this mess :o
new_drivers = new_drivers.loc[:, ~new_drivers.columns.str.contains('^Unnamed')]
new_drivers.dropna(how='all', inplace=True)

print(new_drivers['gender'].value_counts())
new_drivers['gender'].replace(['male', 'boy', 'm'], 'M', inplace=True)
new_drivers['gender'].replace(['woman'], 'F', inplace=True)
new_drivers['birthdate'] = pd.to_datetime(new_drivers['birthdate'], format='mixed', dayfirst=True , errors='coerce')

print(new_drivers.isnull().sum())
new_drivers['gender'] = new_drivers.loc[:, ['gender']].fillna(value='unknown')

print(new_drivers['id'].duplicated().sum())
print(check_outlier_iqr(new_drivers["vetek"], new_drivers))

merged_drivers = [kviut_drivers, new_drivers]
merged_drivers = pd.concat(merged_drivers)

mask = merged_drivers.birthdate == '1900-01-01'
merged_drivers.loc[mask, 'birthdate'] = None

merged_drivers.to_csv('drivers.csv')
