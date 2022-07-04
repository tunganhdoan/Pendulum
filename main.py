import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.title("Pendulum Simulation (ver:1.0)")
        self.geometry('1360x768+300+20')
        self.iconbitmap('./assets/pd.ico')

        self.text = tk.StringVar()

        label = tk.Label(self, textvariable=self.text, font=('Helvetica 13 bold')).pack()
        self.btn1 = ttk.Button(self, text="Button1", command=lambda: self.print_text("Button 1"))
        self.btn1.pack(pady=10)
        self.btn2 = ttk.Button(self, text="Button2", command=lambda: self.print_text("Button 2"))
        self.btn2.pack(pady=10)
        self.btn3 = ttk.Button(self, text="Button3", command=lambda: self.print_text("Button 3"))
        self.btn3.pack(pady=10)

    # Display a Label
    def print_text(self, t):
        self.text.set(t)


if __name__ == '__main__':
    app = App()
    app.mainloop()
