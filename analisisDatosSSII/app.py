from flask import Flask
import analisisDatos_ejercicio2
import analisisDatos_ejercicio3
import analisisDatos_ejercicio4

app = Flask(__name__)


@app.route('/ejercicio3')
def ejercicio3():  # put application's code here
    aux = analisisDatos_ejercicio3.ejercicio3()
    aux2 = aux.replace("\n", "<br>")
    return aux2

@app.route('/ejercicio2')
def ejercicio2():  # put application's code here
    aux = analisisDatos_ejercicio2.ejercicio2()
    aux2 = aux.replace("\n", "<br>")
    return aux2

@app.route('/')
def hello_world():
    return 'holis'

if __name__ == '__main__':
    app.run()
