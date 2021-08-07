# -*- coding: utf-8 -*-
import glob
import os
import numpy as np
import pandas as pd
import csv

def getFileName():
    path = r'C:\Users\Chen\Desktop\python\NewWordDiscovery\标注集\鬼畜类'  # 批量表格所在文件路径
    file = glob.glob(os.path.join(path, "鬼畜类**.csv"))  # 每一个表格相同名称部分
    print(file)
    pds=[]

    for f in file:
        pd0 = pd.read_csv(f, index_col=None, encoding='utf-8',error_bad_lines=False,quoting=csv.QUOTE_NONE)  # 读取每个表格
        pds.append(pd0)
    print(pds[2])
    a=pds[0].iloc[:, 1:10].fillna(0).values
    b=pds[1].iloc[:, 1:10].fillna(0).values
    c=pds[2].iloc[:, 1:10].fillna(0).values
    #dictA = a.to_dict('records')
    wordList1 = []
    wordList2 = []
    wordList3 = []
    for i in a:
        for j in i:
            wordList1.append(j)
    for i in b:
        for j in i:
            wordList2.append(j)
    for i in c:
        for j in i:
            wordList3.append(j)

    li1 = list(set(wordList1))
    li2 = list(set(wordList2))
    li3 = list(set(wordList3))
    tt = set(li1).union(set(li2)).union(set(li3))
    # print(len(li1))
    # print(len(li2))
    print(len(tt))
    print(tt)
    result = pd.read_csv("result\\NewWordDiscovery_10wSample.csv_20210601163441.csv",error_bad_lines=False,quoting=csv.QUOTE_NONE,encoding='utf-8')
    print(result)
    df = result[result["word"].isin(tt)]
    df.to_csv("1.csv",encoding='utf-8')
    print(df)
    factor = df.iloc[:, 1:10]
    X_train = np.array(factor)
    print(X_train)
    #df = pd.concat(dl)  # 合并
    #df.to_csv('Data\Result.csv',encoding='utf-8')
    return 'success'

if __name__ == '__main__':
    getFileName()