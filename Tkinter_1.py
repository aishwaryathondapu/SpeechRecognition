# To import everything from the Tkinter use the below code
from tkinter import *

# The below is the constructor to create the blank window
root=Tk()

root.title("Speech Recognition")
theLabel=Label(root, text="Aishwarya Thondapu")

# Position to keep the window. Layouts

theLabel.pack()

theButton=Button(text="QUIT")
theButton.pack()

# The below command continously display the window
root.mainloop()
