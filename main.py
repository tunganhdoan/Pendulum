from tkinter import Tk

if __name__ == '__main__':
    root = Tk()
    root.title("Pendulum Simulation (ver:1.0)")
    root_width = 600
    root_height = 400
    # get the screen width and height using wininfo_width() and wininfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - root_width / 2)
    center_y = int(screen_height / 2 - root_height / 2)
    # set the position of the window to the center of the screen
    root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
    root.mainloop()
