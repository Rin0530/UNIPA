from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import csv
import os


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

#driver = webdriver.Chrome("/Users/Shared/chromedriver", options=options)
driver = webdriver.Chrome("/Users/Shared/chromedriver")
# Selenium初期設定ここまで
############################



##############################
# ログイン処理
driver.get("https://unipa.itp.kindai.ac.jp/up/faces/login/Com00501A.jsp")
print("UNIPAopen")
element = driver.find_element_by_id("form1:htmlUserId")
element.send_keys("1910370050r")
element = driver.find_element_by_id("form1:htmlPassword")
element.send_keys("kjRyekXDRw5d")
element = driver.find_element_by_id("form1:login")
element.click()
print("login")
# ログイン処理ここまで
##############################




##############################
# 時間割取得
timeTable = []
i = 0
driver.get("https://unipa.itp.kindai.ac.jp/up/faces/up/km/Kma00203A.jsp#")
element = driver.find_element_by_class_name("selectOneMenu")
select_Display = Select(element)
select_Display.select_by_value("1")
element = driver.find_element_by_id("form1:search")
element.click()
os.system("sleep 1")
try:
    for i in range(20):
        element =  driver.find_element_by_id("form1:standardJugyoTimeSchedule00List:"+str(i)+":rowVal000002")
        timeTable.append(element.text)

except Exception as identifier:
    with open("./timeTable.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(timeTable)
        element = driver.find_element_by_xpath(
            "//div[@id='account']/table/tbody/tr[2]/td/table/tbody/tr/td[5]/a/img")
        element.click()