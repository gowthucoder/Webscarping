import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)


    if response.status_code == 200:
    
        soup = BeautifulSoup(response.text, 'html.parser')

        
        quotes = []
        for quote_div in soup.find_all('div', class_='quote'):
            text = quote_div.find('span', class_='text').text
            author = quote_div.find('small', class_='author').text
            quotes.append({'text': text, 'author': author})

        return quotes
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


url = 'http://quotes.toscrape.com'
quotes = scrape_quotes(url)


if quotes:
    for i, quote in enumerate(quotes, 1):
        print(f"{i}. {quote['text']} - {quote['author']}")
