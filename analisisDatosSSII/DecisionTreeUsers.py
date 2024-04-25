from sklearn import tree
from sklearn.tree import export_graphviz
from subprocess import call
import analisisDatos_ejercicio4
import numpy as np


def randomForestUser(pas, perms, clic, emails, phising):
    usersData, usersTarget = analisisDatos_ejercicio4.datosEntrenamiento()
    X, y = usersData, usersTarget
    users_X_train = X[:int(-0.40 * len(X))]
    users_X_test = X[int(-0.40 * len(y)):]
    users_y_train = y[:int(-0.40 * len(y))]
    users_y_test = y[int(-0.40 * len(y)):]
    clf = tree.DecisionTreeClassifier(max_depth=20, random_state=0, min_samples_leaf=5)
    clf = clf.fit(users_X_train, users_y_train)
    aux1 = [pas, perms, clic, emails, phising]
    uTest = np.array(aux1)
    uTest = np.array([uTest])
    aux = 0
    test = []
    for i in range(len(users_X_test)):
        test.append(clf.predict([users_X_test[i]]))
    for i in range(len(users_y_test)):
        if test[i] == users_y_test[i]:
            aux += 1
    print(aux / len(users_X_test))
    return clf.predict(uTest)

print(randomForestUser(0, 1, 23, 250, 1))