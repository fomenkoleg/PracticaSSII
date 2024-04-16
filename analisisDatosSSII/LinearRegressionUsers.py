import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import analisisDatos_ejercicio4

def func(emails):
# Load the dataset

    users_X, users_y = analisisDatos_ejercicio4.datosEntrenamiento()
    X = []
# Use only one feature
    for i in users_X:
        pas, perm, em, phis, clic = i
        aux =[clic/em]
        aux = np.array(aux)
        X.append(aux)

    users_X = np.array(X)
# Split the data into training/testing sets
    users_X_train = users_X[:int(-0.40*len(users_X))]
    users_X_test = users_X[int(-0.40*len(users_X)):]
# Split the targets into training/testing sets
    users_y_train = users_y[:int(-0.40*len(users_y))]
    users_y_test = users_y[int(-0.40*len(users_y)):]
# Create linear regression object
    regr = linear_model.LinearRegression()
# Train the model using the training sets
    regr.fit(users_X_train, users_y_train)
    print(regr.coef_)
# Make predictions using the testing set
    users_y_pred = regr.predict(users_X_test)
# The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(users_y_test, users_y_pred))
# Plot outputs
    plt.scatter(users_X_test, users_y_test, color="black")
    plt.plot(users_X_test, users_y_pred, color="blue", linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()
    l = [emails]
    aux = [np.array(l)]
    e = regr.predict(np.array(aux))
    print(str(e[0]))
    return e[0]

func(0.12)