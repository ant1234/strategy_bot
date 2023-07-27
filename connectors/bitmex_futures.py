import logging
import requests
import pprint

def get_contracts(): 

    contracts = [] 

    # Reach out to the binance futures api and get a list of futures contracts 
    response_object = requests.get('https://www.bitmex.com/api/v1/instrument/active')

    if(response_object.status_code == 200):

        for binance_contract in response_object.json(): 
            contracts.append(binance_contract['symbol'])

        return contracts


