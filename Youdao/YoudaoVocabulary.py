# _*_ coding: utf-8 _*_
"""
Time:     2021/7/21 16:51
Author:   ChenXin
Version:  V 0.1
File:     YoudaoVocabulary.py
Describe:  Github link: https://github.com/Chen-X666
"""
def createVocabularyByTranslation(fileName):
    '''
        通过有道的逐句对照生成单词本
    '''
    file = open(fileName+'.txt', 'r', encoding='utf-8')  # 要读取的txt文件reading.txt
    lines = file.readlines()
    xml_file = open((fileName+'.xml'), 'w',encoding='utf-8')  # 生成的xml文件
    xml_file.write('<wordbook>')
    for line in range(len(lines) - 1):
        if line % 2 == 0:
            xml_file.write('<item>')
            xml_file.write('    <word>' + lines[line].strip('\n') + '</word>\n')
            line += 1
            xml_file.write('    <trans>' + '<![CDATA[' + lines[line].strip('\n') + ']]>' + '</trans>\n')
            xml_file.write('    <tags>reading</tags>\n')  # reading是你单词本的名字，你可以改成自己的
            xml_file.write('    <progress>1</progress>\n')
            xml_file.write('</item>')
    xml_file.write('</wordbook>')

if __name__ == '__main__':
    createVocabularyByTranslation(fileName='test')


