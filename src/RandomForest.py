from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, cross_val_score

class RandomForest:
    def __init__(self, train_df):
        self.train_df = train_df

    def run_simulation(self, predict_value):
        print 'Random Forest: '
        X = self.train_df.drop(predict_value, axis=1).drop('animal_name', axis=1)
        y = self.train_df[predict_value]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=27)

        random_forest = RandomForestClassifier(n_estimators=100, random_state=30)
        random_forest.fit(X_train, y_train)
        y_predict = random_forest.predict(X_test)
        score = random_forest.score(X_test, y_test)

        print '\t Model Accuracy: '
        print '\t', score

        # Cross validation
        scores = cross_val_score(random_forest, X, y, scoring='accuracy', cv=10)
        print '\t Cross Validation: '
        print '\t', scores