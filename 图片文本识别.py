# -*- coding: UTF-8 -*-
#from langconv import *
from aip import AipOcr
#from demo import *
import re
import time
import os
def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence
    
""" 网上找的账号"""
'''
APP_ID = '11352343'
API_KEY = 'Nd5Z1NkGoLDvHwBnD2bFLpCE'
SECRET_KEY = 'A9FsnnPj1Ys2Gof70SNgYo23hKOIK8Os'
'''

'''我的账号'''

APP_ID = '18903023'
API_KEY = 'fsByKaWqaNr8YZ6uToIZcprN'
SECRET_KEY = 'At92EOAVc3FWaNWMGCq8giZ9zXXiPasC'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_end_list(image):
    """ 如果有可选参数 """
    #options = {}
    #options["detect_direction"] = "true"

    """ 带参数调用通用文字识别（高精度版） """
    #result_list = client.basicAccurate(image)['words_result']
    
    """ 带参数调用通用文字识别 """
    time.sleep(0.1)
    result_list = client.basicGeneral(image)['words_result']
    endlist = []
    for result in result_list:
        endlist.append(result['words'])
    return endlist

from Text_Processing import *

if __name__ == '__main__':
    bookname='中国革命史略_10970057'
    imagePath = 'B:\长征\长征python\Picture\%s'%(bookname)
    fileList = os.listdir(imagePath)
    for n in range(0,len(fileList)):
        s=''
        filePath=os.path.join(imagePath,'images_%s.png'%(n))
        image = get_file_content(filePath)
        tick=0
        while tick < 3:#尝试三次，不行就跳过该图片
            try:
                result = get_end_list(image)
                tick=3
            except:
                tick+=1
                time.sleep(tick)
        for i in result:
            s+=pun_replace(textParse(i))
        with open(r'B:\长征\图书文本\%s.txt'%(bookname),'a') as f:
            f.write(s)
        print('images_%s.png 已写入！'%(n))