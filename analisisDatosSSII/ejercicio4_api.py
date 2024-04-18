import requests

def ejercicio4API():
    page = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    page_json = page.json()
    l = []
    cont = 0
    while len(l) < 10:
        id_historia = page_json[cont]
        historia = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id_historia}.json").json()
        if historia['type'] == 'story':
            if 'url' in historia and len(historia['kids']) >= 3 and 'title' in historia and 'by' in historia:
                titulo = historia['title']
                autor = historia['by']
                url = historia['url']
                top_comments = historia['kids'][:3]

                #text = historia['text']
                l.append(f'<h2>{titulo}</h2>Autor: {autor}<br>Leer más: <a href="{url}">{url}</a>')
                com1 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{top_comments[0]}.json").json()
                com2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{top_comments[1]}.json").json()
                com3 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{top_comments[2]}.json").json()
                l.append(f'<h4>Top 3 comentarios:</h4>'
                         f'<br><b>{com1["by"]}</b><br>{com1["text"]}'
                         f'<br><b>{com2["by"]}</b><br>{com2["text"]}'
                         f'<br><b>{com3["by"]}</b><br>{com3["text"]}')


        cont += 1
    news = ''
    for i in l:
        news = news + i + '<br><br>'
    return news