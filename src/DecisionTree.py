from sklearn import tree
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix, classification_report
import graphviz
from sklearn.model_selection import train_test_split, cross_val_score

class DecisionTree:
    def __init__(self, train_df):
        self.train_df = train_df

    def run_simulation(self, predict_value):
        print 'Decision Tree: '
        X = self.train_df.drop(predict_value, axis=1).drop('animal_name', axis=1)
        y = self.train_df[predict_value]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

        dt = tree.DecisionTreeClassifier()
        dt.fit(X_train, y_train)
        y_predicted = dt.predict(X_test)
        score = dt.score(X_test, y_test)

        print '\t Model Accuracy: '
        print '\t', score

        # Cross validation
        scores = cross_val_score(dt, X, y, scoring='accuracy', cv=10)
        print '\t Cross Validation: '
        print '\t', scores

    