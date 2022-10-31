import pyupbit

access = "RezwD3ZpSnG7x4xxb6rP3tBL0aXxEA5xQDWYoKax"
secret = "xcwRigN9QfxxgAQa4tiNrcFdh8UJ6XB7AhbcySmR"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-DOGE"))     # KRW-DOGE 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회