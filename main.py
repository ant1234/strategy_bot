import tkinter as tk
import logging
import pprint
import os
from connectors.binance_futures import BinanceFuturesClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
testnet_public_key = os.environ.get('BINANCE_TESTNET_PUBLIC_KEY')
testnet_secret_key = os.environ.get('BINANCE_TESTNET_SECRET_KEY')

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

    binance = BinanceFuturesClient(True)

    # pprint.pprint(binance.get_historical_candles('BTCUSDT', '1h'))

    # settings regarding the widget display.
    row_counter = 0
    column_counter = 0
    bitmex_contracts = bitmex_get_contracts()
    calibre_font = ('calibre', 11, 'normal')
    
    # tkinter ui.
    root = tk.Tk()
    root.configure(bg='grey12')

    for bitmex_contract in bitmex_contracts:

        # create a widget for displaying bitmex future contracts and styles.
        label_widget = tk.Label(root, 
                                text=bitmex_contract,
                                font=calibre_font, 
                                bg='grey12',
                                fg='SteelBlue1',
                                width=11)
        
        label_widget.grid(row=row_counter, 
                          column=column_counter, 
                          sticky='ew')

        # style the grid into 5 columns to limit rows all the way down the page.
        if row_counter == 5:
            column_counter += 1
            row_counter = 0
        else:
            row_counter += 1

    # prevent termination of program after running.
    root.mainloop()