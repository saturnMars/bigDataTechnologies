import pandas as pd
from script import hdf5_getters
from script import utils


def get_song_fields(file_path):
    '''
    Get song's attributes
    :param file_path: path of HDF5 file
    :return: attributes as Pandas Series
    '''

    # Container --> Pandas.Series
    song = pd.Series(dtype="object")

    # Open HDF5 File by Hdf5_getters script
    file = hdf5_getters.open_h5_file_read(file_path)

    # Fetch attributes
    song["artist_familiarity"] = hdf5_getters.get_artist_familiarity(file)
    song["artist_hotttnesss"] = hdf5_getters.get_artist_hotttnesss(file)
    song["artist_id"] = hdf5_getters.get_artist_id(file)
    song["artist_mbid"] = hdf5_getters.get_artist_mbid(file)
    song["artist_playmeid"] = hdf5_getters.get_artist_playmeid(file)
    song["artist_7digitalid"] = hdf5_getters.get_artist_7digitalid(file)
    song["artist_latitude"] = hdf5_getters.get_artist_latitude(file)
    song["artist_longitude"] = hdf5_getters.get_artist_longitude(file)
    song["artist_location"] = hdf5_getters.get_artist_location(file)
    song["artist_name"] = hdf5_getters.get_artist_name(file)
    song["release"] = hdf5_getters.get_release(file)
    song["release_7digitalid"] = hdf5_getters.get_release_7digitalid(file)
    song["song_id"] = hdf5_getters.get_song_id(file)
    song["song_hotttnesss"] = hdf5_getters.get_song_hotttnesss(file)
    song["title"] = hdf5_getters.get_title(file)
    song["track_7digitalid"] = hdf5_getters.get_track_7digitalid(file)
    song["similar_artists"] = hdf5_getters.get_similar_artists(file)
    song["artist_terms"] = hdf5_getters.get_artist_terms(file)
    song["artist_terms_freq"] = hdf5_getters.get_artist_terms_freq(file)
    song["artist_terms_weight"] = hdf5_getters.get_artist_terms_weight(file)
    song["analysis_sample_rate"] = hdf5_getters.get_analysis_sample_rate(file)
    song["audio_md5"] = hdf5_getters.get_audio_md5(file)
    song["danceability"] = hdf5_getters.get_danceability(file)
    song["duration"] = hdf5_getters.get_duration(file)
    song["end_of_fade_in"] = hdf5_getters.get_end_of_fade_in(file)
    song["energy"] = hdf5_getters.get_energy(file)
    song["key"] = hdf5_getters.get_key(file)
    song["key_confidence"] = hdf5_getters.get_key_confidence(file)
    song["loudness"] = hdf5_getters.get_loudness(file)
    song["mode"] = hdf5_getters.get_mode(file)
    song["mode_confidence"] = hdf5_getters.get_mode_confidence(file)
    song["start_of_fade_out"] = hdf5_getters.get_start_of_fade_out(file)
    song["tempo"] = hdf5_getters.get_tempo(file)
    song["time_signature"] = hdf5_getters.get_time_signature(file)
    song["time_signature_confidence"] = hdf5_getters.get_time_signature_confidence(file)
    song["track_id"] = hdf5_getters.get_track_id(file)
    song["segments_start"] = hdf5_getters.get_segments_start(file)
    song["segments_confidence"] = hdf5_getters.get_segments_confidence(file)
    song["segments_pitches"] = hdf5_getters.get_segments_pitches(file)
    song["segments_timbre"] = hdf5_getters.get_segments_timbre(file)
    song["segments_loudness_max"] = hdf5_getters.get_segments_loudness_max(file)
    song["segments_loudness_max_time"] = hdf5_getters.get_segments_loudness_max_time(file)
    song["segments_loudness_start"] = hdf5_getters.get_segments_loudness_start(file)
    song["sections_start"] = hdf5_getters.get_sections_start(file)
    song["sections_confidence"] = hdf5_getters.get_sections_confidence(file)
    song["beats_start"] = hdf5_getters.get_beats_start(file)
    song["beats_confidence"] = hdf5_getters.get_beats_confidence(file)
    song["bars_start"] = hdf5_getters.get_bars_start(file)
    song["bars_confidence"] = hdf5_getters.get_bars_confidence(file)
    song["tatums_start"] = hdf5_getters.get_tatums_start(file)
    song["tatums_confidence"] = hdf5_getters.get_tatums_confidence(file)
    song["artist_mbtags"] = hdf5_getters.get_artist_mbtags(file)
    song["artist_mbtags_count"] = hdf5_getters.get_artist_mbtags_count(file)
    song["year"] = hdf5_getters.get_year(file)

    # Close file
    file.close()

    return song


def fetch_all_songs(root_folder, num_song=100):
    '''
     Visit every sub-folder and fetch songs data
    :param root_folder: HDF5 database's main folder
    :param num_song: how many songs you want to get
    :return: Pandas.DataFrame
    '''
    # Container
    database = pd.DataFrame()

    # Get all song patches
    songPath = utils.get_all_files(root_folder)[:num_song]

    # Retrieve all songs
    for i, file in enumerate(songPath):
        song = get_song_fields(file)
        database = database.append(song, ignore_index=True)
        print("(", i, ") LOADED -->", file)
    return database


# ---------------------------------------------------
ROOT_FOLDER = "/Users/marco/Documents/MillionSongSubset/data"

# CREATE DATABASE - Pandas DataFrame
print("Start loading...")
song_database = fetch_all_songs(ROOT_FOLDER)
print("\n", song_database, "\nA) Load completed")