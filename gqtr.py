"""
GQtr
parses https://goodreads.com/ to get quotes using tags

Usage:

get a random quote:
python gqtr.py <tag>

getting a certain number of quotes(if available):
python gqtr.py <tag> <number of quotes (optional)>

for all quotes:
python gqtr.py <tag> all

"""
__author__ = "wasi0013"
import sys, random
import requests, bs4


url = 'https://goodreads.com/quotes/tag/'
d = {}


def get_quotes(base_url, tag, num_of_quotes = None, page = ''):
    url = base_url + tag + page
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    [row.extract() for row in  soup.findAll(['script', 'br'])]
    divs = soup.select('div.quoteText')
    for div in divs:
        text, author = (i.strip() for i in div.getText().strip().split('―'))
        d[text] = author
    length = len(d)
    if num_of_quotes:
        if length >= num_of_quotes:
            return d

    next_page = soup.select('a.next_page')
    for link in next_page:
        page = link['href'].split('?')[1]
        print('Quotes gathered so far %d Parsing: %s'% (length, page))
        get_quotes(base_url, tag, num_of_quotes, '?' + page)
    return d


if __name__ == '__main__':
    l = len(sys.argv)
    num = None
    quotes = {}

    if  l < 2:
        print('Error: No tags were provided!\nType "python', sys.argv[0],'<your tag> <num of quotes(optional>"')
    else:
        if l > 2:
            try:
                num = int(sys.argv[2])
                print('Getting ', num,' quotes for the tag:', sys.argv[1], ". Please be patient")
                quotes = get_quotes(url, sys.argv[1], num)
            except:
                print('Warning: Getting all quotes for the tag:', sys.argv[1], "\nThis may take a while, please be patient")
                quotes = get_quotes(url, sys.argv[1])
            #print quotes
            for i, quote in enumerate(quotes):
                if num:
                    num -= 1
                elif num == 0:
                    break
                print("%d:"%(i+1))
                print(quote)
                print('-')
                print(quotes[quote])

        else:
                seed = random.randint(1,999)
                print('Getting a random quote for the tag:', sys.argv[1], "using seed: %d. Please be patient"%seed)
                quotes = get_quotes(url, sys.argv[1], seed)
                quote, author = random.choice(list(quotes.items()))
                print(quote,'\n-\n'+author)

            
    