from bs4 import BeautifulSoup
import csv
import codecs
import requests

kbo_web = 'https://mykbostats.com/games/4684-Kia-vs-Doosan-20160809'
kbo_plp = requests.get(kbo_web).text
kbo_plp_soup = BeautifulSoup(kbo_plp,'html.parser')
kbo_plp_log = kbo_plp_soup.find_all('div','inning-detail')

for log in kbo_plp_log:
    print log.text
