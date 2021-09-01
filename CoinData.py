import requests
endpoint = 'https://www.coinspot.com.au/api/ro'
headers = {
    'key': '',
    'sign': hmac.new(secret, hashlib.sha512).hexdigest(),
    }
r = request.get(endpoint, )
r.headers

print(r)
