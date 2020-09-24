import tkinter as tk
from tkinter import ttk


class InterfaceFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        ttk.Label(self, text="Dungeon generator", font=("Segoe UI", 20)).pack()

        size_option_frame = SizeOptionFrame(self, self.controller, *args, **kwargs)
        size_option_frame.pack(side="top", fill="both", expand=True)

        coverage_frame = CoverageOptionFrame(self, self.controller, *args, **kwargs)
        coverage_frame.pack(side="top", fill="both", expand=True)

        dead_frame = AgentDeadOptionFrame(self, self.controller, *args, **kwargs)
        dead_frame.pack(side="top", fill="both", expand=True)

        clone_frame = AgentCloneOptionFrame(self, self.controller, *args, **kwargs)
        clone_frame.pack(side="top", fill="both", expand=True)

        direction_frame = AgentDirectionOptionFrame(self, self.controller, *args, **kwargs)
        direction_frame.pack(side="top", fill="both", expand=True)

        operation_frame = OperationFrame(self, self.controller, *args, **kwargs)
        operation_frame.pack(side="top", fill="both", expand=True)


class SizeOptionFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        size_label = tk.Label(self, text="Map size: ")
        size_label.pack(side="left", expand=True)
        size_step = 5
        size_max = 50
        size_values = [f'{nbr} x {nbr}' for nbr in range(10, size_max + size_step, size_step)]
        self.size_value = tk.StringVar(value=size_values[0])
        self.size_combobox = ttk.Combobox(self, textvariable=self.size_value, state="readonly", values=size_values)
        self.size_combobox.pack(side="left", fill="x", expand=True)
        self.size_combobox.bind("<<ComboboxSelected>>", self.handle_size_selection)

    def handle_size_selection(self, event):
        new_size = int(self.size_combobox.get().split('x')[0].strip())
        self.controller.change_board_size(new_size)


class CoverageOptionFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        coverage_label = tk.Label(self, text="Coverage limitation (%): ")
        coverage_label.pack(side="left", expand=True)
        self.coverage_value = tk.IntVar(value=50)
        self.controller.set_cover(self.coverage_value)
        coverage_spinbox = ttk.Spinbox(self, from_=0, to=100, textvariable=self.coverage_value)
        coverage_spinbox.pack(side="left", fill="x", expand=True)


class AgentDeadOptionFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        dead_label = tk.Label(self, text="Agent's dead probability (%): ", state="disabled")
        dead_label.pack(side="left", expand=True)
        self.dead_value = tk.IntVar(value=10)
        dead_spinbox = ttk.Spinbox(self, from_=0, to=100, textvariable=self.dead_value, state="disabled")
        dead_spinbox.pack(side="left", fill="x", expand=True)


class AgentCloneOptionFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        clone_label = tk.Label(self, text="Agent's clone probability (%): ", state="disabled")
        clone_label.pack(side="left", expand=True)
        self.clone_value = tk.IntVar(value=10)
        clone_spinbox = ttk.Spinbox(self, from_=0, to=100, textvariable=self.clone_value, state="disabled")
        clone_spinbox.pack(side="left", fill="x", expand=True)


class AgentDirectionOptionFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        direction_label = tk.Label(self, text="Agent's direction switch probability (%): ", state="disabled")
        direction_label.pack(side="left", expand=True)
        self.direction_value = tk.IntVar(value=25)
        direction_spinbox = ttk.Spinbox(self, from_=0, to=100, textvariable=self.direction_value, state="disabled")
        direction_spinbox.pack(side="left", fill="x", expand=True)


class OperationFrame(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.controller = controller

        random_button = ttk.Button(self, text="Random probability", underline=0, state="disabled")
        random_button.pack(side="left", fill="x", expand=True)

        generate_button = ttk.Button(self, text="Generate", underline=0,
                                     command=self.controller.generate)
        generate_button.pack(side="right", fill="x", expand=True)
