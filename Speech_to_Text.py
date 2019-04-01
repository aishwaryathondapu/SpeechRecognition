import sys
import speech_recognition as sr
from tkinter import *
from googletrans import Translator as gt
# Print the version of the python and version of the speech recognition
# Instead of reinstalling the speechrecognition for python version 3.6 using the python version 3.7 interpreter where the
# speech recognition package is already installed and changed the interpreter to python version 3.7. To change the interpreter
# go to PyCharm-->Pre
# Printing the Python Version
print("Python Version:"+sys.version)
print(sr.__version__)
# Creating the object for speech recognition as r
r=sr.Recognizer()
# Print the object r
print("The object of speech recognition:"+str(r))
# As we want to listen to the voice from the microphone use the Microphone() from speech_recognition
micro_phone=sr.Microphone()
# To list all the available microphones use the list_microphone_names
list_of_microphone_devices=micro_phone.list_microphone_names()
print("List of available devices:")
for i in range(0,len(list_of_microphone_devices)):
    print(list_of_microphone_devices[i]+ " ")
print("Total number of devices:"+str(len(list_of_microphone_devices)))
# If we want to use the particulat Microphone pass the index of the device to device_index parameter. As we want to use the built-in
# microphone
microphone_using=sr.Microphone(device_index=0)
# creating the object tkinter
root = Tk()
frame=Frame(root)
def gui_sr():
    root.geometry("500x500")
    root.resizable(width=0,height=0)
    # Set title of the window using the title()
    root.title("Speech Recognition")
    # Test label to display on the window
    #test_label=Label(root, text="Hello from SR")
    #test_label.pack()
    # Create the frame to hold the widgets
gui_sr()
# Create a single line entry that has disabled text "Listening...."
label1=Label(root,text="You said:")
text = Entry(root,bd=2.75)
label1.pack()
frame.pack()
root.mainloop()