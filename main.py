import tkinter as tk

from model.Board import *
from view.InterfaceFrame import *
from view.BoardFrame import *
from view.OutputFrame import *
from controller.EventController import *


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Dungeon Generator")
        self.resizable(False, False)
        self.controller = EventController(self)

        board = Board()

        self.controller.set_board(board)

        main_frame = ttk.Frame(self, padding=(20, 10, 10, 10))
        main_frame.pack(fill="both", expand=True)
        interface_frame = InterfaceFrame(main_frame, self.controller, padding=(20, 10, 10, 10))
        interface_frame.pack(side="left", fill="x")
        board_frame = BoardFrame(main_frame, board, self.controller, padding=(10, 10, 10, 10))
        board_frame.pack(side="left", fill="both")

        output_frame = OutputFrame(self, self.controller, padding=(20, 10, 20, 10))
        output_frame.pack(side="bottom", fill="both", expand=True)

root = App()
root.mainloop()
