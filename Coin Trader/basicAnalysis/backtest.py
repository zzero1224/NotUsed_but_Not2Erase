import pyupbit
import numpy as np

# 7일간 리플 코인의 코인 시장에서 open시가 high고가 low저가 close종가 volume거래량
df = pyupbit.get_ohlcv("KRW-XRP", count=10)

# let parameter k = 0.5
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0005
# where --> 3항 연산자마냥 조건문, 참일 때, 거짓일 때
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target']-0.0005, 1)
# df['close'] / df['target'] : 수익률

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD : max draw down
print("MDD(%): ", df['dd'].max())
df.to_excel("draw_down.xlsx")