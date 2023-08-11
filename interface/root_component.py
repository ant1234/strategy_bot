import tkinter as tk
import time
from interface.styling import *
from interface.logging_component import Logging
from interface.watchlist_component import WatchList
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex_futures import BitmexFuturesClient

class Root(tk.Tk):
    def __init__(self, binance: BinanceFuturesClient, bitmex: BitmexFuturesClient):
        super().__init__()

        self.binance = binance
        self.bitmex = bitmex

        self.binance_contracts = binance.contracts
        self.bitmex_contracts = bitmex.contracts

        # title
        self.title('Trading Bot')

        # configure colours
        self.configure(bg=BG_COLOUR)

        # layout
        self._left_frame = tk.Frame(self, bg=BG_COLOUR)
        self._left_frame.pack(side=tk.LEFT)

        self._right_frame = tk.Frame(self, bg=BG_COLOUR)
        self._right_frame.pack(side=tk.LEFT)

        self._watchlist_frame = WatchList(self.binance_contracts, self.bitmex_contracts, self._left_frame)
        self._watchlist_frame.pack(side=tk.TOP)

        self._logging_frame = Logging(self._left_frame)
        self._logging_frame.pack(side=tk.TOP)

        self._update_ui()

    def _update_ui(self):

        for log in self.bitmex.logs:
            if not log['displayed']:
                self._logging_frame.add_log(log['log'])
                log['displayed'] = True

        for log in self.binance.logs:
            if not log['displayed']:
                self._logging_frame.add_log(log['log'])
                log['displayed'] = True

        self.after(1500, self._update_ui)

        # watchlist prices

        for key, value in self._watchlist_frame.body_widgets['symbol']. items():

            symbol = self._watchlist_frame.body_widgets['symbol'][key].cget('text')
            exchange = self._watchlist_frame.body_widgets['exchange'][key].cget('text')

            if exchange == 'Binance':
                if symbol not in self.binance.contracts:
                    continue

                if symbol not in self.binance.prices:
                    self.binance.get_bid_ask(self.binance.contracts[symbol])
                    continue

                prices = self.binance.prices[symbol]

            elif exchange == 'Bitmex':
                if symbol not in self.bitmex.contracts:
                    continue

                if symbol not in self.bitmex.prices:
                    continue

                prices = self.bitmex.prices[symbol]

            else:
                continue

            if prices['bid'] is not None:
                self._watchlist_frame.body_widgets['bid_var'][key].set(prices['bid'])

            if prices['ask'] is not None:
                self._watchlist_frame.body_widgets['ask_var'][key].set(prices['ask'])


            
