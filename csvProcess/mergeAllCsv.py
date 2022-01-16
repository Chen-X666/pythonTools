# _*_ coding: utf-8 _*_
"""
Time:     2021/11/30 10:26
Author:   ChenXin
Version:  V 0.1
File:     mergeAllCsv.py
Describe:  Github link: https://github.com/Chen-X666
"""
import csv
import os
import glob
import os
import pandas as pd

import pandas as pd

import datetime

inputfile = str(os.path.dirname(os.getcwd())) + "\\csvProcess\\CandidateWordResult\\*.csv"
print(inputfile)
outputfile = str(os.path.dirname(os.getcwd())) + "\\csvProcess\\trainingData4.csv"
csv_list = glob.glob(inputfile)

filepath = csv_list[0]
df = pd.read_csv(filepath,encoding='GBK')
df = df.to_csv(outputfile, index=False)

for i in range(1, len(csv_list)):
    print(csv_list[i])
    filepath = csv_list[i]
    df = pd.read_csv(filepath,encoding='GBK',error_bad_lines=False)
    df = df.to_csv(outputfile, index=False, header=False, mode='a+')
print('finished')