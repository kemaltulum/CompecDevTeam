import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("input/data_homes.csv")

print(data.columns.values)

# print(data.tail())

# print(data.info())

# print(data.describe())

# print(data.describe(include=['O']))

# print(data)

# data[['Rooms',  'Area']] .groupby(['Rooms'], as_index=False) .mean().sort_values(by='Area', ascending=False)

# pd.crosstab(data['Rooms'], data['Heating'])

# data.groupby(['Rooms'], as_index=False).count()

data['Rooms'] = data['Rooms'].replace(['10+5', '3+3', '31+1', '2+2', '5+4', '6+3'], 'Rare')
data['Rooms'] = data['Rooms'].replace(['4+2', '3+2'], '4+1')

room_mapping = {"1+1": 2, "2+1": 3, "3+1": 4, "4+1": 5, "Rare": 6}
data['Rooms'] = data['Rooms'].map(room_mapping)

# data.groupby(['Heating'], as_index=False).mean()
# data.groupby(['Heating'], as_index=False).count()


data = data.drop(['Heating'], axis=1)

# data.to_csv("input/stripped_home_data.csv")


npMatrix = np.matrix(data)
X, Y = npMatrix[:,1:4], npMatrix[:,0]
mdl = LinearRegression().fit(X,Y) # either this or the next line
m = mdl.coef_[0]
b = mdl.intercept_

def func(theta, rooms, area, year):
    return theta[0] + theta[1]*rooms + theta[2]*area + theta[3]*year

theta = []
theta.append(mdl.intercept_[0])
for coef in mdl.coef_[0]:
    theta.append(coef)


print(func(theta, 5, 140, 32))




