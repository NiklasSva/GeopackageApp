# file_IO.py
# Copyright (c) 2024, Niklas Svantesson

import os
import geopandas
import csv

file_types = []
with open('config/file_types.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        file_types.append((row[0], row[1]))
        print(file_types)

# READ --------------------------------------------------------------------------------------------
def ReadFile(filename):
    """
    Reads a file based on its file extension.

    Parameters:
        filename (str): The path and name of the file.

    Returns:
        geopandas.GeoDataFrame or None: The read file or None if the file
            could not be read.
    """

    if not os.path.exists(filename):
        print(f"The file '{filename}' does not exist.")
        return None

    file_extension = os.path.splitext(filename)[1].lower()
    for file_type in file_types:
        if file_type[0] == "dataImport" and file_extension == file_type[1]:
            try:
                return geopandas.read_file(filename)
            except Exception:
                print(f"Failed to read file '{filename}'.")
                return None

    print(f"The file extension '{file_extension}' is not supported.")
    return None



# WRITE
# TODO: Write GeoPackage or Shapefile