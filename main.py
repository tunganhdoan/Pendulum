from tkinter import Tk
import test_main_only
# if __name__ == '__main__':
# It's boilerplate code that protects users from accidentally invoking the script when they didn't intend to.
# So when the interpreter runs a module,
# the __name__ variable will be set as  __main__ if the module that is being run is the main program.
# But if the code is importing the module from another module,
# then the __name__  variable will be set to that module’s name.

print("File one __name__ is set to: {}" .format(__name__))
if __name__ == '__main__':
    root = Tk()
    root.mainloop()
