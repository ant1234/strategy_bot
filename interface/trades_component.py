import tkinter as tk
import typing

from interface.styling import * 

class TradeWatch(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.body_widgets = dict()
        self._headers = ['times', 'symbol', 'exchange', 'strategy', 'side', 'quantity', 'status', 'pnl']

        self._table_frame = tk.Frame(self, bg=BG_COLOUR)
        self._table_frame.pack(side=tk.TOP)


        for idx, h in enumerate(self._headers):
            header = tk.Label(self._table_frame, text=h.capitalize(), bg=BG_COLOUR, fg=FG_COLOUR, font=BOLD_FONT)
            header.grid(row=0, column=idx)

        for h in self._headers:
            self.body_widgets[h] = dict()
            if h in ['status', 'pnl']:
                self.body_widgets[h + '_var'] = dict()

        self._body_index = 1

    def add_trade(self, data: typing.Dict):

        b_index = self._body_index
        t_index = data['time']

        self.body_widgets['time'][t_index] = tk.Label(self._table_frame, text=data['time'], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['time'][t_index].grid(row=b_index, column=0)

        self.body_widgets['symbol'][t_index] = tk.Label(self._table_frame, text=data['symbol'], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['symbol'][t_index].grid(row=b_index, column=1)

        self.body_widgets['exchange'][t_index] = tk.Label(self._table_frame, text=data['exchange'], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['exchange'][t_index].grid(row=b_index, column=2)

        self.body_widgets['strategy'][t_index] = tk.Label(self._table_frame, text=data['strategy'], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['strategy'][t_index].grid(row=b_index, column=3)

        self.body_widgets['side'][t_index] = tk.Label(self._table_frame, text=data['side'], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['side'][t_index].grid(row=b_index, column=4)

        self.body_widgets['quantity'][t_index] = tk.Label(self._table_frame, text=data['quantity'], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['quantity'][t_index].grid(row=b_index, column=5)

        self.body_widgets['status_var'][t_index] = tk.StringVar()
        self.body_widgets['status'][t_index] = tk.Label(self._table_frame, textvariable=self.body_widgets['status_var'][t_index], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['status'][t_index].grid(row=b_index, column=6)

        self.body_widgets['pnl_var'][t_index] = tk.StringVar()
        self.body_widgets['pnl'][t_index] = tk.Label(self._table_frame, textvariable=self.body_widgets['pnl_var'][t_index], bg=BG_COLOUR, fg=FG_COLOUR_2, font=GLOBAL_FONT)
        self.body_widgets['pnl'][t_index].grid(row=b_index, column=7)

        self._body_index += 1
