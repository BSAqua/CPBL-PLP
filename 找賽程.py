from bs4 import BeautifulSoup
import requests
cpbl_html = requests.get("http://www.cpbl.com.tw/schedule/index/2016-3-01.html?&date=2016-3-01&gameno=01&sfieldsub=&sgameno=01")
soup = BeautifulSoup(cpbl_html.text,"html.parser")
allEvent = soup.find_all("a")

for html in allEvent:
    print(html["href"])