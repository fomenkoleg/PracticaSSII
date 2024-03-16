from flask import Flask
from analisisDatosSSII import analisisDatos_ejercicio2

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/ejercicio2')
def printResoults2():
    return analisisDatos_ejercicio2.ejercicio2()

if __name__ == '__main__':
    app.run()
