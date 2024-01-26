# Simple full href extractor

import requests
from bs4 import BeautifulSoup

host = input('Site to check: ')

req = requests.get('http://' + host)
data_read = req.text

real_stuff = BeautifulSoup(data_read, features='html.parser')

#print(real_stuff)

for x in real_stuff.find_all('a'):
    print(x.get('href'))
