import tkinter as tk
from tkinter import ttk

from model.Tile import *


class BoardFrame(ttk.Frame):
    TILES_COLORATION = {
        Tile.WALL: "black",
        Tile.EMPTY: "white"
    }

    def __init__(self, container, board, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.board = board
        self.controller = controller
        self.controller.set_board_frame(self)

        self.canvas = tk.Canvas(self, bg="white", height=400, width=400)
        self.canvas.pack(fill="both", expand=True)
        self.draw()

    def draw(self):
        canvas_width = int(self.canvas['width'])
        tiles_in_line = len(self.board)
        if tiles_in_line > 0:
            tile_width = canvas_width / tiles_in_line
            for line_index in range(0, tiles_in_line):
                for column_index in range(0, tiles_in_line):
                    nw_x = tile_width * column_index
                    nw_y = tile_width * line_index
                    se_x = nw_x + tile_width
                    se_y = nw_y + tile_width
                    tile = self.board.get_board()[line_index][column_index]
                    color = BoardFrame.TILES_COLORATION.get(tile, "red")
                    self.canvas.create_rectangle(nw_x, nw_y, se_x, se_y, fill=color, width=1, outline='white')
