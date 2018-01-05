from bs4 import BeautifulSoup
import requests
knbsb = requests.get("https://www.knbsbstats.nl/2017/HB/statsHB/1335.htm")
soup = BeautifulSoup(knbsb.text,"html.parser")
font = soup.find_all("font",face = {"verdana"},size = {2})

for plp in font:
    print plp.get_text()




