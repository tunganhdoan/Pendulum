import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()
    root.state('zoomed')
    root.title("Pendulum Simulation (ver:1.0)")
    root.geometry('1360x768+300+20')
    root.iconbitmap('./assets/pd.ico')

    ttk.Label(root, text='Hi, there').pack()

    label = ttk.Label(root)
    label['text'] = 'Hi, there' #use dictionary index
    label.pack()

    label_1 = ttk.Label(root)
    label_1.config(text='Hi, there')
    label_1.pack()
    root.mainloop()
