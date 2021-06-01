import pandas as pd
import numpy as np
idx = []
count = 0
final_dat = []

data = pd.read_csv('interval_applied.csv',names=['x_coord','y_coord'])
data['index'] = 0

datalist = data.values.tolist()
del datalist[0]
size = len(datalist)

h = (datalist[-1][0]-datalist[0][0])//49

for i in range(0,50):
    idx.append(datalist[0][0]+h*i)

##################################같은 x에 대해 y차이가 4 넘으면 인덱스 추가#######################
for j in range(0,size-1):
    for i in range(0,49):
        if datalist[j][0]==idx[i]:
            if (datalist[j+1][1]-datalist[j][1]) < 4:
                datalist[j][2] = count
            else:
                datalist[j][2] = count
                count = count+1

'''
for i in range(0,49):
    for j in range(0,size-1):
        if datalist[j][0]==idx[i]:
            if datalist[j][2] == datalist[j+1][2]:
                datalist[j][0]  = 0
'''

data_array = np.array(datalist)
df_data = pd.DataFrame(data_array)

df_data.to_csv('fin2.csv', index = False)