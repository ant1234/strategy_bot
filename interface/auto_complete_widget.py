import tkinter as tk
import typing

class Autocomplete(tk.Entry):
    def __init__(self, symbols: typing.List[str], *args, **kwargs):

        super().__init__(*args, **kwargs)

        self._symbols = symbols

        self._lb: tk.Listbox
        self._lb_open = False

        self._var = tk.StringVar()
        self.configure(textvariable=self._var)
        self._var.trace("w", self._changed)

    def _changed(self, var_name: str, index: str, mode: str):

        self._var.set(self._var.get().upper())

        if self._var.get() == "":
            if self._lb_open:

                self._lb.destroy()
                self._lb_open = False
        else :

            if not self._lb_open:
                self._lb = tk.Listbox(height=8)
                self._lb.place(x=self.winfo_x() + self.winfo_width() - 55, y=self.winfo_y() + self.winfo_height() + 5)
                self._lb_open = True

            symbols_matched = [symbol for symbol in self._symbols if symbol.startswith(self._var.get())]

            if len(symbols_matched) > 0:

                try:
                    self._lb.delete(0, tk.END)
                except tk.TclError:
                    pass

                for symbol in symbols_matched:

                    self._lb.insert(tk.END, symbol)

            else:
                if self._lb_open:
                    self._lb.destroy()
                    self._lb_open = False                

