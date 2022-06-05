import requests
from pprint import pprint
import json

# url  = 'https://moonriver.api.subscan.io/api/scan/block'
url  = 'https://shiden.api.subscan.io/api/scan/block'
# url  = 'https://polkadot.api.subscan.io/api/scan/extrinsic'
# url = 'https://shiden.api.subscan.io/api/scan/metadata'
headers = {
    'content-type': 'application/json',

}
data = {

    # "extrinsic_index": r'2028659-2'
# 1465413-2
#     "block_num": 100
    "block_num": 541319
    # "block_num": 1465063
    # "block_hash": "0xa029cf076c8c602f2ed5a766a95796a26c695308fda83da0830954efc4c2a2cb"
    # "block_num": 9630845
    # "block_hash": "0x56cca580b4484680a64777651680082b8f6bf482aee4d41b48976283c0fcf958"
}
headers = None
response = requests.post(
    url,
    headers=headers,
    data=json.dumps(data)
)

# for i in response.json()['data']:
#     pprint(i)
# pprint(response.json()['data']['extrinsics'])
pprint(response.json()['data'])
# pprint(response.json())
