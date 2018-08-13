import requests
import csv
import json
import time
import datetime
import talib
start = int(round(time.time() * 1000))-600000
end = int(round(time.time() * 1000))
# r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/trades')
print(start)
print(end)

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
API_TOCKEN = '3fcdf0c7-078b-43b0-a09b-ffc6143573e9'
SECRET_KEY = '9akSvT8klk3SxE0YneRHS+WVk3Lv462SNt/jM9bRa8S5fMiXxIwxYPk5teMrGxz6Xxuq+MBcuIIhUK0GOz6mVg=='
r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/candles?start='+str(start)+'&end='+str(end)+'&interval=1')

print(r.text)
print(int(round(time.time() * 1000)))

price_list = r.json()
print(len(price_list))
print(price_list[0][4])



import time, base64, hmac, hashlib
# nonce = str(time.time())
# def get_signiture():
#
#     method = 'GET'
#     request_path = '/balances'
#
#     what = nonce + method + request_path # + request_body
#     key = base64.b64decode(SECRET_KEY)
#     signature = hmac.new(SECRET_KEY.encode('utf-8'), what.encode('utf-8'), hashlib.sha512)
#     return base64.b64encode(signature.digest())
#
# a = get_signiture()
# print(a)
# print(str(a)[2:-1])
# url = 'https://api.gopax.co.kr/balances'
# headers = {'API-KEY': API_TOCKEN, 'Accept': 'application/json','SIGNATURE':str(a)[2:-1],'NONCE':nonce,'Content-Type':'application/json'}
# response = requests.get(url, headers=headers)

# print(response.json())

# 발급받은 api키와 시크릿키를 입력한다
apikey = '3fcdf0c7-078b-43b0-a09b-ffc6143573e9'
secret = '9akSvT8klk3SxE0YneRHS+WVk3Lv462SNt/jM9bRa8S5fMiXxIwxYPk5teMrGxz6Xxuq+MBcuIIhUK0GOz6mVg=='

# nonce값 생성
nonce = str(time.time())
method = 'POST'
request_path = '/orders'

request_body = {
  "type": 'market',
  "side": 'bid',
  "price":7000000,
  "amount": 5000,
  "tradingPairName":'BTC-KRW'
}

#필수 정보를 연결하여 prehash 문자열을 생성함
what = nonce + method + request_path + json.dumps(request_body,sort_keys=True)
#base64로 secret을 디코딩함
key = base64.b64decode(secret)
#hmac으로 필수 메시지에 서명하고
signature = hmac.new(key, str(what).encode('utf-8'), hashlib.sha512)
#그 결과물을 base64로 인코딩함
signature_b64 = base64.b64encode(signature.digest())

custom_headers = {
	'API-Key': apikey,
	'Signature': signature_b64,
	'Nonce': nonce
}
#
# req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = custom_headers)



req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = custom_headers,json=request_body)

print(req.json())