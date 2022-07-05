import tkinter as tk
from tkinter import ttk

import numpy as np
from PIL import Image, ImageTk


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        length = tk.DoubleVar()
        length.set(1.0)

        def length_slider_changed(event):
            renew_calculation()

        def gravity_slider_changed(event):
            renew_calculation()

        def renew_calculation():
            tharm = 2 * np.pi * np.sqrt(length.get() / gravity.get())
            result.configure(text=str(tharm))

        length_label = ttk.Label(self, text="Length").grid(column=0, row=0, sticky=tk.E)
        length_scale = ttk.Scale(self, variable=length, orient='horizontal', length=200, from_=1, to=50,
                                 command=length_slider_changed).grid(column=1, row=0)
        length_spinbox = ttk.Spinbox(self, textvariable=length, wrap=True, width=10, from_=1, to=50).grid(column=2,
                                                                                                          row=0)

        mass = tk.DoubleVar()
        mass_label = ttk.Label(self, text="Mass").grid(column=0, row=1, sticky=tk.E)
        mass_scale = ttk.Scale(self, variable=mass, orient='horizontal', length=200).grid(column=1, row=1)
        mass_spinbox = ttk.Spinbox(self, textvariable=mass, wrap=True, width=10).grid(column=2, row=1)

        gravity = tk.DoubleVar()
        gravity.set(1.0)
        gravity_label = ttk.Label(self, text="Gravity").grid(column=0, row=2, sticky=tk.E)
        gravity_scale = ttk.Scale(self, variable=gravity, orient='horizontal', length=200, from_=1, to=50,
                                  command=gravity_slider_changed).grid(column=1, row=2)
        gravity_spinbox = ttk.Spinbox(self, textvariable=gravity, wrap=True, width=10, from_=1, to=50).grid(column=2,
                                                                                                            row=2)

        initial_angle_label = ttk.Label(self, text="Initial Angle").grid(column=0, row=3, sticky=tk.E)
        initial_angle_scale = ttk.Scale(self, variable=input, orient='horizontal', length=200).grid(column=1, row=3)
        initial_angle_spinbox = ttk.Spinbox(self, textvariable=input, wrap=True, width=10).grid(column=2, row=3)

        time_step_label = ttk.Label(self, text="Time Step").grid(column=0, row=4, sticky=tk.E)
        time_step_scale = ttk.Scale(self, variable=input, orient='horizontal', length=200).grid(column=1, row=4)
        time_step_spinbox = ttk.Spinbox(self, textvariable=input, wrap=True, width=10).grid(column=2, row=4)

        # Create a photoimage object of the image in the path
        image1 = Image.open("images/ani_pen.gif")
        place_holder = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=place_holder)
        label1.image = place_holder

        # Position image
        label1.place(x=600, y=50)

        # Create a Tkinter variable
        dropdown_value = tk.StringVar(self)

        # Dictionary with options
        choices = {'Small angles', 'Euler', 'Improved Euler', 'RK4'}
        dropdown_value.set('Small angles')  # set the default option

        popupMenu = ttk.OptionMenu(self, dropdown_value, *choices)
        ttk.Label(self, text="Choose a method").grid(row=6, column=0)
        popupMenu.grid(row=6, column=1)

        # on change dropdown value
        def change_dropdown(*args):
            print(dropdown_value.get())

        # link function to change dropdown
        dropdown_value.trace('w', change_dropdown)

        # Results

        result = ttk.Label(self, text="abc")
        result.grid(column=2, row=10)

        # Initial angular displacement (rad), tangential velocity (m.s-1)
        theta0, v0 = np.radians(60), 0
        # Estimate of the period using the harmonic (small displacement) approximation.
        # The real period will be longer than this.
        tharm = 2 * np.pi * np.sqrt(length.get() / gravity.get())
        print("{}".format(tharm))
        # add padding to the frame and show it
        self.grid(padx=50, pady=50, sticky=tk.NSEW)
