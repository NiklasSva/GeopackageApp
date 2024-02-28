# Copyright (c) 2024, Niklas Svantesson
import file_io.io_dependencies as io

# READ
def ReadGeopackage(filename):
    try:
        geo_data_frame = io.geopandas.read_file(filename)
        print (f"The GeoDataFrame is:\n{geo_data_frame}")
    except:
        print ("Failed to read GeoPackage file.")

# WRITE
def WriteGeopackage(geo_data_frame, filename):
    try:
        if not io.os.path.exists(filename):
            geo_data_frame.to_file("../output/" + filename, driver="GPKG")
            return 0
        else:
            return ("The GeoPackage file already exists, overwrite it?")
    except:
        return 1

def OverwriteGeopackage(geo_data_frame, filename):
    try:
        geo_data_frame.to_file("../output/" + filename, driver="GPKG")
    except:
        print ("Failed to overwrite GeoPackage file.")

def SaveGeopackage(geo_data_frame, filename):
    try:
        result = WriteGeopackage(geo_data_frame, filename)
        if result == 0:
            print (result)
            overwrite = input("Overwrite file? (y/n/rename): ")
            if overwrite == "y":
                WriteGeopackage(geo_data_frame, filename)
            elif overwrite == "rename":
                new_filename = input("Enter new filename: ")
                WriteGeopackage(geo_data_frame, new_filename)
            else:
                print ("File not overwritten.")
        elif result == 1:
            print ("Failed to write GeoPackage file.")
        else:
            return 0
    except:
        print ("Failed to save GeoPackage file.")
