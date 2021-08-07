# -*- coding: utf-8 -*-

import csv
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
def countSumLine(tableType,videoType,startDate):
    lines = 0
    for i in range(0,48):
        fileNameTxt = r'C:\Users\Chen\Desktop\python\NewWordDiscovery\Data\%s\%s%s.txt' % (
        tableType,videoType, str(startDate))
        myfile = open(fileNameTxt,encoding='utf-8')
        line = len(myfile.readlines())
        lines = lines + line
        startDate = (datetime.strptime(str(startDate), '%Y-%m-%d') + relativedelta(months=+1)).date()
    return lines


if __name__ == '__main__':
    startDate = "2017-01-01"
    tableType = "guichu"
    videoType = "鬼畜类"
    SumLine = countSumLine(tableType,videoType,startDate)
    print(SumLine)
    sum = 100000
    csvFileName = r'C:\Users\Chen\Desktop\python\NewWordDiscovery\Data\%s\10wSample.csv' % (tableType)
    for i in range(0,48):
        fileName = r'C:\Users\Chen\Desktop\python\NewWordDiscovery\Data\%s\%s%s.txt' % (tableType, videoType, str(startDate))
        print(fileName)
        df = pd.read_table(fileName, encoding='utf-8',error_bad_lines=False,quoting=csv.QUOTE_NONE)
        line = df.count()
        df.drop_duplicates(subset=['bulletContent'],keep='first',inplace=True)
        n = sum * line/SumLine
        print(round(n))
        sample = df.sample(n=int(round(n * 1000000) / 1000000.0), random_state=None,axis=0,replace=False)
        sample.to_csv(csvFileName, mode='a', header=False,index=False)
        print(sample)
        startDate = (datetime.strptime(str(startDate), '%Y-%m-%d') + relativedelta(months=+1)).date()

