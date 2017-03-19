# GQtr 
parses https://goodreads.com/ to get quotes using tags

## Installation:

* install [Python 3](https://www.python.org/downloads/)
* install [pip](https://pypi.python.org/pypi/pip)
* clone this repository 
## Dependencies:  

* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [requests](http://docs.python-requests.org/en/master/)

install them using `pip install -r requirements.txt` 

## Usage:


* get a random quote: `python gqtr.py <tag>`

* getting a certain number of quotes(if available): `python gqtr.py <tag> <number of quotes (optional)>`

* for getting all quotes for the specified tag: `python gqtr.py <tag> all`