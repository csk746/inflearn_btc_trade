#
# 주문 등록하기
#
import time, base64, hmac, hashlib, requests, json

# 발급받은 api키와 시크릿키를 입력한다
apikey = ''
secret = ''

# nonce값 생성
nonce = str(time.time())
method = 'POST'
request_path = '/orders'

request_body = {
    "amount": 0.001,
    "price": 7000000,
    "side": "buy",
    "tradingPairName": "BTC-KRW",
    "type": "limit"
};

# 필수 정보를 연결하여 prehash 문자열을 생성함
what = nonce + method + request_path + json.dumps(request_body, sort_keys=True)
# base64로 secret을 디코딩함
key = base64.b64decode(secret)
# hmac으로 필수 메시지에 서명하고
signature = hmac.new(key, str(what).encode('utf-8'), hashlib.sha512)
# 그 결과물을 base64로 인코딩함
signature_b64 = base64.b64encode(signature.digest())

custom_headers = {
    'API-Key': apikey,
    'Signature': signature_b64,
    'Nonce': nonce
}

req = requests.post(url = 'https://api.gopax.co.kr' + request_path, headers = custom_headers,json=request_body)

print(req.json())