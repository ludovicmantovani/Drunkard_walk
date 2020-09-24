from tkinter import ttk


class OutputFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller
        root = self

        image_save_button = ttk.Button(self, text="Save as image", command=root.destroy, underline=8,
                                       state="disabled")
        image_save_button.pack(side="left", fill="x", expand=True)

        text_save_button = ttk.Button(self, text="Save as text", command=root.destroy, underline=8,
                                      state="disabled")
        text_save_button.pack(side="left", fill="x", expand=True)

        quit_button = ttk.Button(self, text="Quit", command=lambda: self.controller.destroy_app(), underline=0)
        quit_button.pack(side="right", fill="x", expand=True)
