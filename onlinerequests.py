import requests

API_KEY = '06c9HJ2r7mxAHkE6A542X7PyNGpGReu72VP9Xkzx'
HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=EUR%2CUSD%2CRUB%2CGBP'
response = requests.get(HOST)