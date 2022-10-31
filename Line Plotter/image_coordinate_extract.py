import numpy as np
import pandas as pd
import cv2

#count는 횟수 맞나 확인하려 넣은 것, 무의미한 값
count = 1
black_coord = []
interval_coord = []
#opencv는 이미지의 좌측 상단을 원점으로 설정하고 좌표를 잡습니다
#x는 우로 갈 수록, y는 아래로 갈 수록 증가합니다.

image = cv2.imread('image4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_array = np.array(gray)
size = img_array.shape

for i in range(0, size[0]-1):
    for j in range(0, size[1]-1):
        if img_array[i, j] == 0:
            black_coord.append([j, i])
            count = count+1

h = (max(black_coord[:])[0]-min(black_coord[:])[0])//50
for k in range(0,50):
    for [p, q] in black_coord:
        if p == min(black_coord[:])[0]+h*k:
            interval_coord.append([p,q])

blk_coord_array = np.array(black_coord)
itv_coord_array = np.array(interval_coord)

df_itv = pd.DataFrame(itv_coord_array)
df_img = pd.DataFrame(img_array)
df_coord = pd.DataFrame(blk_coord_array)
#어레이에 저장된 이미지의 색상값이 img.csv에 저장됨
df_img.to_csv('img.csv', index=False)
#어레이에 저장된 좌표 데이터가 저장됨
df_coord.to_csv('coordinates.csv', index=False)

######## 요 파일이 사용하는 인터벌 파일 ################
df_itv.to_csv('interval_applied.csv', index = False)
