from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)
        # show the frame on the container
        self.pack(**options)
