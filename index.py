# Random Forest / Naiive Bayes
from src.loader import DataFactory

from src.DecisionTree import DecisionTree
from src.RandomForest import RandomForest
import numpy as np

import matplotlib.pyplot as plt

df = DataFactory()
animal_df = df.get_dataframe()

dt = DecisionTree(animal_df)
dt.run_simulation('class_type')

rf = RandomForest(animal_df)
rf.run_simulation('class_type')