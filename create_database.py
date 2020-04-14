import pandas as pd
from script import hdf5_getters


def get_song_fiels(path):
    '''
    Get song's attributes
    :param path: path of HDF5 file
    :return: attributes as Pandas Series
    '''

    # Get hdf5 file
    file = pd.HDFStore(path)

    # Fetch attributes (iloc[0] --> from DataFrame to Series)
    meta_song = file.get("metadata/songs").iloc[0]
    analysis_song = file.get("analysis/songs").iloc[0]
    year = file.get("musicbrainz/songs").iloc[0]
    # TODO --> There're many useless attributes now (Idx_sections_confidence, ...)

    # TODO --> The others are array (not table). How to handle those?
    # similar_art = file.get("analysis/bars_start")

    # Close reading process
    file.close()

    # Merge the series
    song = pd.concat([meta_song, year, analysis_song])

    return song


# ---------------------------------------------------
root = "/Users/marco/Documents/MillionSongSubset/data"
file = "/A/A/A/TRAAAAW128F429D538.h5"
path = root + file

song = get_song_fiels(path)
print("*********************** ATTRIBUTES --> (", len(song), ") *******************")
print(song)
