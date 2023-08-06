import tkinter as tk
import typing

from models import *

from interface.styling import *

class WatchList(tk.Frame):
    def __init__(self, binance_contracts: typing.Dict[str, Contract], bitmex_contracts: typing.Dict[str, Contract], *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.binance_symbols = list(binance_contracts.keys())
        self.bitmex_symbols = list(bitmex_contracts.keys())

        self._commands_frame = tk.Frame(self, bg=BG_COLOUR)
        self._commands_frame.pack(side=tk.TOP)

        self._table_frame = tk.Frame(self, bg=BG_COLOUR)
        self._table_frame.pack(side=tk.TOP)

        self._binance_label = tk.Label(self._commands_frame, text='Binance', bg=BG_COLOUR, fg=FG_COLOUR, font=BOLD_FONT)
        self._binance_label.grid(row=0, column=0)

        self._binance_entry = tk.Entry(self._commands_frame, fg=BG_COLOUR, justify=tk.CENTER, insertbackground=FG_COLOUR, bg=BG_COLOUR_2)
        self._binance_entry.bind('<Return>', self._add_binance_symbol)
        self._binance_entry.grid(row=1, column=0)

        self._bitmex_label = tk.Label(self._commands_frame, text='Bitmex', bg=BG_COLOUR, fg=FG_COLOUR, font=BOLD_FONT)
        self._bitmex_label.grid(row=0, column=1)

        self._bitmex_entry = tk.Entry(self._commands_frame, fg=BG_COLOUR, justify=tk.CENTER, insertbackground=FG_COLOUR, bg=BG_COLOUR_2)
        self._bitmex_entry.bind('<Return>', self._add_bitmex_symbol)
        self._bitmex_entry.grid(row=1, column=1)

        self._headers = ['symbol', 'exchange', 'bid', 'ask']

        for idx, h in enumerate(self._headers):
            header = tk.Label(self._table_frame, text=h.capitalize(), bg=BG_COLOUR, fg=FG_COLOUR, font=BOLD_FONT)
            header.grid(row=0, column=idx)

    def _add_binance_symbol(self, event):

        symbol = event.widget.get()

        if symbol in self.binance_symbols:
            self._add_symbol(symbol, 'Binance')
            event.widget.delete(0, tk.END)

    def _add_bitmex_symbol(self, event):

        symbol = event.widget.get()

        if symbol in self.bitmex_symbols:
            self._add_symbol(symbol, 'Bitmex')
            event.widget.delete(0, tk.END)

    def _add_symbol(self, symbol:str, exchange: str):
        return
