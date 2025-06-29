import src.api as api
import tkinter as tk
from tkinter import font


class TripDirections(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Driving directions"
        self.inputs = []
        self.read_only = None

    def display(self):
        self._display_window()
        self._address_input()
        self._summit_button()
        self._display_directions()

    def _display_window(self):
        title_frame = tk.Frame(master=self, borderwidth=2, relief=tk.GROOVE)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(
            master=title_frame,
            text="Trip Directions",
            font=font.Font(size=28, weight="bold")
        )
        title_label.pack()

    def _address_input(self):
        input_frame = tk.Frame(master=self, borderwidth=2, relief=tk.GROOVE)
        input_frame.pack(fill=tk.X)
        input_frame.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1, minsize=50)
        self.columnconfigure(0, weight=1, minsize=75)

        labels = ['From: ', 'To: ']
        for row, val in enumerate(labels):
            label = tk.Label(master=input_frame, text=val)
            label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.E)
            entry = tk.Entry(master=input_frame)
            self.inputs.append(entry)
            entry.grid(row=row, column=1, padx=5, pady=5, sticky=tk.EW)

    def _summit_button(self):
        summit_frame = tk.Frame(master=self, borderwidth=2)
        summit_frame.pack()
        button = tk.Button(
            master=summit_frame,
            text="Summit",
            fg="black",
            highlightbackground="lightblue",
            command=self._on_click
        )

        button.grid(row=0, padx=5, pady=5, sticky=tk.NSEW)

    def _display_directions(self):
        directions_frame = tk.Frame(master=self, borderwidth=2, relief=tk.GROOVE)
        directions_frame.pack(fill=tk.BOTH, expand=True)
        directions_frame.columnconfigure(0, weight=1)
        directions_frame.rowconfigure(1, weight=1)

        label = tk.Label(master=directions_frame, text='Directions')
        label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        text = tk.Text(master=directions_frame, wrap=tk.WORD, height=10)
        text.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)
        text.config(state=tk.DISABLED)

        self.read_only = text

    def _on_click(self):
        src = api.get_address_coordinates(self.inputs[0].get())
        dst = api.get_address_coordinates(self.inputs[1].get())
        instructions = api.get_directions(src, dst)

        self.read_only.config(state=tk.NORMAL)
        self.read_only.delete('1.0', tk.END)

        for instruction in instructions:
            self.read_only.insert(tk.END, instruction + "\n")

        self.read_only.config(state=tk.DISABLED)
