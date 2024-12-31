import numpy as np
import pandas as pd

#3
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris = pd.read_csv(url)

#4
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

#5
missing_values =  iris.isnull().sum()

#6
iris.loc[9:28, 'petal_length'] = np.nan

#7
iris = iris.fillna(1.0)

#8
iris = iris.drop('class', axis=1)

#9
iris.loc[0:2] = np.nan

#10
iris = iris.dropna()

#11
iris.reset_index(inplace=True)








