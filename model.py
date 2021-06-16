import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


class Model(object):

    def __init__(self):
        u = np.array([[-0.39687045, 0.96060931, -2.37424058, -1.00306368],
                      [0.51255844, -0.25286013, -0.21518908, -0.76941246],
                      [-0.11568799, -0.70774918, 2.58942965, 1.77247614]])
        b = np.array([9.03178957, 1.84119789, -10.87298745])
        c = np.array([0, 1, 2])
        self.clf = LogisticRegression(random_state=0, max_iter=1000)
        self.clf.coef_ = u
        self.clf.intercept_ = b
        self.clf.classes_ = c

    def predict(self, X):
        return self.clf.predict(X)


if __name__ == "__main__":
    from sklearn.model_selection import train_test_split
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = Model()
    print(model.predict(X_test))
    print(y_test)
