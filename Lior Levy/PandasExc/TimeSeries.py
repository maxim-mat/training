import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#3
apple = pd.read_csv('appl_1980_2014.csv')

#4
apple_dtypes = apple.dtypes

#5
apple['Date'] = pd.to_datetime(apple['Date'])

#6
apple.set_index('Date' , inplace=True)

#7
duplicates = apple.index.has_duplicates

#8
apple.sort_index(ascending= True , inplace=True)

#9
months_end = apple[(apple.index + pd.offsets.BMonthEnd(0)).day == apple.index.day]

#10
days_diff = (apple.tail(1).index.item() - apple.head(1).index.item()) / np.timedelta64(1, 'D')

#11
average_days_per_month = 30.44
months_in_data = round(days_diff / average_days_per_month)

#12
plt.plot(apple['Adj Close'])
plt.rcParams["figure.figsize"] = (13.5, 9)
plt.show()