from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():

    wine = datasets.load_wine()

    print(wine.feature_names)

    print(wine.target_names)

    print(wine.data[0:5])

    print(wine.target)

    X_train,X_test,Y_train,Y_test = train_test_split(wine.data,wine.target,test_size = 0.3)

    knn = KNeighborsClassifier(n_neighbors = 3)

    knn.fit(X_train,Y_train)

    Y_pred = knn.predict(X_test)

    print("Accuracy:",metrics.accuracy_score(Y_test,Y_pred))


def main():

    print("Machine learning Application")

    print("Wine predictor application using K Nearest Knighbor algorithm")

    WinePredictor()

if __name__ == "__main__":
    main()