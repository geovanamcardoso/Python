import requests
import json

url = 'http://dummyjson.com/products?limit=100'
try:
    req = requests.get(url)
    if req.status_code == 200:
        dic = req.json()