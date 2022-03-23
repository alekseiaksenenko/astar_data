import subprocess
from pprint import pprint
import json

block_num = 3
bashCommand = """
                curl -X POST 'https://shiden.api.subscan.io/api/scan/block' \
                  --header 'Content-Type: application/json' \
                  --header 'X-API-Key: YOUR_KEY' \
                  --data-raw '{
                    "block_num": """ + str(block_num) + """
                  }'
              """

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