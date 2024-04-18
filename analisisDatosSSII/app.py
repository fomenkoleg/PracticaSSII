import io
import requests
from bs4 import BeautifulSoup
from markupsafe import Markup
from flask import Flask, render_template, request, make_response
from xhtml2pdf import pisa
import analisisDatos_ejercicio2
import analisisDatos_ejercicio3
import analisisDatos_ejercicio4
import ejercicio3_5
import ejercicio1_2
import ejercicio4_api
import LinearRegressionUsers
import RandomForestUsers


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
        text3 += (Markup.escape(line) + Markup('<br />'))

@app.route('/parte1/ejercicio3')
def ejercicio3():  # put application's code here
    aux = analisisDatos_ejercicio3.ejercicio3()
    aux2 = aux.replace("\n", "<br>")
    return aux2
    for line in palabras4.split('\n'):
        text4 += Markup.escape(line) + Markup('<br />')

    #palabras = palabras.replace("\n", "<br>")
    #palabras = palabras.replace("\r", "<br>")
    return render_template('ejercicio4.html', ejer1=text, ejer2=text2, ejer3=text3, ejer4=text4)



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
def parte2():
    return render_template('parte2.html')

@app.route('/parte2/usuariosCriticos')
def userCritic():
    return render_template('userCritic.html')

@app.route('/parte2/usuariosCriticosSelect')
def userCriticSelect():
    return render_template('userCriticHalves.html')

@app.route('/parte2/usuariosCriticos/')
def uCritic():
    numberlines = request.args.get('numberline')
    if int(numberlines) <= 0:
        return render_template('error.html')

    aux = analisisDatos_ejercicio4.ejercicio_headnum(int(numberlines)).to_dict(orient='records')
    #show = aux.to_string().replace("\n", "<br>")
    #return show
    return render_template('userCritic.html', usuarios=aux)


@app.route('/parte2/usuariosCriticos/downloadPDF')
def download():
    numberlines = request.args.get('numberline')
    html_content = requests.get(f"http://127.0.0.1:5000/parte2/usuariosCriticos/?numberline={numberlines}").content

    soup = BeautifulSoup(html_content, 'html.parser')
    first_container = soup.findAll('div', {'class': 'container'})[1]
    first_container.decompose()
    pdf_button = soup.find('a', class_='btn btn-primary')
    pdf_button.decompose()
    modified_html = str(soup)

    pdf_data = io.BytesIO()

    pisa.CreatePDF(modified_html, dest=pdf_data)

    pdf_data.seek(0)
    pdf_content = pdf_data.read()

    response = make_response(pdf_content)
    response.headers['Content-Disposition'] = 'attachment; filename=UsuariosCriticos.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response


@app.route('/parte2/usuariosCriticosSelect/')
def uCriticSelect():
    numberlines = request.args.get('numberline')
    mitad = request.args.get('mitad')
    if int(numberlines) <= 0 or int(mitad) not in [1, 2]:
        return render_template('error.html')

    aux = analisisDatos_ejercicio4.ejercicio_50percent(int(mitad), int(numberlines)).to_dict(orient='records')
    #show = aux.to_string().replace("\n", "<br>")
    #return show
    return render_template('userCriticHalves.html', usuarios=aux)

@app.route('/parte2/usuariosCriticosSelect/downloadPDF')
def pdfCriticSelect():
    numberlines = request.args.get('numberline')
    mitad = request.args.get('mitad')
    html_content = requests.get(f"http://127.0.0.1:5000/parte2/usuariosCriticosSelect/?numberline={numberlines}&mitad={mitad}").content

    soup = BeautifulSoup(html_content, 'html.parser')
    first_container = soup.findAll('div', {'class': 'container'})[1]
    first_container.decompose()
    pdf_button = soup.find('a', class_='btn btn-primary')
    pdf_button.decompose()
    modified_html = str(soup)

    pdf_data = io.BytesIO()

    pisa.CreatePDF(modified_html, dest=pdf_data)

    pdf_data.seek(0)
    pdf_content = pdf_data.read()

    response = make_response(pdf_content)
    response.headers['Content-Disposition'] = 'attachment; filename=UsuariosCriticosMitades.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response

@app.route('/parte2/webDesactualizadas')
def websOutdated():
    return render_template('outdatedWeb.html')

@app.route('/parte2/webDesactualizadas/')
def wOutdated():
    numberlines = request.args.get('numberline')
    if(int(numberlines) < 0):
        return render_template('error.html')

    aux = ejercicio1_2.top_webs(int(numberlines))
    return render_template('outdatedWeb.html', desactualizadas=aux)

@app.route('/parte2/websDesactualizadas/downloadPDF')
def webDesacPDF():
    numberlines = request.args.get('numberline')
    html_content = requests.get(f"http://127.0.0.1:5000/parte2/webDesactualizadas/?numberline={numberlines}").content

    soup = BeautifulSoup(html_content, 'html.parser')
    first_container = soup.findAll('div', {'class': 'container'})[1]
    first_container.decompose()
    pdf_button = soup.find('a', class_='btn btn-primary')
    pdf_button.decompose()
    modified_html = str(soup)

    pdf_data = io.BytesIO()

    pisa.CreatePDF(modified_html, dest=pdf_data)

    pdf_data.seek(0)
    pdf_content = pdf_data.read()

    response = make_response(pdf_content)
    response.headers['Content-Disposition'] = 'attachment; filename=WebsDesactualizadas.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response

@app.route('/parte2/ultimasVulnerabilidades')
def lastVulnerabilities():
    aux = ejercicio3_5.prueba()
    return aux

@app.route('/parte2/hackerNews')
def lastNews():
    aux = ejercicio4_api.ejercicio4API()
    return aux

@app.route('/parte2/prediccion/lineal')
def predictUser():
    return render_template('preddictUser.html')

@app.route('/parte2/prediccion/lineal/')
def predict():
    numberEmails = request.args.get('emails')
    numberclic = request.args.get('clic')
    numberEmails = int(numberEmails)
    numberclic = int(numberclic)
    if numberEmails <= 0 or numberclic > numberEmails:
        return render_template('error.html')
    aux = LinearRegressionUsers.func(numberclic/numberEmails)
    aux = aux * 100
    aux = "{:.2f}%".format(aux)
    return render_template('preddictUser.html', prediccionLineal=str(aux))

@app.route('/parte2/prediccion/RF')
def predictUserRF():
    return render_template('preddictUserRF.html')

@app.route('/parte2/prediccion/RF/')
def predictRF():
    numberPass = request.args.get('pass')
    numberPerms = request.args.get('perms')
    numberClic = request.args.get('clic')
    numberEmails = request.args.get('emails')
    numberPhising = request.args.get('phishing')
    if int(numberEmails) < 0 or (int(numberPhising) > int(numberEmails) or int(numberClic) > int(numberEmails)):
        return render_template('error.html')
    if numberPass == 'on':
        numberPass = 1
    else:
        numberPass = 0
    if numberPerms == 'on':
        numberPerms = 1
    else:
        numberPerms = 0
    aux = RandomForestUsers.randomForestUser(int(numberPass), int(numberPerms), int(numberClic),int(numberEmails), int(numberPhising))
    return render_template('preddictUserRF.html', prediccion=str(aux[0]))

    #numberPhising = request.args.get('phising')



if __name__ == '__main__':
    app.run()
