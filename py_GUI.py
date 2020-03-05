# Seleniumのインポート
import Selenium_Setting as ss
# Tkinterモジュールのインポート
import tkinter
import tkinter.messagebox
# その他etcのインポート
import os
import csv
import sys


i = 0
j = 0
count=0
subName = ""
week = 0


# 最新授業資料ダウンロード
def clicked(kurasu,youbi):
    global subName 
    global week
    subName = kurasu
    week = youbi
    class_name["text"]=kurasu

def materials():
    global subName 
    global week
    if subName == "":
        Error_Null()
        return

    label["text"]="Now processing..."
    #いわゆる移譲ってやつだね
    A = ss.Start(subName,week)
    if A == 1:
        label["text"]="この講義に授業資料はありません"
    elif A ==2:
        label["text"]=subName+"は見つかりませんでした\n科目名を見直してください"
    else :
        label["text"]="授業資料をダウンロードしました"

def syllabus():
    global subName
    if subName == "":
        Error_Null()
        return
    label["text"]="Now processing..."
    ss.syllabus(subName)
    label["text"]=""

def Quit():
    ss.Quit()
    #label["text"]="ログアウトしました アプリを終了してください"
    sys.exit(0)

def Error_Null():
    tkinter.messagebox.showinfo("Error","科目名を選択してください")

def succeed():
    label["text"]="授業資料をダウンロードしました"




# ウィンドウ立ち上げ
#--------------------------------

# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

# ウィンドウの名前を設定
root.title("UNIPA_Instance")

# ウィンドウの大きさを設定
root.geometry("1200x1200")




Frame1 = tkinter.Frame(root, height = 400, width = 400, relief='sunken',borderwidth=5)

Frame1.grid()

Frame2 = tkinter.Frame(root, relief='sunken',borderwidth=5)

Frame2.grid()

###################################
# 各曜日を示すラベル表示
label_Mon = tkinter.Label(Frame1,text="月曜日",)
label_Mon.grid(row = 0,column = 0)

label_Tue = tkinter.Label(Frame1,text="火曜日")
label_Tue.grid(row = 0,column = 1)

label_Wed = tkinter.Label(Frame1,text="水曜日")
label_Wed.grid(row = 0,column = 2)

label_Thu = tkinter.Label(Frame1,text="木曜日")
label_Thu.grid(row = 0,column = 3)

label_Fri = tkinter.Label(Frame1,text="金曜日")
label_Fri.grid(row = 0,column = 4)

label_Sta = tkinter.Label(Frame1,text="土曜日")
label_Sta.grid(row = 0,column = 5)
#####################################

# 月曜日時間割    
Mon_1 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_1["text"],0))
Mon_2 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_2["text"],0))
Mon_3 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_3["text"],0))
Mon_4 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_4["text"],0))
Mon_5 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_5["text"],0))
Mon_6 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_6["text"],0))

# 火曜日時間割
Tue_1 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_1["text"],1))
Tue_2 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_2["text"],1))
Tue_3 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_3["text"],1))
Tue_4 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_4["text"],1))
Tue_5 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_5["text"],1))
Tue_6 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_6["text"],1))

# 水曜日時間割
Wed_1 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_1["text"],2))
Wed_2 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_2["text"],2))
Wed_3 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_3["text"],2))
Wed_4 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_4["text"],2))
Wed_5 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_5["text"],2))
Wed_6 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_6["text"],2))

# 木曜日時間割
Thu_1 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_1["text"],3))
Thu_2 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_2["text"],3))
Thu_3 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_3["text"],3))
Thu_4 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_4["text"],3))
Thu_5 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_5["text"],3))
Thu_6 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_6["text"],3))

# 金曜日時間割
Fri_1 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_1["text"],4))
Fri_2 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_2["text"],4))
Fri_3 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_3["text"],4))
Fri_4 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_4["text"],4))
Fri_5 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_5["text"],4))
Fri_6 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_6,4))

# 土曜日時間割
Sat_1 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_1["text"],5))
Sat_2 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_2["text"],5))
Sat_3 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_3["text"],5))
Sat_4 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_4["text"],5))
Sat_5 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_5["text"],5))
Sat_6 = tkinter.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_6["text"],5))


timetable = [
    Mon_1,Mon_2,Mon_3,Mon_4,Mon_5,Mon_6,
    Tue_1,Tue_2,Tue_3,Tue_4,Tue_5,Tue_6,
    Wed_1,Wed_2,Wed_3,Wed_4,Wed_5,Wed_6,
    Thu_1,Thu_2,Thu_3,Thu_4,Thu_5,Thu_6,
    Fri_1,Fri_2,Fri_3,Fri_4,Fri_5,Fri_6,
    Sat_1,Sat_2,Sat_3,Sat_4,Sat_5,Sat_6
    ]

#data = pd.read_csv("timeTable.csv").values.tolist()

with open("timeTable.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f) # readerオブジェクトの作成
    for r in reader: # for文を用いて一行ずつ読み込む
        data = r


for button in timetable:
    button["text"]=data[count]
    #button["command"] = lambda:clicked(button["text"],j)
    button.grid(row = i+1,column = j)
    i = i+1
    count=count+1
    if i==6:
        i = 0
        j = j+1

class_name = tkinter.Label(Frame2,height = 2,width = 20)

class_name.grid(row=0,column=0)

jugyoSiryo = tkinter.Button(Frame2,text="授業資料",command=materials,height = 2,width = 20)

jugyoSiryo.grid(row=0,column=1)

shirabasu = tkinter.Button(Frame2, text="シラバス",command=syllabus,height = 2,width = 20)

shirabasu.grid(row=0,column=2)



# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
fin = tkinter.Button(root, text="終了", command=Quit)

# ボタンの表示
fin.grid(row=2,column=0)



#　ラベルの作製
label = tkinter.Label(root,height=2,width=40)
#if ss.login == 1:
#    label["text"] = "UNIPAのログインに失敗しました\nIDとパスワードの入力をやり直してください"

#　ラベルの表示
label.grid(row=3,column=0)


# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop()
