import tkinter as tk
import logging
from binance_futures import write_log

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
    # tkinter ui.
    root = tk.Tk()

    # prevent termination of program after running.
    root.mainloop()