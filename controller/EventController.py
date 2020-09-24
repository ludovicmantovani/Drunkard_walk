class EventController:
    def __init__(self, app):
        self.app = app
        self.board = None
        self.board_frame = None
        self.cover_option = None

    def destroy_app(self):
        # ret = mb.askyesno(title="Quitter", message="Voulez-vous vraiment quitter ?")
        # if ret == True:
        self.app.destroy()

    def change_board_size(self, new_size):
        if self.board is not None and self.board_frame is not None:
            self.board.set_size(new_size)
            self.board_frame.draw()

    def set_board(self, board):
        self.board = board

    def set_board_frame(self, board_frame):
        self.board_frame = board_frame

    def set_cover(self, coverage_value):
        self.cover_option = coverage_value

    def generate(self):
        self.board.generate(int(self.cover_option.get()))
        self.board_frame.draw()
