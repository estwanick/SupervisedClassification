# Random Forest / Naiive Bayes
from src.loader import DataFactory
import matplotlib
import numpy as np

import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = DataFactory()
genre = df.join()