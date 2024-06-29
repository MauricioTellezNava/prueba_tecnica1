from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Creando un header
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

request = requests.get('https://www.milenio.com/', headers=headers)
html = request.content

# Creando soup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())  # Para buscar los elementos necesarios

articles = []

for h in soup.findAll("a", class_="board-module__a"):
    if h.get('target') != '_blank':
        name = h.contents[0]
        link = h['href']
        category = link.split('/')[1]

        article = {
            "name": name,
            "link": link,
            "category": category
        }

        articles.append(article)

# Código para crear un dataset con las columnas 'name', 'link' y 'category'
df = pd.DataFrame(articles, columns=['name', 'link', 'category'])

from datetime import datetime
now = datetime.now()
date_time = now.strftime("%H%M_%d%m%Y")
filename = f"noticias_{date_time}.csv"
df.to_csv(filename, index=False)
