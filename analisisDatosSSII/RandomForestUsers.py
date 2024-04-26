from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import graphviz
import analisisDatos_ejercicio4
import numpy as np


def randomForestUser(pas, perms, clic, emails, phising):
    usersData, usersTarget = analisisDatos_ejercicio4.datosEntrenamiento()
    X, y = usersData, usersTarget
    users_X_train = X[:int(-0.40 * len(X))]
    users_X_test = X[int(-0.40 * len(y)):]
    users_y_train = y[:int(-0.40 * len(y))]
    users_y_test = y[int(-0.40 * len(y)):]
    clf = RandomForestClassifier(max_depth=5, random_state=0, n_estimators=100)
    clf.fit(users_X_train, users_y_train)
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

    for i in range(10):
        estim = clf.estimators_[i]
        dot_data = tree.export_graphviz(estim, out_file=None, feature_names=X.dtype.names,
                    class_names=['No es crítico', 'Es crítico'], rounded=True, proportion=False,
                    precision=2, filled=True)
        grafica = graphviz.Source(dot_data)
        grafica.render('RandomForest/tree' + str(i))

    return clf.predict(uTest)

def randomForestUser1():
    usersData, usersTarget = analisisDatos_ejercicio4.datosEntrenamiento()
    X, y = usersData, usersTarget
    users_X_train = X[:int(-0.40 * len(X))]
    users_X_test = X[int(-0.40 * len(y)):]
    users_y_train = y[:int(-0.40 * len(y))]
    users_y_test = y[int(-0.40 * len(y)):]
    clf = RandomForestClassifier(max_depth=5, random_state=0,n_estimators=100)
    clf.fit(users_X_train, users_y_train)

    aux = 0
    test = []
    for i in range(len(users_X_test)):
        test.append(clf.predict([users_X_test[i]]))
    for i in range(len(users_y_test)):
        if test[i] == users_y_test[i]:
            aux += 1
    print(aux/len(users_X_test))

print(randomForestUser(0, 1, 23, 250, 1))