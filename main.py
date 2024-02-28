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

import geopandas
import matplotlib.pyplot as pyplot
import tkinter
# -----------------------------------
from tkinter import filedialog 
# This allows you to use the filedialog module directly without having to
# prefix it with "tkinter." when calling its functions.
# -----------------------------------
import functions.file_IO as io

def open_file_dialog():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

file = open_file_dialog()
print (io.ReadFile(file))

# make dummy geopackage for testing
# geo_data_frame = geopandas.GeoDataFrame(geometry=geopandas.points_from_xy([0, 1, 2], [0, 1, 2]))
# geo_data_frame.to_file("dummy_geopackage.gpkg")


'''

#geo_data_frame.plot()
#pyplot.show()

'''