import requests

def ejercicio4API():
    page = requests.get("https://cve.circl.lu/api/cve/CVE-2010-3333")
    aux = page.json()
    l = []
    for i in range(10):
        aux1 = aux["capec"][i]
        vul = "<h2>"+aux1["name"]+' '+aux1['id']+'</h2><br>Prerequisites: '+aux1['prerequisites']+'<br>'+aux1['summary']+'<br>' + 'Related weakness: '
        for j in aux1['related_weakness']:
            vul = vul + str(j) + ' '
        vul = vul + '<br>'
        l.append(vul)
    news = ''
    for i in l:
        news = news + i + '<br><br>'
    return news