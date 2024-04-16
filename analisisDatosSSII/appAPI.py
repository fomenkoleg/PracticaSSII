from flask import Flask, render_template, request, jsonify
import analisisDatos_ejercicio4
import ejercicio3_5
import ejercicio1_2
import LinearRegressionUsers

app = Flask(__name__)

@app.route('/rest/parte2/usuariosCriticos/')
def uCritic():
    numberlines = request.args.get('numberline')
    if int(numberlines) <= 0:
        return "Error de entrada"

    aux = analisisDatos_ejercicio4.ejercicio_headnum(int(numberlines)).to_dict(orient='records')
    #show = aux.to_string().replace("\n", "<br>")
    #return show
    return jsonify(aux)

@app.route('/rest/parte2/usuariosCriticosSelect/')
def uCriticSelect():
    numberlines = request.args.get('numberline')
    mitad = request.args.get('mitad')
    if int(numberlines) <= 0 or int(mitad) not in [1, 2]:
        return "Error de entrada"

    aux = analisisDatos_ejercicio4.ejercicio_50percent(int(mitad), int(numberlines)).to_dict(orient='records')
    #show = aux.to_string().replace("\n", "<br>")
    #return show
    return jsonify(aux)

@app.route('/rest/parte2/webDesactualizadas/')
def wOutdated():
    numberlines = request.args.get('numberline')
    if(int(numberlines) < 0):
        return render_template('error.html')

    aux = ejercicio1_2.top_webs(int(numberlines))
    return jsonify(aux)

@app.route('/rest/parte2/ultimasVulnerabilidades')
def lastVulnerabilities():
    aux = ejercicio3_5.prueba()
    return jsonify(aux)

@app.route('/rest/parte2/prediccion/lineal/')
def predict():
    numberEmails = request.args.get('emails')
    #numberPhising = request.args.get('phising')
    aux = LinearRegressionUsers.func(int(numberEmails))
    return jsonify(str(aux))

if __name__ == '__main__':
    app.run()













