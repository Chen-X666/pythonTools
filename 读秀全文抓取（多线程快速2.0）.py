from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
import threading
import os

#下载图片到本地
def draw_local(imgpath,imgurl,count):
    t=0
    while t<10: #尝试10次 5s
        content = requests.get(imgurl).content
        with open(os.path.join(imgpath,str(count)+'.png'), 'wb') as fw:
            fw.write(content)
        if get_FileSize(os.path.join(imgpath,str(count)+'.png')) > 4546:
            return
        time.sleep(0.5)
        t+=1
  
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    return round(fsize, 2)
  
options = webdriver.FirefoxOptions()

'''编辑你的chrome路径和chromedriver路径'''
#options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#chrome_driver_binary = r'B:\ChromeDownload\85.0.4103\chromedriver.exe'
'''编辑你的chrome路径和chromedriver路径'''

driver = webdriver.Firefox()
driver.delete_all_cookies()
threads=[] #初始化线程列表

#['孙中山','恽代英','广州起义','叶挺','聂荣臻','张太雷','叶剑英','辛亥革命','黄花岗起义','二次革命']
ind='二次革命'
driver.get("https://book.duxiu.com/search?Field=all&channel=search&sw=%s&ecode=utf-8&edtype=&searchtype=&view=0"%(ind))
driver.implicitly_wait(30)#等待页面加载完成
driver.find_element_by_xpath("//div[@id=\'noscroll\']/div[5]/div/div[2]/ul/li[2]/a").click()

#拿到前十本书的地址
books=[]
while len(books) < 10:
    for book in driver.find_elements_by_css_selector(".books"):
        bookname=book.find_element_by_tag_name("dt").text
        bookauthors=book.find_element_by_tag_name("dd").text.replace(' ','').replace(':','').replace('著','').replace('编','').replace('写','') 
        if '作者' not in bookauthors:
            bookauthors='未知作者'
        else:
            bookauthors=bookauthors.replace('作者','')
        books.append([bookname+bookauthors,book.find_element_by_link_text("包库全文").get_attribute('href')])
    if len(books) > 10:
        books=books[:10]
        break
    if len(books) == 10:
        break
    driver.find_element_by_link_text("下一页").click()

page_list=[]
title_list=[]
#遍历十本书的内容
for book in books:
    js = 'window.open("%s")'%(book[1])
    driver.execute_script(js)
    title_list.append(book[0])
    
    # 获取打开的多个窗口句柄
    windows = driver.window_handles
    # 切换到当前最新打开的窗口
    driver.switch_to.window(windows[-1])
    page_list.append(driver.find_elements_by_css_selector(".readerPager"))
    
windows = driver.window_handles
driver.switch_to.window(windows[0])
driver.close()#关掉最开始的页面

# 获取打开的多个窗口句柄
windows = driver.window_handles
count=0
for w in windows:
    driver.switch_to.window(w)
    title=title_list[count]
    print('请查看是否需要跳过：y/n')
    while True:
        c=input()
        if c == 'y':
            break
        elif c == 'n':
            break
        else:
            print('无效命令！')
    if c == 'y':
        count+=1
        driver.close()
        continue
        
    print('开始下载：',title)
        
    imgpath=d=os.path.join(os.path.dirname(__file__),"书籍\%s"%(title))
    if not os.path.exists(imgpath):#判断存放图片的文件夹是否存在
        os.makedirs(imgpath)
    
    page_count=1
    for target in page_list[count]:
        driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
        while True:
            imgurl=target.find_element_by_tag_name('input').get_attribute('src')
            if 'http://img.sslibrary.com/n/' in imgurl:
                break
            else:
                time.sleep(0.1)
        t = threading.Thread(target=draw_local, args=(imgpath,imgurl,page_count))
        threads.append(t)
        t.start()
        if len(threads) > 3:
            for t in threads:
                t.join()
            threads=[]
        page_count+=1
        if page_count % 10 == 0:
            driver.delete_all_cookies()
    count+=1
    driver.delete_all_cookies()
    driver.close()
    
        

        
            
    


    
