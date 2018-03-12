# Random Forest / Naiive Bayes
from src.loader import DataFactory
from src.RandomForest import RandomForest
import matplotlib
import numpy as np

import matplotlib.pyplot as plt

df = DataFactory(records=10)
test_df, train_df = df.get_dataframe()
rf = RandomForest(train_df, test_df)
rf.run_simulation('rating')