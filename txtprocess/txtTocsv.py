# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pymysql
from sqlalchemy import create_engine
import pandas as pd
if __name__ == '__main__':
    videoType = "鬼畜类"
    startDate = "2017-01-01"
    for i in range(0, 48):
        print(startDate)
        videoType = "鬼畜类"
        fileNameCsv = r'C:\Users\Chen\Desktop\python\NewWordDiscovery\Data\guichu\%s%s.csv'% (videoType,str(startDate))
        fileNameTxt = r'C:\Users\Chen\Desktop\python\NewWordDiscovery\Data\guichu\%s%s.txt'% (videoType,str(startDate))
        import csv
        csvFile = open(fileNameCsv, 'w', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)
        csvRow = []
        f = open(fileNameTxt, 'r', encoding='utf-8')
        for line in f:
            csvRow = line.split()
            writer.writerow(csvRow)
        f.close()
        csvFile.close()
        startDate = (datetime.strptime(str(startDate), '%Y-%m-%d') + relativedelta(months=+1)).date()