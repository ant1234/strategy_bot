import logging
import os
from dotenv import load_dotenv

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root

# Load environment variables from .env file
load_dotenv()

binance_public_key = os.environ.get('BINANCE_TESTNET_PUBLIC_KEY')
binance_secret_key = os.environ.get('BINANCE_TESTNET_SECRET_KEY')
bitmex_public_key =  os.environ.get('BITMEX_TESTNET_PUBLIC_KEY')
bitmex_secret_key = os.environ.get('BITMEX_TESTNET_SECRET_KEY')

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceClient(binance_public_key, binance_secret_key, testnet=True, futures=False)
    bitmex = BitmexClient(bitmex_public_key, bitmex_secret_key, testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()