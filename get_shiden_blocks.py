import subprocess
from pprint import pprint
import json

block_num = 3
bashCommand = """
                curl -X POST 'https://polkadot.api.subscan.io/api/scan/block' \
                  --header 'Content-Type: application/json' \
                 
                  --data-raw '{
                        "block_num": 3
                  }'
              """
# "block_num": """ + str(block_num) + """
# "block_hash" = "0xd1fdaa4297685c97d96eac68a9087bad171a9435c2b89ef309d9df8e993a4298"
# "hash" = "0xd1fdaa4297685c97d96eac68a9087bad171a9435c2b89ef309d9df8e993a4298"
# "row": 1,
# "page": 0
result_raw = subprocess.run(
    bashCommand,
    check=True,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding='utf-8',
)
result_str = result_raw.stdout
result_json = json.loads(result_str)
pprint(result_json)