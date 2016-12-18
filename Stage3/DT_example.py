from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=0)
iris = load_iris()
print(iris)
cross_val_score(clf, iris.data, iris.target, cv=10)
print(cross_val_score)