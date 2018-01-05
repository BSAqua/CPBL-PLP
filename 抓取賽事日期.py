from bs4 import BeautifulSoup

import requests

get = requests.get("http://www.cpbl.com.tw/schedule/index/2017-07-13.html?&date=2017-07-13&gameno=01&sfieldsub=&sgameno=01")
soup = BeautifulSoup(get.text,"html.parser")
allEvent = soup.findAll("th", attrs={"class":"past"})

for event in allEvent:
    print event.string

