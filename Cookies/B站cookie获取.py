# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import os
import json
import pymysql
import requests
import json

driver = webdriver.Firefox()
# 获取cookie

db = pymysql.Connect(
    host='cdb-2m6kkrcx.gz.tencentcdb.com',  # 服务器地址
    port=10165,  # 服务器端口号
    user='root',  # 用户名
    passwd='972113786@qq.com',  # 密码
    db='bilibili_bullet',  # 数据库名
    charset='utf8'  # 编码式
)
cursor = db.cursor()
cursor.execute("SELECT * FROM cookies_table"
               "")
userdata = cursor.fetchall()
for item in userdata:

    username = item[1]
    passwd = item[2]

    driver.get("https://passport.bilibili.com/login")
    driver.implicitly_wait(30)  # 等待页面加载完毕
    #driver.find_element_by_css_selector(".remember-check").click()  # 取消记住我
    driver.find_element_by_id("login-username").clear()
    driver.find_element_by_id("login-username").send_keys(username)
    driver.find_element_by_id("login-passwd").clear()
    driver.find_element_by_id("login-passwd").send_keys(passwd)
    driver.find_element_by_link_text("登录").click()
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    old_cookie = ';'.join(item for item in cookie)  # 检测是否更新cookie
    dic_cookie = {}
    while True:  # 检测是否更新cookie
        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
        for cookie_item in driver.get_cookies():
            dic_cookie[cookie_item["name"]] = cookie_item["value"]
        new_cookie = ';'.join(cookie_item for cookie_item in cookie)  # 检测是否更新cookie
        if new_cookie != old_cookie:
            break
    # SQL 插入语句
    sql = "UPDATE cookies_table SET userCookies='%s' WHERE id=%s" % (json.dumps(dic_cookie), item[0])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    driver.delete_all_cookies()  # 清空cookie

db.close()
driver.close()
