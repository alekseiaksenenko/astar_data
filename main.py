import requests
from pprint import pprint

# url  = 'https://polkadot.api.subscan.io/api/now'
# url  = 'https://polkadot.api.subscan.io/api/scan/metadata'
url  = 'https://polkadot.api.subscan.io/api/scan/blocks'
headers = {
    'content-type': 'application/json',
}

data = {'data-raw': {
    "row": 10,
    "page": 0
}}
response = requests.post(
    url,
    data=data,
    headers=headers
)
pprint(response.json())

# --header 'Content-Type: application/json \
# --header 'X-API-Key: YOUR_KEY'