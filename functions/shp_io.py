# Copyright (c) 2024, Niklas Svantesson
import file_io.io_dependencies as io

# READ
def ReadShapefile(filename):
    try:
        shapefile = io.geopandas.read_file(filename)
        print (f"The Shapefile is:\n{shapefile}")
    except:
        print ("Failed to read shapefile.")

# WRITE
def WriteShapefile(geo_data_frame, filename):
    try:
        if not io.os.path.exists(filename):
            geo_data_frame.to_file("../output/" + filename)
            return 0
        else:
            return ("The Shapefile already exists, overwrite it?")
    except:    
        return 1
    
def OverwriteShapefile(geo_data_frame, filename):
    try:
        geo_data_frame.to_file("../output/" + filename)
    except:
        print ("Failed to overwrite shapefile.")

def SaveShapefile(geo_data_frame, filename):
    try:
        result = WriteShapefile(geo_data_frame, filename)
        if result == 0:
            print (result)
            overwrite = input("Overwrite file? (y/n/rename): ")
            if overwrite == "y":
                WriteShapefile(geo_data_frame, filename)
            elif overwrite == "rename":
                new_filename = input("Enter new filename: ")
                WriteShapefile(geo_data_frame, new_filename)
            else:
                print ("File not overwritten.")
        elif result == 1:
            print ("Failed to write shapefile.")
        else:
            return 0
    except:
        print ("Failed to save shapefile.")