# Copyright (c) 2024, Niklas Svantesson
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above    
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import matplotlib.pyplot as pyplot
import tkinter, geopandas, os, sys
# -----------------------------------
from tkinter import filedialog 
# ^ This allows me to use the filedialog module directly without having
# to prefix it with "tkinter."
# -----------------------------------
import functions.file_IO as io
import functions.custom_console as console

def open_file_dialog(nr:int = 0, filetypes:list[tuple]=[("gpkg files", "*.gpkg")]) -> str: # add other file types here
    root = tkinter.Tk()
    window_title = ""

    if nr == 0:
        window_title = "Select a file"
    elif nr == 1:
        window_title = "Select the first file"
    elif nr == 2:
        window_title = "Select the second file"
    
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("gpkg files", "*.gpkg")], title=window_title)
    print("Selected file:", file_path)
    return file_path

def Display_file_data(file_path:str):
    if file_path is None:
        print("No file selected.")
        return
    
    data = io.ReadFile(file_path)
    if data is None:
        print("Could not read the file.")
        return

    print(data)

def Check_common_columns(data_1:geopandas.GeoDataFrame, data_2:geopandas.GeoDataFrame) -> set:
    print("Columns in data_1:", data_1.columns)
    print("Columns in data_2:", data_2.columns)

    common_columns = set(data_1.columns) & set(data_2.columns)
    print("Common columns:", common_columns)
    return common_columns

def Join_geodata_files():
    file_path_1 = open_file_dialog(1)
    data_1 = io.ReadFile(file_path_1)
    if data_1 is None:
        print("Could not read the first file.")
        return
    
    file_path_2 = open_file_dialog(2)
    data_2 = io.ReadFile(file_path_2)
    if data_2 is None:
        print("Could not read the second file.")
        return   

    common_columns = Check_common_columns(data_1, data_2)
    if len(common_columns) < 1:
        print("The files can not be joined because they have no common columns.")
        return
    
    file_name_1 = os.path.splitext(os.path.basename(file_path_1))[0]
    file_name_2 = os.path.splitext(os.path.basename(file_path_2))[0]

    try:
        merged_data = data_1.merge(data_2, on = list(common_columns), how = 'outer')
        io.WriteToFile(f"joined_{file_name_1}_{file_name_2} ", "gpkg", merged_data)
    except Exception as e:
        print(e)

def Plot_file_data(file_path:str):
    data = io.ReadFile(file_path)
    if data is None:
        print("Could not read the file.")
        return
    
    print(str(data))
    data.plot()
    pyplot.show()

class ConsoleRedirector:
    def __init__(self, console_widget):
        self.console_widget = console_widget

    def write(self, text):
        self.console_widget.insert(tkinter.END, text)
        self.console_widget.see(tkinter.END)  # Auto-scroll to the end of the text
    
def Start_application():
    root = tkinter.Tk()
    root.title("Geopackage App")
    root.geometry("640x480")  

    open_button = tkinter.Button(root, text="Open a geodata file", command=lambda: Display_file_data(open_file_dialog()))
    open_button.pack()
    join_button = tkinter.Button(root, text="Join two geodata files", command=lambda: Join_geodata_files())
    join_button.pack()
    display_button = tkinter.Button(root, text="Display a geodata file", command=lambda: Plot_file_data(open_file_dialog()))
    display_button.pack()
    quit_button = tkinter.Button(root, text="Quit", command=root.destroy)
    quit_button.pack()

    console_output = console.Add_console(root)
    # make print() write to the new console widget
    sys.stdout = ConsoleRedirector(console_output)

    root.mainloop()    

    sys.stdout = sys.__stdout__

# start the application
Start_application()  