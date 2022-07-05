import tkinter as tk
from tkinter import ttk

import numpy as np
from PIL import Image, ImageTk
import scipy.integrate as integrate
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}

        def length_slider_changed(event):
            length.set(round(length.get(),1))
            renew_calculation()

        def length_spinbox_changed():
            length.set(round(length.get(), 1))
            renew_calculation()

        def gravity_slider_changed(event):
            gravity.set(round(gravity.get(), 1))
            renew_calculation()

        def mass_slider_changed(event):
            mass.set(round(mass.get(), 1))
            renew_calculation()

        def initial_angle_slider_changed(event):
            initial_angle.set(round(initial_angle.get()))
            renew_calculation()

        def initial_velocity_slider_changed(event):
            initial_velocity.set(round(initial_velocity.get()))
            renew_calculation()

        def time_step_slider_changed(event):
            time_step.set(round(time_step.get(), 3))
            renew_calculation()

        def renew_calculation():
            l = length.get()
            m = mass.get()
            g = gravity.get()
            theta_0 = initial_angle.get()
            omega_0 = initial_velocity.get()
            dt = time_step.get()
            t = np.arange(0,20,dt)
            sim_points = len(t)
            index = np.arange(0,sim_points,1)
            period = 2 * np.pi * np.sqrt(l / g)
            theta = theta_0*np.cos(np.sqrt(g / l)*t)


            figure = Figure(figsize=(6, 4), dpi=100)
            axes = figure.add_subplot()
            axes.plot(t, theta, 'g', label='plot')
            axes.set_title('Harmonic motion')
            axes.set_xlabel('Time')
            # create FigureCanvasTkAgg object
            figure_canvas = FigureCanvasTkAgg(figure, master=self)
            figure_canvas.draw()
            # create axes
            figure_canvas.get_tk_widget().grid(column=5,row=8)

        length = tk.DoubleVar()
        length.set(1.0)
        length_label = ttk.Label(self, text="Length").grid(column=0, row=0, sticky=tk.E)
        length_scale = ttk.Scale(self, variable=length, orient='horizontal', length=200, from_=1, to=50,
                                 command=length_slider_changed).grid(column=1, row=0)
        length_spinbox = ttk.Spinbox(self, textvariable=length, wrap=True, width=10, from_=1, to=50, command=length_spinbox_changed).grid(column=2,
                                                                                                          row=0)

        mass = tk.DoubleVar()
        mass.set(2.0)
        mass_label = ttk.Label(self, text="Mass").grid(column=0, row=1, sticky=tk.E)
        mass_scale = ttk.Scale(self, variable=mass, orient='horizontal', length=200, from_=1, to=20,
                                  command=mass_slider_changed).grid(column=1, row=1)
        mass_spinbox = ttk.Spinbox(self, textvariable=mass, wrap=True, width=10, from_=1, to=20,
                                      increment=0.1).grid(column=2,
                                                          row=1)

        gravity = tk.DoubleVar()
        gravity.set(9.8)
        gravity_label = ttk.Label(self, text="Gravity").grid(column=0, row=2, sticky=tk.E)
        gravity_scale = ttk.Scale(self, variable=gravity, orient='horizontal', length=200, from_=1, to=20,
                                  command=gravity_slider_changed).grid(column=1, row=2)
        gravity_spinbox = ttk.Spinbox(self, textvariable=gravity, wrap=True, width=10, from_=1, to=20,
                                      increment=0.1).grid(column=2,
                                                          row=2)
        initial_angle = tk.IntVar()
        initial_angle.set(20)
        initial_angle_label = ttk.Label(self, text="Initial Angle").grid(column=0, row=3, sticky=tk.E)
        initial_angle_scale = ttk.Scale(self, variable=initial_angle, orient='horizontal', length=200, from_=0, to=360,
                                        command=initial_angle_slider_changed).grid(column=1, row=3)
        initial_angle_spinbox = ttk.Spinbox(self, textvariable=initial_angle, wrap=True, width=10, from_=1,
                                            to=360, increment=1).grid(column=2, row=3)

        initial_velocity = tk.DoubleVar()
        initial_velocity.set(3.0)
        initial_angle_label = ttk.Label(self, text="Initial Angular Velocity").grid(column=0, row=4, sticky=tk.E)
        initial_angle_scale = ttk.Scale(self, variable=initial_velocity, orient='horizontal', length=200, from_=0, to=360,
                                        command=initial_velocity_slider_changed).grid(column=1, row=4)
        initial_angle_spinbox = ttk.Spinbox(self, textvariable=initial_velocity, wrap=True, width=10, from_=1,
                                            to=360, increment=1).grid(column=2, row=4)

        time_step = tk.DoubleVar(value=0.05)
        time_step_label = ttk.Label(self, text="Time Step").grid(column=0, row=5, sticky=tk.E)
        time_step_scale = ttk.Scale(self, variable=time_step, orient='horizontal', length=200, from_=0.001, to=0.1,
                                    command=time_step_slider_changed).grid(column=1, row=5)
        time_step_spinbox = ttk.Spinbox(self, textvariable=time_step, wrap=True, width=10, increment=0.001, from_=0.001, to=0.1).grid(
            column=2, row=5)

        # Create a photoimage object of the image in the path
        image1 = Image.open("images/ani_pen.gif")
        place_holder = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=place_holder)
        label1.image = place_holder

        # Position image
        #label1.place(x=600, y=50)

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


        self.grid(padx=50, pady=50, sticky=tk.NSEW)
