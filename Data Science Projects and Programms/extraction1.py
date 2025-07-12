import pandas as pd
import requests as r
from bs4 import BeautifulSoup
m = r.get('https://www.w3schools.com/python/default.asp').text
v=BeautifulSoup(m,'html.parser')
menu = v.find('div', id='leftmenuinnerinner')
y=menu.find_all('a')
for link in y:
    text = link.text.strip()
    print(text)