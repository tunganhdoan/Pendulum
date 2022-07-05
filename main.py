from tkinter import *
from tkVideoPlayer import TkinterVideo
FONT_LARGE = ("Times New Roman", 20)
FONT_SMALL = ("Times New Roman", 14)


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Single Pendulum Simulation - ver 1.0')
        self.geometry("1500x800")
        # set minimum window size value
        self.minsize(1500, 800)
        # set maximum window size value
        self.maxsize(1500, 800)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=30)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        # program title
        title_pane = Frame(self, highlightbackground="blue", highlightthickness=2)
        title_pane.grid(row=0,
                        column=0,
                        columnspan=2,
                        sticky="nsew",
                        padx=10,
                        pady=10)
        parameter_pane = Frame(self, highlightbackground="red", highlightthickness=2)
        parameter_pane.grid(row=1,
                            column=1,
                            sticky="nsew",
                            padx=10,
                            pady=10)
        display_pane = Frame(self, highlightbackground="green", highlightthickness=2)
        display_pane.grid(row=1,
                          column=0,
                          sticky="nsew",
                          padx=10,
                          pady=10)
        tkvideo = TkinterVideo(master=display_pane, keep_aspect=True, scaled=False)
        tkvideo.load(r"media/videos/MP4_1920.mp4")
        tkvideo.pack(expand=True, fill="both")
        tkvideo.set_size((1000, 600))  # sets the frame size

        tkvideo.play()  # play the video

if __name__ == "__main__":
    app = App()
    app.mainloop()
