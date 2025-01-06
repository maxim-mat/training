import numpy as np
import pandas as pd


def calc_drive_payment(drive):
    BASIC_TAARIF_KM = 200
    if drive['km'] < BASIC_TAARIF_KM:
        payment = drive['km'] * drive['basic_taarif']
    else:
        payment = BASIC_TAARIF_KM * drive['basic_taarif']
        payment += (drive['km'] - BASIC_TAARIF_KM) * drive['extra_milage']
    if not drive['day']:
        payment += (payment * drive['night_bonus'] / 100)
    if not drive['weekday']:
        payment += (payment * drive['weekend_bonus'] / 100)
    return payment


month_tracks = pd.read_csv(r"monthTracks.csv")
drivers = pd.read_csv(r"drivers.csv")
taarif = pd.read_csv(r"taarif.csv")
merged_drivers = drivers

# cleaning the month tracks
month_tracks = month_tracks.loc[:, ~month_tracks.columns.str.contains('^Unnamed')]
month_tracks.dropna(how='all', inplace=True)
month_tracks.drop_duplicates(inplace=True)

# converting all the string dates to datetime
month_tracks['start_time'] = pd.to_datetime(month_tracks['start_time'], format='mixed', dayfirst=True , errors='coerce')
month_tracks['end_time'] = pd.to_datetime(month_tracks['end_time'], format='mixed', dayfirst=True , errors='coerce')
month_tracks['time'] = pd.to_datetime(month_tracks['time'], format='mixed', dayfirst=True)
month_tracks['km'] = month_tracks['km'] / 1.609

# adding flags to see if drives were during night/weekends
SATURDAY = 5
NIGHT_END = 6
NIGHT_START = 22

month_tracks['weekday'] = np.where((month_tracks['time'].dt.dayofweek != SATURDAY), True, False)
month_tracks['day'] = np.where((month_tracks['start_time'].dt.hour.between(NIGHT_END, NIGHT_START)), True, False)

month_tracks = pd.merge(month_tracks, taarif, left_on='customer', right_on='customer', how='left')
month_tracks['total_income'] = month_tracks.apply(calc_drive_payment, axis=1)

# grouping by month and driver
temp = \
    month_tracks.groupby(by=[month_tracks['time'].dt.month, month_tracks['time'].dt.year, month_tracks['driver_id']])[
        ['km', 'total_income']].sum()
temp = temp.rename_axis(['month', 'year', 'driver_id']).reset_index()
summary = pd.merge(temp, merged_drivers, left_on='driver_id', right_on='id', how='left').drop('id', axis=1)

summary["month"] = summary["month"].astype(str) + "/" + summary["year"].astype(str)
summary.drop('year', axis=1, inplace=True)

# fixing up row names and dtypes
summary = summary.rename(columns={"km": "total_km"})
summary['birthdate'] = pd.to_datetime(summary['birthdate'], format='mixed', dayfirst=True , errors='coerce')
summary['vetek'] = round(summary['vetek'] / 12 , 1)

date_now = pd.to_datetime('now')
summary['birthdate'] = (date_now.year - summary['birthdate'].dt.year) - (date_now.month - summary['birthdate'].dt.month)
summary = summary.rename(columns={"birthdate": "age"})

# dropping unnecessary columns added in merges
summary = summary.loc[:, ~summary.columns.str.contains('^Unnamed')]
summary.to_csv('summary.csv')



