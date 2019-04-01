import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

def on_combo_configure(event):
    global fruit
    font = event.widget.cget('values')
    print(font)

root = tk.Tk()
root.title("testing the combobox")
root.geometry('300x300+50+50')
fruit = ['apples are the best', 'bananas are better']

c = ttk.Combobox(root, values=fruit, width=10)
tk.call('ttk::combobox::PopdownWindow')
c.pack()

root.mainloop()