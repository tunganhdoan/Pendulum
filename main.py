import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()
    root.state('zoomed')
    root.title("Pendulum Simulation (ver:1.0)")
    root.geometry('1360x768+300+20')
    root.iconbitmap('./assets/pd.ico')

    tk.Label(root, text='Classic Label').pack()
    ttk.Label(root, text='Themed Label').pack()
    root.mainloop()
