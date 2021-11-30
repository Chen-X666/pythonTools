# _*_ coding: utf-8 _*_
"""
Time:     2021/11/30 10:26
Author:   ChenXin
Version:  V 0.1
File:     mergeAllCsv.py
Describe:  Github link: https://github.com/Chen-X666
"""
import os

import pandas as pd

import datetime

def getFileName(path):
    files = os.listdir(path)
    # print(files)
    filenames = []
    for file in files:
        filenames.append(file)
    # print(filenames)
    return filenames

if __name__ == '__main__':
    # 合并下面文件下所有excel文件：
    path = r'D:\小的项目\旅游分析\数据'
    # 读取该文件夹下的需要合并的文件路径
    filelist = getFileName(path)
    # 设置合并后文件的名字
    file_time = datetime.datetime.now()
    file_time = str(file_time).replace(' ', '_').replace(':','_').replace('-','_')[:-7]
    savename = file_time + '_合并文件.xlsx'
    # 存储合并的df
    savedata = []
    # 依次读取待合并数据：
    for file in filelist:
        # 读写文件
        filepath = path + "\\" + file
        print('需要合并的文件：', filepath)
        df = pd.read_excel(filepath)
        savedata.append(df)
        # 合并文件
        newdf = pd.concat(savedata)
        # 保存文件
        newdf.to_excel('./data/' + savename, index=False) # 保存文件，为追加模式，且不要列头
        print('合并后数据的大小：', newdf.shape)