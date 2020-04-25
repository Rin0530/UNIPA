# coding: utf-8
# Seleniumモジュール&etcのインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import os
import XOR
import sys
import chromedriver_binary

key = XOR.createKey()
login = 0

# パスワード復号

try:
    fp = open("config","r")
    temp = fp.readlines() 
    fp.close()
except Exception:
    print("パスワードが設定されていません")
    sys.exit(1)
dec_src1 = temp[0].rstrip()
dec_src2 = temp[1].rstrip()
dec_src1 = XOR.decrypto_hex_to_text(dec_src1,key)
dec_src2 = XOR.decrypto_hex_to_text(dec_src2,key)


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

DownloadPass = './Downloads'
####################
#これがないとダウンロードできない
driver.command_executor._commands["send_command"] = (
    "POST",
    '/session/$sessionId/chromium/send_command'
)
params = {
    'cmd': 'Page.setDownloadBehavior',
    'params': {
        'behavior': 'allow',
        #ここでダウンロード先ディレクトリ指定
        'downloadPath': DownloadPass
    }
}
driver.execute("send_command", params=params)
####################
# Seleniumセッティングここまで

####################
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
    element = driver.find_element_by_id("form1:linkPortal")
except Exception:
    print("IDもしくはパスワードが間違っています")
    driver.close()
    sys.exit(1)
# ログイン処理終了
####################

#def Start(Nth,WoD,NoW):
def Start(subName,week):
    if week == 0:
        WoD = "Monday"
    elif week == 1:
        WoD = "Tuesday"
    elif week == 2:
        WoD ="Wednesday"
    elif week == 3:
        WoD = "Thursday"
    elif week == 4:
        WoD = "Friday"
    elif week == 5:
        WoD = "Satuerday"
    
    #授業資料の最新のファイルをダウンロード
    element = driver.find_element_by_id("form1:linkClassProfile").click()
    # 指定した授業が非表示の場合
    # 曜日の欄をクリックして表示
    try:
        element = driver.find_element_by_partial_link_text(subName)
        element.click()
    except Exception:
        element = driver.find_element_by_id(WoD)
        element.click()
        try:
            element = driver.find_element_by_partial_link_text(subName).click()
        except Exception:
            return 2
    
    try:
        element = driver.find_element_by_id("form1:Jgc900:htmlFuncList:0:button3")
        element.click()
        element = driver.find_element_by_id(
            "form1:Jgc00301A:htmlJugyoShiryoTable:0:htmlTitle")
        element.click()
        element = driver.find_element_by_id(
            "form1:Jgc00301A:htmlJugyoShiryoTable:0:htmlFileList:0:_id15")
        element.click()
        element = driver.find_element_by_id(
            "form1:Jgc00301A:htmlJugyoShiryoTable:0:htmlTitle")
        element.click()
        print("Downloaded")
        return 0
    except Exception:
        print("この講義に授業資料はありません")
        return 1

def syllabus(subName):
    element = driver.find_element_by_id("menuc2").click()
    element = driver.find_element_by_id("menuimg2-1").click()
    element = driver.find_element_by_partial_link_text(subName).click()

    handle_array = driver.window_handles
    # seleniumで操作可能なdriverを切り替える
    try:
        driver.switch_to.window(handle_array[1])
    except Exception:
        syllabus(subName)
    
    
    ##########################################
    """ウインドウを新たに作る場合
    syllabusList = []
    # 科目名をリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[2]/td")
    syllabusList.append("科目名 "+element.text)
    # 単位数をリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[5]/td[2]")
    syllabusList.append("単位数 "+element.text)
    # 科目区分をリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[8]/td")
    syllabusList.append("科目区分 " +element.text)
    # 必修選択の別をリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[9]/td")
    syllabusList.append("必修選択の別 "+element.text)
    # 成績評価方法および基準をリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[18]/td")
    syllabusList.append("成績評価方法および基準 "+element.text)
    # オフィスアワーをリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[25]/td")
    syllabusList.append("オフィスアワー "+element.text)

    # 授業計画をリストに追加
    element = driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[26]/td")
    syllabusList.append("授業計画 "+element.text)

    # 元のウインドウに戻る
    driver.close()
    driver.switch_to.window(handle_array[0])
    element = driver.find_element_by_xpath(
        "//div[@id='account']/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a/img").click()

    return syllabusList"""
    ##########################################

    ##########################################
    #スクショをとる場合 
    # ウインドウサイズ取得&変更
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    os.system("sleep 3")
    # スクショ取得
    driver.save_screenshot('./Downloads/syllabus.png')
    driver.close()
    
    # 元のウインドウに戻る
    driver.switch_to.window(handle_array[0])
    element = driver.find_element_by_xpath(
        "//div[@id='account']/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a/img").click()
    ##########################################


def promotion():
    grade = []
    min_IsOK = []
    min_Limit = 0
    count = 0
    total = 0
    try:
        # 成績照会ページに移動
        element = driver.find_element_by_id("menu3").click()
        element = driver.find_element_by_partial_link_text("成績照会").click()
        Grade = driver.find_element_by_id("form1:htmlGakunen").text
        XPathNum = int(Grade[0])
        # 共通教養取得数
        element = driver.find_element_by_xpath("//td[2]/table/tbody/tr[5]/td")
        grade.append(float(element.text))
        min_IsOK.append(float(element.text) > 13)
        # 外国語取得数
        element = driver.find_element_by_xpath("//tr[5]/td[6]")
        grade.append(float(element.text))
        min_IsOK.append(float(element.text) > 12)
        # 第二外国語取得数
        element = driver.find_element_by_xpath("//tr[5]/td[12]")
        min_IsOK.append(float(element.text) > 2)
        # 専門、基礎科目取得数
        element = driver.find_element_by_xpath("//tr["+ str(11+XPathNum*9) +"]/td[2]/table/tbody/tr[5]/td[2]")
        grade.append(float(element.text))
        min_IsOK.append(float(element.text) > 9)
        # 専門、専門科目取得数数
        element = driver.find_element_by_xpath("//tr["+ str(11+XPathNum*9) +"]/td[2]/table/tbody/tr[7]/td[7]")
        grade.append(float(element.text))
        hoge = float(element.text)
        # 他コ開講
        element = driver.find_element_by_xpath("//tr["+ str(13+XPathNum*9) +"]/td[2]/table/tbody/tr[5]/td[2]")
        grade.append(float(element.text))
        hogehoge = float(element.text)

        element = driver.find_element_by_xpath("//div[@id='account']/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a/img").click()
    except Exception:
        return 2
    if hogehoge > 12:
        hogehoge = 12
    min_IsOK.append(hoge+hogehoge >67)

    # 学年毎に処理を分岐
    if Grade == "3年":          # 3年の進級判定基準
        for score in min_IsOK:
            if score == False:
                # 進級不可
                return 1
    if Grade == "1年":          # 1年の進級判定基準
        min_Limit = 24
        count = 3
    elif Grade == "2年":        # 2年の進級判定基準
        min_Limit = 58
        count = 4

    # 進級判定
    for score in grade:
        total += score  
        if total > min_Limit:
            # 進級可
            return 0
        # 進級不可
        return 1

def average(GradeNum):
    grades = 0
    count = 0
    # 成績照会ページに移動
    element = driver.find_element_by_id("menu3").click()
    element = driver.find_element_by_partial_link_text("成績照会").click()
    Grade = driver.find_element_by_id("form1:htmlGakunen").text

    if(GradeNum == 1):
        try:
            element = driver.find_element_by_xpath("//tr[29]/td[4]")
            grades = grades + int(element.text)
            count = count+1
            element = driver.find_element_by_xpath("//tr[30]/td[4]")
            grades = grades + int(element.text)
            count = count+1
        except Exception:
            pass

    # 前期の成績を集計
    for i in range():
        try:
            element = driver.find_element_by_css_selector("tr:nth-child("+str(GradeNum+12)+") tr:nth-child("+ str(i)+ ") > .tdHyokaList")
            if(element.text == "不受"):
                continue
            element = driver.find_element_by_css_selector("tr:nth-child("+str(GradeNum+12)+") tr:nth-child("+ str(i)+ ") > .tdSotenList")
        except Exception:
            continue
        if(element.text == ''):
            continue
        grades = grades + int(element.text)
        count = count+1

    # 後期のお成績を集計
    for i in range(28):
        try:
            element = driver.find_element_by_css_selector("tr:nth-child("+ str(GradeNum+14) +") tr:nth-child("+ str(i)+ ") > .tdHyokaList")
            if(element.text == "不受"):
                continue
            element = driver.find_element_by_css_selector("tr:nth-child("+ str(GradeNum+14) +") tr:nth-child("+ str(i)+ ") > .tdSotenList")
        except Exception:
            continue
        if(element.text == ''):
            continue
        grades = grades + int(element.text)
        count = count+1
    return grades / float(count)
    


def Quit():
    ##############
    #ログアウト処理
    element = driver.find_element_by_xpath(
        "//div[@id='account']/table/tbody/tr[2]/td/table/tbody/tr/td[5]/a/img")
    element.click()
    print("logout")
    ##############
    #ドライバーを閉じる
    driver.quit()
    return
    
