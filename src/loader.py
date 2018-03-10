import pandas as pd

class DataFactory:
    def __init__(self):
        self.genre = pd.read_csv('./data/genre-hierarchy.txt', delimiter='\t', header=None)
        self.songs = pd.read_csv('./data/song-attributes.txt', delimiter='\t', header=None)
        self.train0 = pd.read_csv('./data/train_0.txt', delimiter='\t', header=None, nrows=100)

        self.train0.columns = ['userid', 'songid', 'rating']
        self.songs.columns = ['songid', 'albumid', 'artistid', 'genreid']
        self.genre.columns = ['genreid', 'parentid', 'level', 'name']
        self.genre = self.format_genre(self.genre)

    def getGenre(self):
        return self.genre

    def getSongs(self):
        return self.songs

    def format_genre(self, genre):
        genre['fullgenreid'] = genre['genreid'].astype(str) + genre['parentid'].astype(str)+ genre['level'].astype(str)
        return genre

    def join(self):
        df = pd.merge(self.train0, self.songs, left_on='songid', right_on='songid')

    # TODO Join Genre columns into 1 integer
    # TODO Append Genre columns into df