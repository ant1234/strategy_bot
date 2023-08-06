import tkinter as tk
from interface.styling import *
from interface.logging_component import Logging

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

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




            
