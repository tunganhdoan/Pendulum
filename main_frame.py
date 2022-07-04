from tkinter import ttk
import tkinter as tk

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        # config the grid
        # configure the grid
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # label
        # username
        length_label = ttk.Label(self, text="Length:")
        length_label.grid(column=1, row=0, sticky=tk.W, **options)

        # show the frame on the container
        self.pack(**options)
