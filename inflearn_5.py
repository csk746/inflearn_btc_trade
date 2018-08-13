
import requests
import time


while True:
    now_time = round(time.time() * 1000)
    start = int(now_time)-60*50*1000
    end = int(now_time)
    # print(start)
    # print(end)
    #
    r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/candles?start='+str(start)+'&end='+str(end)+'&interval=1')
    #
    # print(len(r.json()))

    arr = r.json()
    close_price_lsit = []
    for ar in arr:
        close_price_lsit.append(ar[4])
        # print(ar)

    # print(close_price_lsit)
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

    avg_min_15 = sum(close_price_lsit[-15:])/15
    avg_min_50 = sum(close_price_lsit[-50:])/50
    #
    print(avg_min_15)
    print(avg_min_50)

    if avg_min_15 > avg_min_50 * 1.004:
        print('매수')

    if avg_min_50 > avg_min_15:
        print('매도')

    time.sleep(5)



