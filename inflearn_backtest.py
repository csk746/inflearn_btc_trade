
import requests
import time
import time, base64, hmac, hashlib, requests, json
import telegram

# talib 불러오기
import talib
import numpy as np

apikey = ''
secret = ''

my_token = ''
chat_id = ''

bot = telegram.Bot(token = my_token)
is_buy = False
message = '트레이딩 봇 시작!'

# bot.sendMessage(chat_id=chat_id, text=message)
rsi_status = ''
def buy_test(amount,price):
    print('{} 매수!'.format(price))
def sell_test(amount,price):
    print('{} 매도!'.format(price))

now_time = round(time.time() * 1000)
# 1000 이 1초
# 60*1000 이 1분
# 60*60*1000 이 1시간
start = int(now_time)-60*60*1000*1000
end = int(now_time)
# print(start)
# print(end)
r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/candles?start='+str(start)+'&end='+str(end)+'&interval=30')

arr = r.json()
# print(len(r.json()))
close_price_list = []

for ar in arr:
    close_price_list.append(float(ar[4]))
    close_price_list_nparr = np.array(close_price_list, dtype='f8')
    output = talib.SMA(close_price_list_nparr)

    # rsi 계산
    rsi = talib.RSI(close_price_list_nparr,timeperiod = 14)
    # print(close_price_list[-1])

    if rsi[-1] < 30:
        rsi_status='low'
    elif 30<=rsi[-1]<70:
        if rsi_status == 'low'and is_buy == False:
            # buy_test(0.001, close_price_list[-1])
            print('rsi 상향 돌파')
        if rsi_status == 'high' and is_buy == True:
            sell_test(0.001, close_price_list[-1])
            is_buy = False
        rsi_status = 'middle'
    else:
        rsi_status = 'high'
    avg_min_15 = sum(close_price_list[-15:]) / 15
    avg_min_50 = sum(close_price_list[-50:]) / 50
    if avg_min_15 > avg_min_50 * 1.004 and is_buy == False:
        is_buy = True
        buy_test(0.001,close_price_list[-1])
    # print(output)
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


    #
    # print(avg_min_15)
    # print(avg_min_50)


    # if avg_min_15 > avg_min_50 * 1.004 and is_buy == False:
    #     buy(0.001,close_price_list[-1])
    #
    # if avg_min_50 > avg_min_15 and is_buy == True:
    #     sell(0.001,close_price_list[-1])






