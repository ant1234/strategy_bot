import tkinter as tk
import logging
import pprint
import os
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex_futures import BitmexFuturesClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables for binance.
binance_testnet_public_key = os.environ.get('BINANCE_TESTNET_PUBLIC_KEY')
binance_testnet_secret_key = os.environ.get('BINANCE_TESTNET_SECRET_KEY')

# Access environment variables for bitmex.
bitmex_testnet_public_key = os.environ.get('BITMEX_TESTNET_PUBLIC_KEY')
bitmex_testnet_secret_key = os.environ.get('BITMEX_TESTNET_SECRET_KEY')

# logging used for debugging. 
logger = logging.getLogger()

# set logging level to show info logging in the console.
logger.setLevel(logging.DEBUG)

# show time, level names and messages 
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# output logging messages to file.
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient(binance_testnet_public_key, binance_testnet_secret_key, True)
    bitmex = BitmexFuturesClient(bitmex_testnet_public_key, bitmex_testnet_secret_key, True)

    # print(bitmex.contracts['XBTUSD'].base_asset, bitmex.contracts['XBTUSD'].price_decimals)
    # print(bitmex.balances['XBt'].wallet_balance)

    # print(bitmex.place_order(bitmex.contracts['XBTUSD'], 'Limit', 100, 'Buy', price=20000, tif='GoodTillCancel'))
    print(bitmex.cancel_order('d98cfcd4-8690-47e4-acc6-dcbfc8108287').status)


    # tkinter ui.
    root = tk.Tk()

    # prevent termination of program after running.
    root.mainloop()