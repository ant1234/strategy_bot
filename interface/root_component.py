import tkinter as tk
import time
from interface.styling import *
from interface.logging_component import Logging
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex_futures import BitmexFuturesClient

class Root(tk.Tk):
    def __init__(self, binance: BinanceFuturesClient, bitmex: BitmexFuturesClient):
        super().__init__()

        self.binance = binance
        self.bitmex = bitmex

        # title
        self.title('Trading Bot')

        # configure colours
        self.configure(bg=BG_COLOUR)

        # layout
        self._left_frame = tk.Frame(self, bg=BG_COLOUR)
        self._left_frame.pack(side=tk.LEFT)

        self._right_frame = tk.Frame(self, bg=BG_COLOUR)
        self._right_frame.pack(side=tk.LEFT)

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




            
