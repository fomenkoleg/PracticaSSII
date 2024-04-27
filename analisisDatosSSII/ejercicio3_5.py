import requests

def vulnerabilidades():
    page = requests.get("https://cve.circl.lu/api/last")
    aux = page.json()
    l = []
    for i in range(10):
        aux1 = aux[i]
        vul = "<h2>"+aux1['id']+'</h2><br>Summary: '+aux1['summary']+'<br>' + 'Published: '+aux1['Published']+'<br>Last Modified: '+aux1['last-modified']+'<br>'+'References: <br>'
        for j in aux1['references']:
            vul = vul + str(j) + ' '
        vul = vul + '<br>'
        vul = vul + 'Vulnerable configuration: <br>'
        for j in aux1['vulnerable_configuration']:
            vul = vul + str(j) + ' '
        vul = vul + '<br>'
        vul = vul+ 'Vulnerable products: <br>'
        for j in aux1['vulnerable_configuration']:
            vul = vul + str(j) + ' '
        vul = vul + '<br>'
        l.append(vul)
    news = ''
    for i in l:
        news = news + i + '<br><br>'
    return news