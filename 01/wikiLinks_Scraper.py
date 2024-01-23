import requests
from bs4 import BeautifulSoup
import re
import time
import random

pages = set()

def getLinks(pageUrl):
    global pages
    # set headers to imitate a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    # add delay to not overload the server
    time.sleep(random.uniform(0, 2))
    # make HTTP request with headers
    response = requests.get('http://en.wikipedia.org{}'.format(pageUrl), headers=headers)
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*200)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
                getLinks('')
                
if __name__ == "__main__":
    getLinks('')