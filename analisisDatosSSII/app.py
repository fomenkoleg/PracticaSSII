import datetime
from markupsafe import Markup
from flask import Flask, render_template, request
import analisisDatos_ejercicio2
import analisisDatos_ejercicio3
import analisisDatos_ejercicio4

app = Flask(__name__)

@app.route("/parte1/ejercicio4")
def ejercicio4():
    palabras = analisisDatos_ejercicio4.ejercicio4_1()
    palabras2 = analisisDatos_ejercicio4.ejercicio4_2()
    palabras3 = analisisDatos_ejercicio4.ejercicio4_3()
    palabras4 = analisisDatos_ejercicio4.ejercicio4_4()
    text = ''
    text2 = ''
    text3 = ''
    text4 = ''
    for line in palabras.split('\n'):
        text += Markup.escape(line) + Markup('<br />')
    for line in palabras2.split('\n'):
        text2 += Markup.escape(line) + Markup('<br />')
    for line in palabras3.split('\n'):
        text3 += Markup.escape(line) + Markup('<br />')
    for line in palabras4.split('\n'):
        text4 += Markup.escape(line) + Markup('<br />')

    #palabras = palabras.replace("\n", "<br>")
    #palabras = palabras.replace("\r", "<br>")
    return render_template('ejercicio4.html', ejer1=text, ejer2=text2, ejer3=text3, ejer4=text4)

@app.route('/parte1/ejercicio3')
def ejercicio3():  # put application's code here
    aux = analisisDatos_ejercicio3.ejercicio3()
    aux2 = aux.replace("\n", "<br>")
    return aux2

@app.route('/parte1/ejercicio2')
def ejercicio2():  # put application's code here
    aux = analisisDatos_ejercicio2.ejercicio2()
    aux2 = aux.replace("\n", "<br>")
    return aux2

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/parte1')
def parte1():
    return render_template('parte1.html')
@app.route('/parte2')
def usuariosCriticos():
    return render_template('parte2.html')

@app.route('/parte2/usuariosCriticos')
def userCritic():
    return render_template('userCritic.html')

@app.route('/parte2/usuariosCriticos/')
def uCritic():
    numberlines = request.args.get('numberline')
    aux = analisisDatos_ejercicio4.ejercicio4_2().head(int(numberlines))
    show = aux.to_string().replace("\n", "<br>")
    return show


if __name__ == '__main__':
    app.run()
