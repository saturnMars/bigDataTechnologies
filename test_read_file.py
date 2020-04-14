import pandas as pd
from script import hdf5_getters

# Try Hdf5_getters file
def getSongName(path):
    h5 = hdf5_getters.open_h5_file_read(path)
    songName = hdf5_getters.get_title(h5)
    h5.close()
    return songName

# Read the HDF5 File
root = "/Users/marco/Documents/MillionSongSubset/data"
file = "/A/A/A/TRAAAAW128F429D538.h5"
path = root + file

# CALL get name
songName = getSongName(path)
print("SONG: -->", songName)

# From raw data to dataframe
output_table = pd.read_hdf(path, 'metadata/songs')
print(output_table)

print("SONG(2) --> ", output_table["title"].iloc[0])
