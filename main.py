import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.title("Pendulum Simulation (ver:1.0)")
        self.geometry('1360x768+300+20')
        self.iconbitmap('./assets/pd.ico')


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**options)
        # show the frame on the container
        self.pack(**options)

if __name__ == '__main__':
    app = App()
    main_frame = MainFrame(app)
    app.mainloop()
