from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix, classification_report

# TODO: Take prediction value as input

class RandomForest:
    def __init__(self, train_df, test_df):
        self.train_df = train_df
        self.test_df = test_df

    def run_simulation(self, predict_value):
        random_forest = RandomForestClassifier(n_estimators=100)
        train_predictors = self.train_df.drop(predict_value, axis=1).drop("name", axis=1)
        train_actual = self.train_df[predict_value]

        test_predictors = self.test_df.drop(predict_value, axis=1).drop("name", axis=1)
        test_actual = self.test_df[predict_value]

        random_forest.fit(train_predictors, train_actual)
        sanity_score = random_forest.score(train_predictors, train_actual)

        y_predict = random_forest.predict(test_predictors)
        y_predict_confidence =  random_forest.predict_proba(test_predictors)[0:10]
        y_predict_accuracy = accuracy_score(test_actual, y_predict)
        y_predict_cohen_kappa = cohen_kappa_score(test_actual, y_predict)
        class_report = classification_report(test_actual, y_predict)

        print class_report
