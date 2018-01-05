from bs4 import BeautifulSoup
import requests
get = requests.get("http://www.cpbl.com.tw/games/box.html?&game_type=01&game_id=1&game_date=2016")
soup = BeautifulSoup(get.text,"html.parser")
allEvent = soup.findAll("td", attrs={"align":"left"})

for event in allEvent:
    print event.string