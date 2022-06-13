import matplotlib.pyplot as plt
import json
import numpy as np

def getDeprecatedArray(values):
    array = json.loads(values)['results']
    res = [];
    for el in array:
        res.append(el['deprecated'])
    return res


def getNormalArray(values):
    array = json.loads(values)['results']
    res = [];
    for el in array:
        res.append(el['normal'])
    return res


def getPrefferedArray(values):
    array = json.loads(values)['results']
    res = [];
    for el in array:
        res.append(el['preferred'])
    return res

values = '{"results": [{"normal": 176, "preferred": 0, "deprecated": 10, "count": 176, "name":"Q123"},{"normal": 176, "preferred": 0, "deprecated": 3, "count": 176, "name":"Q124"}]}'
ind = np.arange(2)  # the x locations for the groups
  

plt.figure()
plt.bar(ind, getDeprecatedArray(values), tick_label ='deprecated',width= 0.7, color = 'red')

plt.figure()
plt.bar(ind, getNormalArray(values) ,tick_label ='normal',width= 0.7, color = 'yellow')

plt.figure()
plt.bar(ind, getPrefferedArray(values), tick_label ='preferred',width= 0.7, color = 'green')

  
# naming the x-axis
plt.xlabel('Entities-Rank')
# naming the y-axis
plt.ylabel('Values')
# plot title
plt.title('Rankings distribution')
  
# function to show the plot
plt.show()

