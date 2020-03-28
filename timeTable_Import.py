# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import csv
import os
import sys
from pathlib import Path
import XOR

args = sys.argv
key = XOR.createKey()

if len(args) == 3:
    ##############################
    # timeTable.csvをリセット
    root = Path("./timeTable.csv")
    if root.is_file():
        os.remove("./timeTable.csv")
    ##############################

    ##############################
    # ID,パスワードをセット
    root = Path("./config")
    hex_src1 = XOR.crypto_text_to_hex(args[1],key)
    hex_src2 = XOR.crypto_text_to_hex(args[2],key)
    if root.is_file():
        os.remove("./config")
    os.system("echo "+hex_src1+" >> config")
    os.system("echo "+hex_src2+" >> config")
    ##############################
elif len(args) != 1:
    print("引数は2つ入力してください")
    print("第一引数はID,第二引数はパスワードです")
    sys.exit(0)



##############################
# Selenium初期設定
options = Options()
options.add_argument('--headless')
"""
#非ヘッドレスモードのダウンロードディレクトリを指定
options = webdriver.ChromeOptions()
prefs = {"download.default_directory":"./"}
options.add_experimental_option("prefs",prefs)
"""

#geckodriver_path = "/Users/Shared/geckodriver"
#ChromeDriverのパスを引数に指定しChromeを起動

driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
# Selenium初期設定ここまで
############################


############################
# パスワード復号
try:
    fp = open("config","r")
    temp = fp.readlines() 
    fp.close()
except Exception:
    print("パスワードが設定されていません")
    sys.exit(0)
dec_src1 = temp[0].rstrip()
dec_src2 = temp[1].rstrip()
dec_src1 = XOR.decrypto_hex_to_text(dec_src1,key)
dec_src2 = XOR.decrypto_hex_to_text(dec_src2,key)
############################

##############################
# ログイン処理
driver.get("https://unipa.itp.kindai.ac.jp/up/faces/login/Com00501A.jsp")
print("UNIPAopen")
element = driver.find_element_by_id("form1:htmlUserId")
element.send_keys(dec_src1)
element = driver.find_element_by_id("form1:htmlPassword")
element.send_keys(dec_src2)
element = driver.find_element_by_id("form1:login")
element.click()
print("login")
try:
    element = driver.find_element_by_id("form1:linkPortal").click()
except Exception:
    print("ID,またはパスワードが間違っています")
    sys.exit(0)
# ログイン処理ここまで
##############################




##############################
# 時間割取得

timeTable = []
element = driver.find_element_by_id("menuc2").click()
element = driver.find_element_by_id("menuimg2-1").click()

for i in range(6):
    for j in range(6):
        element = driver.find_element_by_id("form1:calendarList:"+str(i)+":rowVal0"+str(j+1))
        class_name = element.text
        index = class_name.find("【")
        class_name = class_name[:index]
        timeTable.append(class_name.strip())

with open("./timeTable.csv","w",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(timeTable)

 ##############
#ログアウト処理
element = driver.find_element_by_xpath(
        "//div[@id='account']/table/tbody/tr[2]/td/table/tbody/tr/td[5]/a/img")
element.click()
print("logout")
##############
#ドライバーを閉じる
driver.quit()