from parser import parseFile

from keras.models import Sequential
from keras.layers import Dense
import numpy
import math

def heatingToInt(s : str) -> int:
  m = {
    'Kat Kaloriferi': 0,
    'Yok': 1,
    'Merkezi': 2,
    'Kombi': 3,
    'Soba': 4,
  }
  return m[s]

def preprocess(l : list) -> tuple:
  x = []
  y = []
  for house in l:
    newhouse = {}
    newhouse['furnished'] = int(house['furnished'])
    newhouse['heating'] = heatingToInt(house['heating'])
    nrsplit = house['numrooms'].split()
    newhouse['numrooms'] = int(nrsplit[0]) + int(nrsplit[2])
    newhouse['m2'] = house['m2']
    newhouse['floor'] = house['floor']
    newhouse['age'] = house['age']
    x.append(newhouse)
    y.append(house['price'])
  return (x, y)

def findStats(l : list, keys) -> tuple:
  means = {}
  for key in keys:
    means[key] = 0
    for house in l:
      means[key] += float(house[key])
  for key in keys:
    means[key] /= len(l)
  sds = {}
  for key in keys:
    sds[key] = 0
    for house in l:
      sds[key] += (float(house[key])-means[key])**2
  for key in keys:
    sds[key] = (sds[key]/(len(l)-1))**0.5
  #print('statistic info : ')
  #print(means, sds)
  return (means, sds)

def softmax(x, mean, sd) -> float:
  return 1/(1+math.exp(-(x-mean)/sd))

(data, prices) = preprocess(parseFile('database.txt'))
#print(data)
#print(prices)
matdata = numpy.zeros((len(data), 10))
matprices = numpy.zeros((len(data)))
(means, sds) = findStats(data, ['floor', 'm2', 'age', 'numrooms'])
priceMean = numpy.mean(prices)
priceSD = numpy.std(prices)

for (i, house) in enumerate(data):
  matdata[i][0] = house['furnished']
  matdata[i][1] = softmax(house['floor'], means['floor'], sds['floor'])
  matdata[i][2] = softmax(house['m2'], means['m2'], sds['m2'])
  matdata[i][3] = softmax(house['age'], means['age'], sds['age'])
  for j in range(4, 9):
    matdata[i][j] = 0
  matdata[i][4+house['heating']] = 1
  matdata[i][9] = softmax(house['numrooms'], means['numrooms'], sds['numrooms'])

  matprices[i] = softmax(prices[i], priceMean, priceSD)

print(matdata)
print(matprices)

model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=10))
model.add(Dense(units=1, activation='softmax'))

model.compile(loss='mean_squared_error',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(matdata, matprices, epochs=5, batch_size=32)
loss_and_metrics = model.evaluate(matdata, matprices, batch_size=128) # Ideally, we should have a seperate test set here.
print(loss_and_metrics)
