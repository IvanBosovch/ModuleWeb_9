import requests
from bs4 import BeautifulSoup


domain = 'https://quotes.toscrape.com'
url = 'https://quotes.toscrape.com/'
response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
html = soup.prettify()
list_author = []


def scrap_quote():
        quotes = soup.find_all('div', class_='quote')

        list_quote = []

        for q in quotes:
            tags = []
            result_quotes = q.find('span').text
            result_author = q.find('small', class_='author').text.strip()
            author_url = domain + q.a['href']
            scrap_author(author_url)

            result_tags = q.find_all('a', class_='tag')

            for tag in result_tags:
                tags.append(tag.text)
                quote_dict = {'tags': tags, 'author': result_author, 'quote': result_quotes}
            list_quote.append(quote_dict)

        return list_quote

def scrap_author(author_url):
    author_response = requests.get(author_url)
    author_soup = BeautifulSoup(author_response.text, features="html.parser")

    authors = author_soup.find_all('div', class_='author-details')
    for author in authors:
        result_name = author.find('h3').text
        result_date = author.find('span', class_='author-born-date').text
        result_address = author.find('span', class_='author-born-location').text
        result_descriprion = author.find('div', class_='author-description').text.strip()
        list_author.append({'fullname': result_name, 'born_date': result_date, 'born_location': result_address, 'description': result_descriprion})
    return list_author



