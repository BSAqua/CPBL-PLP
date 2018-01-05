# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import csv
import codecs
import requests

for date in range(1, 13, 1):
    year = 'http://www.cpbl.com.tw/schedule/index/2016-1-01.html?&date=2016-1-01&gameno=01&sfieldsub=&sgameno=01'
    string = '-' + str(date) + '-'
    month = year.replace('-1-', string)
    print(month)
    cpbl_schedule = requests.get(month).text
    soup = BeautifulSoup(cpbl_schedule, 'html.parser')
    table = soup.find_all('table', 'schedule_info')
    cpbl = 'http://www.cpbl.com.tw'

    for a in table:
        if a.find('a'):
            box = a.find('a')['href']
            play_by_play = box.replace('box', 'play_by_play')
            cpbl_plp = cpbl + play_by_play
            get = requests.get(cpbl_plp).text
            soup = BeautifulSoup(get, 'html.parser')
            allEvent = soup.findAll('td', attrs={'align': 'left'})

        with open(txt, 'wb') as csvFile:
                csvFile.write(codecs.BOM_UTF8)
                writer = csv.writer(csvFile, dialect='excel')

        for event in allEvent:
            cpblEvent = event.string.encode('utf-8')
            print (cpblEvent)
            writer.writerow([cpblEvent])
        writer.writerow([' '])

















