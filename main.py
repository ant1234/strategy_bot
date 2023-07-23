import tkinter as tk
import logging

# logging used for debugging. 
logger = logging.getLogger()

# set logging level to show info logging in the console.
logger.setLevel(logging.INFO)

# show time, level names and messages 
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

logger.debug('This message is useful when debugging the program.')
logger.info('This shows some basic information in the program.')
logger.warning('This shows something to pay close attention to.')
logger.error('This shows that something has gone wrong in the program.') 

# tkinter ui.
root = tk.Tk()

# prevent termination of program after running.
root.mainloop()