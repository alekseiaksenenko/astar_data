import subprocess
from pprint import pprint
import json
import io

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/now' \
#                   --header 'Content-Type: application/json'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/metadata' \
#                     --header 'Content-Type: application/json'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/now' \
#                   --header 'Content-Type: application/json'
#               """

# "row": 10,
#                     "page": 955378
block_num = 3
bashCommand = """
                curl -X POST 'https://polkadot.api.subscan.io/api/scan/block' \
                  --header 'Content-Type: application/json' \
                  --header 'X-API-Key: YOUR_KEY' \
                  --data-raw '{
                    "block_num": """ + str(block_num) + """
                  }'
              """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/extrinsics' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "row": 1,
#                     "page": 1
#                   }'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/extrinsic' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "extrinsic_index": "2028659-2"
#                   }'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/events' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "row": 10,
#                     "page": 1
#                   }'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/event' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "event_index": "2013673-2"
#                   }'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/v2/scan/search' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "key": "1REAJ1k691g5Eqqg9gL7vvZCBG7FCCZ8zgQkZWd4va5ESih"
#                   }'
#               """

# "category": "transfer"
# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/daily' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "start": "2020-07-03",
#                     "end": "2020-07-04",
#                     "format": "day"
#                   }'
#               """



# # curl -X POST 'https://polkadot.api.subscan.io/api/scan/accounts' \
# #   --header 'Content-Type: application/json' \
# #   --header 'X-API-Key: YOUR_KEY' \
# #   --data-raw '{
# #     "row": 1,
# #     "page": 1
# #   }'
# """
# """
# bashCommand = """
#                   curl -X POST 'https://polkadot.api.subscan.io/api/v2/scan/accounts' \
#                       --header 'Content-Type: application/json' \
#                       --header 'X-API-Key: YOUR_KEY' \
#                       --data-raw '{
#                         "row": 1,
#                         "page": 0
#                       }'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/staking_history' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "row": 20,
#                     "page": 0,
#                     "address": "165LPQijvZdnmxcuCfxGWvcoSVtoJnCFm1UjjijzsSGGAk22"
#                   }'
#               """

# bashCommand = """
#                 curl -X POST 'https://polkadot.api.subscan.io/api/scan/staking/nominator' \
#                   --header 'Content-Type: application/json' \
#                   --header 'X-API-Key: YOUR_KEY' \
#                   --data-raw '{
#                     "address": "165LPQijvZdnmxcuCfxGWvcoSVtoJnCFm1UjjijzsSGGAk22"
#                   }'
#               """


result = subprocess.run(
    bashCommand,
    check=True,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding='utf-8',
)
result = result.stdout
result = json.loads(result)
pprint(result)