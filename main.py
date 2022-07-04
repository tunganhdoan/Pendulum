from tkinter import Tk

if __name__ == '__main__':
    root = Tk()
    root.state('zoomed')
    root.title("Pendulum Simulation (ver:1.0)")
    root.geometry('1360x768+300+20')
    root.iconbitmap('./assets/pd.ico')
    root.mainloop()
