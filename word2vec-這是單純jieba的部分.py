# -*- coding: utf-8 -*-

import
import jieba
import logging
import codecs
import csv

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("userdict.txt")

stopwordset = set()
with open('stopwords.txt','r') as sw:
    for line in sw:
        stopwordset.add(line.strip('\n'))

texts_num = 0

with open('cpbl_jieba.txt','w') as output:
    output.write(codecs.BOM_UTF8)
    with open('cpbl.txt','r') as cpbl:
        for line in cpbl:
            cpbl_words = jieba.cut(line,cut_all=False)
            for word in cpbl_words:
                if word not in stopwordset:
                    cpbl_word = word.encode('utf-8')
                    output.write(codecs.BOM_UTF8)
                    output.write('\n' + cpbl_word + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info('Already finished %d line jieba' % texts_num)