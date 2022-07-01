from tkinter import *

FONT_LARGE = ("Times New Roman",20)
class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Single Pendulum Simulation - ver 1.0')
        self.state('zoomed')
        self.minsize(1024, 768)
        # program title
        program_title = Label(self, text="PHYSICS OF PENDULUM", font=FONT_LARGE)
        # using grid method to position of label
        program_title.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
