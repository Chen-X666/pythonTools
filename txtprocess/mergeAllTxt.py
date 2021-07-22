# _*_ coding: utf-8 _*_
"""
Time:     2021/7/22 21:32
Author:   ChenXin
Version:  V 0.1
File:     mergeAllTxt.py
Describe:  Github link: https://github.com/Chen-X666
"""
import os

def mergeAllTxt():
    # coding=utf-8
    # 获取目标文件夹的路径
    filedir = 'C:/Users/Chen/Desktop/bulletAnalysis/Data/guichu'
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(filedir)
    # 打开当前目录下的result.txt文件，如果没有则创建
    f = open('C:/Users/Chen/Desktop/bulletAnalysis/Data/guichu/guichuAll.txt', 'w',encoding='utf-8')
    # 先遍历文件名
    for filename in filenames:
        print(filename)
        filepath = filedir + '/' + filename
        # 遍历单个文件，读取行数
        for line in open(filepath,encoding='utf-8'):
            f.writelines(line)
        f.write('\n')
    # 关闭文件
    f.close()
    
def getTxtByLineToList():
    file = open('../../Data/guichu/guichuAll.txt', encoding='utf-8')
    line = file.read().splitlines()
    file.close()
    return line

if __name__ == '__main__':
    print()