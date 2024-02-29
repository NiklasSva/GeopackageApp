# file_IO.py
# Copyright (c) 2024, Niklas Svantesson

import os
import geopandas

import sys
sys.path.append('/mnt/6fa208e0-09d5-428e-82b6-f58f1a68c957/Code4Fun/GeopackageApp')

from supported_drivers import supported_drivers
from supported_file_types import supported_file_types as file_types


# READ --------------------------------------------------------------------------------------------
def ReadFile(file_name):
    """
    Reads a file based on its file extension.

    Parameters:
        file_name (str): The path and name of the file.

    Returns:
        geopandas.GeoDataFrame or None: The read file or None if the file
            could not be read.
    """

    if not os.path.exists(file_name):
        print(f"The file '{file_name}' does not exist.")
        return None

    file_extension = os.path.splitext(file_name)[1].lower()

    try:
        return geopandas.read_file(file_name, driver=file_types[file_extension])

    except KeyError:
        print(f"The file extension '{file_extension}' is not supported.")

    return None

# WRITE -------------------------------------------------------------------------------------------

def WriteToFile(file_name, file_type, data):
    """
    Writes a file based on its file extension.

    Parameters:
        file_name (str): The path and name of the file.
        file_type (str): The file type.
        data (geopandas.GeoDataFrame): The data to write.

    Returns:
        None
    """
    if not isinstance(data, geopandas.GeoDataFrame):
        print("The data must be a GeoDataFrame.")
        return

    if not os.path.exists("./output"):
        os.makedirs("./output")

    driver = supported_drivers[file_type]
    if driver is not None:
        data.to_file(f"./output/{file_name}.{file_type}", driver=driver)
    elif file_type == "shp":
        data.to_file(f"./output/{file_name}.shp")
    else:
        print(f"The file type '{file_type}' is not supported.")
