# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import requests
import codecs
import csv


txt = 'npb.doc'

with open(txt, 'wb') as csvFile:
    csvFile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvFile, dialect='excel')

    npb_web = 'http://npb.jp/scores/2017/1101/db-h-04/playbyplay.html'
    npb_plp = requests.get(npb_web).text
    npb_soup = BeautifulSoup(npb_plp,'html.parser')
    npb_web_plp = npb_soup.find_all('td','w1')

    for print_plp in npb_web_plp:
        npb_plp_print = print_plp.get_text().encode('utf-8')
        print (npb_plp_print)
        writer.writerow([npb_plp_print])
