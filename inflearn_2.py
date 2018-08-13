
import requests
import time


now_time = round(time.time() * 1000)
start = int(now_time)-60*10*1000
end = int(now_time)
print(start)
print(end)
#
r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/candles?start='+str(start)+'&end='+str(end)+'&interval=1')
#
print(len(r.json()))

arr = r.json()

for ar in arr:
    print(ar)

# [
#   [
#     <Time>,
#     <Low>,
#     <High>,
#     <Open>,
#     <Close>,
#     <Volume>
#   ],
#   [
#     1521004080000,
#     10081000,
#     10081000,
#     10081000,
#     10081000,
#     0.01
#   ]
# ]


