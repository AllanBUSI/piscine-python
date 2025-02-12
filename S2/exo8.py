# Exercice 8: Web scraping avec BeautifulSoup
# Utilisez la bibliothèque BeautifulSoup pour extraire les titres et les liens des derniers articles d'un site web d'actualités.

import requests
from bs4 import BeautifulSoup

def scrape_news_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        print(f"Title: {title}\nLink: {link}\n")

# Exemple d'utilisation
url = 'https://example-news-website.com'
scrape_news_articles(url)
