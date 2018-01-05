from bs4 import BeautifulSoup
import csv
import requests

txt = 'knbsnplp.txt'
with open(txt, 'wb') as csvFile:
    writer = csv.writer(csvFile, dialect='excel')

    knbsb_web = 'https://www.knbsbstats.nl/honkbal/hb-uitslagen-programma/'
    knbsb_schedle = requests.get(knbsb_web).text
    knbsb_soup = BeautifulSoup(knbsb_schedle,'html.parser')
    knbsb_plp_web = knbsb_soup.find_all('tr')

    for knbsb_plp_print in knbsb_plp_web:
        if knbsb_plp_print.find('a'):
            box = knbsb_plp_print.find('a')['href']
            knbsb_plp = requests.get(box)
            knbsb_plp_soup = BeautifulSoup(knbsb_plp.text,'html.parser')
            knbsb_plp_log = knbsb_plp_soup.find_all("font", face={"verdana"}, size={2})

            for knbsb_plp_log_print in knbsb_plp_log:
                print knbsb_plp_log_print.text
                print ' '
                print ' '
                writer.writerow([knbsb_plp_log_print.text])
                writer.writerow(' ')
                writer.writerow(' ')
            writer.writerow([' '])

