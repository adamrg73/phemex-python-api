import os 
import sys
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path + "/../")

from phemex.client import Client
from phemex.exceptions import PhemexAPIException

# Create a testnet client
client = Client("api_key", "api_secret", True)

# Get account and positions
r = client.query_account_n_positions(Client.CURRENCY_BTC)
print(r)
r = client.query_account_n_positions(Client.CURRENCY_USD)
print(r)
try:
    r = client.query_account_n_positions("BTC1")
    print(r)
except PhemexAPIException as e:
    print(e)
    
try:
    r = client.query_all_orders("BTC1")
    print(r)
except PhemexAPIException as e:
    print(e)
