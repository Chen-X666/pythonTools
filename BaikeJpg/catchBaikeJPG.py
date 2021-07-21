# -------------------------------------------------------------------------------
# Description:
# Reference:
# Name:   通过keyword获取百度百科图片
# Author: ChenX
# Date:   2021/6/10
# -------------------------------------------------------------------------------
# coding:utf-8
import requests
import pandas as pd
from lxml import etree

#传入数组数据
def catch_Jpg(name):
    # 爬取页面源码数据
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }   # UA伪装
    url = 'https://baike.baidu.com/item/'+name
    page_text = requests.get(url=url,headers = headers).text
    # 页面数据解析
    tree = etree.HTML(page_text)
    # 创建一个文件夹
    li = tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a/img')
    print(li[0].attrib['src'])
    f = requests.get(li[0].attrib['src'])
    # 下载文件
    with open("result/"+name+".jpg", "wb") as code:
        code.write(f.content)

if __name__ == "__main__":
    failure = success = 0
    df = pd.read_csv("subject.csv",encoding='utf-8')
    data=df['subject'].values
    print(data)
    for a in data:
        try:
            print(a)
            catch_Jpg(a)
        except Exception:
            print('failure')
            failure = failure + 1
            print(Exception)
        else:
            print("success")
            success = success + 1
    print('爬虫结束成功:%d'%(success) +"失败:%d"%(failure))
