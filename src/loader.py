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

        self.train0['rating'] = self.train0['rating'].apply(pd.to_numeric)

    def get_genre(self):
        return self.genre

    def get_songs(self):
        return self.songs

    def format_genre(self, genre):
        genre['fullgenreid'] = genre['genreid'].astype(str) + genre['parentid'].astype(str)+ genre['level'].astype(str)
        return genre

    def get_dataframe(self):
        df = pd.merge(self.train0, self.songs, left_on='songid', right_on='songid')
        df = pd.merge(df, self.genre, left_on='genreid', right_on='genreid')
        return df