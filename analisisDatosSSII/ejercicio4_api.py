import requests

def ejercicio4API():
    page = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    page_json = page.json()
    l = []
    for i in range(10):
        id_historia = page_json[i]
        historia = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id_historia}.json").json()
        titulo = historia['title']
        autor = historia['by']
        url = historia['url']
        text = historia['text']
        l.append(f'<h2>{titulo}</h2>Autor: {autor}<br>URL: <a href="{url}">{url}</a><br>Texto: {text}')
    news = ''
    for i in l:
        news = news + i + '<br><br>'
    return news