import json
from screp import scrap_quote, list_author, scrap_author

def save_f():
    with open('quote.json', 'w') as file:
        json.dump(scrap_quote(), file, indent=4)
    print('Quotes.json saved')

    with open('author.json', 'w') as file:
        json.dump(list_author, file, indent=4)
    print('Auhtors.json saved')


if __name__ == '__main__':
    save_f()
