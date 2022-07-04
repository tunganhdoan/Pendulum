import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()
    root.state('zoomed')
    root.title("Pendulum Simulation (ver:1.0)")
    root.geometry('1360x768+300+20')
    root.iconbitmap('./assets/pd.ico')

    text = tk.StringVar()


    # Display a Label
    def print_text(t):
        text.set(t)


    label = tk.Label(root, textvariable=text, font=('Helvetica 13 bold')).pack()
    btn1 = ttk.Button(root, text="Button1", command=lambda: print_text("Button 1"))
    btn1.pack(pady=10)
    btn2 = ttk.Button(root, text="Button2", command=lambda: print_text("Button 2"))
    btn2.pack(pady=10)
    btn3 = ttk.Button(root, text="Button3", command=lambda: print_text("Button 3"))
    btn3.pack(pady=10)
    root.mainloop()
