# custom_console.py
# Copyright (c) 2024, Niklas Svantesson

import tkinter

def Add_console(root:tkinter.Tk):
    console_frame = tkinter.Frame(root)
    console_frame.pack(pady=10)
    console_output = tkinter.Text(root, height=10, width=50)
    console_output.pack()
    return console_output
