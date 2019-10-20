import re
from bs4 import BeautifulSoup, SoupStrainer
import requests


def scrapePage(url):
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data)
    headers = soup.find_all(re.compile(r'h\d+'))
    i = 0
    while(str(headers[i]).find("Plot") != 1):
        i+=1


