#!/bin/python
#-*- coding:utf-8 -*-
import sys
from collections import defaultdict
import random
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts

from IPython import embed

reload(sys)
sys.setdefaultencoding('utf-8')

filename = "../stockList.xlsx"

data = pd.read_excel(filename)
#embed()
l = data.index.size
#
dic_hangye1 = defaultdict(list)
dic_hangye2 = defaultdict(list)
dic_hangye2_to_hangye1 = defaultdict(dict)

def getHangye1():
	for i in data.index:
		code = data.iloc[i, 0]
		name = data.iloc[i, 1]
		hangyes = data.iloc[i, 3]
		if not type(hangyes) == unicode:
			continue
		lst_hangye = hangyes.split("--")
		if not len(lst_hangye) >= 1:
			continue
		hangye1 = lst_hangye[0].strip()
		hangye2 = lst_hangye[1].strip()
		#print code, name, hangye1, hangye2
		dic_hangye1[hangye1].append(code)
		dic_hangye2[hangye2].append(code)
		dic_hangye2_to_hangye1[hangye1][hangye2] = 1
	print "Read all Stock information done..."

def processData():
	for k,v in dic_hangye1.items():
		print u"行业：", k
		for c in v:
			print c
			s = c.split(".")
			res = ts.get_notices(code = s[0])
			print res

def main():
	getHangye1()
	processData()

if __name__=="__main__":
	main()