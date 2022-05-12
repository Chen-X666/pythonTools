# _*_ coding: utf-8 _*_
"""
Time:     2022/5/5 12:00
Author:   ChenXin
Version:  V 0.1
File:     pretreatment.py
Describe:  Github link: https://github.com/Chen-X666
"""
import pandas as pd
import xlrd
writer = pd.ExcelFile('ori/交房情况表 .xls')
sheet_len = len(writer.sheet_names)
print(sheet_len)
# 指定下标读取
names = []
calls = []
for i in range(0,sheet_len):
    df = pd.read_excel(writer,sheet_name=i)
    temp = str(df.columns[0]).split('丹')[0]
    df = pd.read_excel(writer, sheet_name=i, header=1)
    df['房号'] = df['房号'].apply(lambda x: temp+str(x))
    df['房号.1'] = df['房号.1'].apply(lambda x: temp + str(x))
    df['房号'] = df['房号'] + df['业主姓名']
    df['房号.1'] = df['房号.1'] + df['业主姓名.1']
    names.extend(df['房号'].to_list())
    names.extend(df['房号.1'].to_list())
    calls.extend(df['电话'].to_list())
    calls.extend(df['电话.1'].to_list())
print(len(names))
print(names)
print(len(calls))
data = pd.DataFrame(columns=['name','call'])
data['name'] = names
data['call'] = calls
data.to_csv('1.csv')


