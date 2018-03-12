import pandas as pd

class DataFactory:
    def __init__(self, records=None):
        self.genre = pd.read_csv('./data/genre-hierarchy.txt', delimiter='\t', header=None)
        self.songs = pd.read_csv('./data/song-attributes.txt', delimiter='\t', header=None)

        if records:
            self.train = pd.read_csv('./data/train_0.txt', delimiter='\t', header=None, nrows=records)
            self.test = pd.read_csv('./data/test_0.txt', delimiter='\t', header=None, nrows=records)
        else:
            self.train = pd.read_csv('./data/train_0.txt', delimiter='\t', header=None)
            self.test = pd.read_csv('./data/test_0.txt', delimiter='\t', header=None)

        self.train.columns = ['userid', 'songid', 'rating']
        self.test.columns = ['userid', 'songid', 'rating']
        self.songs.columns = ['songid', 'albumid', 'artistid', 'genreid']
        self.genre.columns = ['genreid', 'parentid', 'level', 'name']
        self.genre = self.format_genre(self.genre)

        # self.train0['rating'] = self.train0['rating'].apply(pd.to_numeric)

    def get_genre(self):
        return self.genre

    def get_songs(self):
        return self.songs

    def format_genre(self, genre):
        genre['fullgenreid'] = genre['genreid'].astype(str) + genre['parentid'].astype(str)+ genre['level'].astype(str)
        return genre

    def get_dataframe(self):
        train_df = pd.merge(self.train, self.songs, left_on='songid', right_on='songid')
        train_df = pd.merge(train_df, self.genre, left_on='genreid', right_on='genreid')
        test_df = pd.merge(self.test, self.songs, left_on='songid', right_on='songid')
        test_df = pd.merge(test_df, self.genre, left_on='genreid', right_on='genreid')
        return train_df, test_df