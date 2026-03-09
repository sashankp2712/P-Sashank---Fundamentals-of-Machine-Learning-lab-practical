from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,random_state=1
)

# KNN model
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train,y_train)

pred = knn.predict(X_test)

print("Predicted Classes:", pred)
print("Actual Classes:", y_test)

print("Accuracy:", accuracy_score(y_test,pred))
