import numpy as np
import pandas as pd
import cv2

#count는 횟수 맞나 확인하려 넣은 것, 무의미한 값
count = 1
black_coord = []
#opencv는 이미지의 좌측 상단을 원점으로 설정하고 좌표를 잡습니다
#x는 우로 갈 수록, y는 아래로 갈 수록 증가합니다.

image = cv2.imread('image.jpg')
img_h, img_w, img_c = image.shape
half_h = img_h//2
half_w = img_w//2

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#img_array = np.array(gray)
#size = img_array.shape

newimage = np.zeros((half_h, half_w), dtype = image.dtype)
new_h = img_h//half_h
new_w = img_w//half_w


for j in range(half_h):
    for i in range(half_w):
        y = j*new_h
        x = i*new_w
        pixel = image[y:y+new_h, x:x+new_w]
        newimage[j, i]=pixel.sum(dtype='int64')//(new_h*new_w)

cv2.imshow('s', newimage)
cv2.waitKey()
cv2.destroyAllWindows()
#new_gray = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
newimg_array = np.array(newimage)
newsize = newimg_array.shape

for i in range(0, newsize[0]-1):
    for j in range(0, newsize[1]-1):
        if newimg_array[i, j] == 0:
            black_coord.append([i, j])
            count = count+1

blk_coord_array = np.array(black_coord)

df_img = pd.DataFrame(newimg_array)
df_coord = pd.DataFrame(blk_coord_array)
#어레이에 저장된 이미지의 색상값이 img.csv에 저장됨
df_img.to_csv('new_img.csv', index=False)
#어레이에 저장된 좌표 데이터가 저장됨
df_coord.to_csv('new_coordinate.csv', index=False)
