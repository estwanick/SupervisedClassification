import pandas as pd

class DataFactory:
    def __init__(self, records=None):
        self.predict = pd.read_csv('./data/zoo-animal-classification/class.csv', header=0, delimiter=',', dtype='category')

        if records:
            self.train = pd.read_csv('./data/zoo-animal-classification/zoo.csv', header=0, delimiter=',', nrows=records, dtype='category')
        else:
            self.train = pd.read_csv('./data/zoo-animal-classification/zoo.csv', header=0, delimiter=',', dtype='category')

    def get_dataframe(self):
        return self.train
        # return self.train.merge(self.predict, left_on='class_type', right_on='Class_Number')
