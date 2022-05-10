import requests
from bs4 import BeautifulSoup

from Globals import Globals


def get_list():
    r = requests.get(Globals.url)
    soup = BeautifulSoup(r.content, 'html.parser')
    sp = soup.find('table', class_='data').text
    return sp.split("\n")
