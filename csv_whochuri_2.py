import pandas as pd
import numpy as np
idx = []
idx2 = []
count = 0
final_dat = []

data = pd.read_csv('interval_applied.csv',names=['x_coord','y_coord'])
data['index'] = 0

datalist = data.values.tolist()
size = len(datalist)

del datalist[0]
h = (datalist[-1][0]-datalist[0][0])//49

for i in range(0,50):
    idx.append(datalist[0][0]+h*i)

##################################같은 x에 대해 y차이가 4 넘으면 인덱스 추가#######################
for j in range(0,size-1):
    for i in range(0,49):
        if datalist[j][0]==idx[i]:
            if datalist[j+1][0]==datalist[j][0] and (datalist[j+1][1]-datalist[j][1])<4:
                datalist[j][2] = 1
            else:
                datalist[j][2] = 0


##################################중복 값 제거######################################
k = 0
while k <= size-1:
    if datalist[k][2] == 1:
        del datalist[k]
        k -= 1
    k += 1
    size = len(datalist)

data_array = np.array(datalist)
df_data = pd.DataFrame(data_array)

df_data.to_csv('fin.csv', index = False)