import logging
import requests
import pprint

logger = logging.getLogger()

# "https://fapi.binance.com"
# "https://testnet.binancefuture.com"

def get_contracts():

    "Get a list of futures from wss://fstream.binance.com."
    contracts = []

    # Reach out to the binance futures api and get a list of futures contracts.
    response_object = requests.get('https://fapi.binance.com/fapi/v1/exchangeInfo')

    for binance_contract in response_object.json()['symbols']:
        contracts.append(binance_contract['pair'])
    
    return contracts
