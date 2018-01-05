# -*- coding: UTF-8 -*-
import csv
import codecs
with open('test.csv', 'wb') as csvfile:
    csvfile.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['測試'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
