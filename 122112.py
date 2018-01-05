import pandas
import sys
from bs4 import BeautifulSoup
import requests

url = 'http://npb.jp/scores/2017/1104/h-db-06/playbyplay.html'
res = requests.get('http://npb.jp/scores/2017/1104/h-db-06/playbyplay.html')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
test1 = pandas.read_html(url)[3]
for i in range(4, len(pandas.read_html(url)), 1):
    test2 = pandas.read_html(url)[i]
    test1 = pandas.concat([test1, test2], axis=0, ignore_index=True)

baseball = pandas.DataFrame(test1)
baseball.columns = [soup.select('.w1')[0].text, soup.select('.w1')[1].text, soup.select('.w1')[2].text,
                    soup.select('.w1')[3].text, soup.select('.w2')[0].text]
reload(sys)
sys.setdefaultencoding('utf8')
baseball.to_excel('20171104.xlsx')