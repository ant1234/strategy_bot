import tkinter as tk 
import typing
from interface.styling import *

class StrategyEditor(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._commands_frame = tk.Frame(self, bg=BG_COLOUR)
        self._commands_frame.pack(side=tk.TOP)

        self._table_frame = tk.Frame(self, bg=BG_COLOUR)
        self._table_frame.pack(side=tk.TOP)

        self._add_button = tk.Button(self._commands_frame, text="Add Strategy", font=GLOBAL_FONT, command=self._add_strategy_row, bg=BG_COLOUR_2, fg=FG_COLOUR)

        self._add_button.pack(side=tk.TOP)

        self.body_widgets = dict()

        self._headers = ['Strategy', 'Contract', 'Timeframe', 'Balance %', 'Take Profit %', 'Stop Loss %']

        for idx, h in enumerate(self._headers):
            header = tk.Label(self._table_frame, text=h, bg=BG_COLOUR, fg=FG_COLOUR, font=BOLD_FONT)
            header.grid(row=0, column=idx)

        for h in self._headers:
            self.body_widgets[h] = dict()
            if h in ['bid', 'ask']:
                self.body_widgets[h + '_var'] = dict()

        self._body_index = 1

    def _add_strategy_row():
        return