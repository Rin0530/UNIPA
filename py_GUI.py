# coding: utf-8
# Seleniumのインポート
import Selenium_Setting as ss
# Tkinterモジュールのインポート
import tkinter as tk
import tkinter.messagebox
# その他etcのインポート
import csv
import sys
import atexit
import os

i = 0
j = 0
count=0
subName = ""
week = 0
img = None


# 曜日と科目名をセット
def clicked(kurasu,youbi):
    global subName 
    global week
    subName = kurasu
    week = youbi
    class_name["text"]=kurasu

# 最新授業資料ダウンロード
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

    # シラバスをスクショしてウインドウに表示
    ss.syllabus(subName)
    CreateNewWindow()

def promotion():
    can_promotion = ss.promotion()
    if can_promotion == 0:
        label["text"]="進級できます"
    elif can_promotion == 1 :
        label["text"]="進級できません"
    elif can_promotion == 2:
        label["text"]=("成績の取得に失敗しました\n不具合報告して下さい")

def CreateNewWindow():  
    newWindow = tk.Toplevel(root)
    #newWindow.geometry("800x1200")
    newWindow.minsize(800,400)

    # 画像を表示するための準備
    global img
    img = tk.PhotoImage(file='Downloads/syllabus.png')
    canvas = tk.Canvas(newWindow,width=img.width(),height=img.height(),bg="white")
    canvas.create_image(0,0,image=img,anchor=tkinter.NW)

    scrollbar_y = tk.Scrollbar(newWindow,orient=tk.VERTICAL,command=canvas.yview)
    frame = tk.Frame(canvas)

    # スクロールバー設定
    #canvas.create_window((0,0), window=frame, anchor=tk.NW, image=canvas.photo)
    canvas["yscrollcommand"]=scrollbar_y.set
    #canvas.config(scrollregion=canvas.bbox("all"))
    canvas["scrollregion"]=(0,0,0,img.height())
    canvas.update_idletasks()

    canvas.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
    scrollbar_y.pack(fill=tk.Y, side=tk.RIGHT)

def Error_Null():
    tk.messagebox.showinfo("Error","科目名を選択してください")

def Quit():
    ss.Quit()
    sys.exit(0)
    os.remove("./Downloads/syllabus.png")


# ウィンドウ立ち上げ
#--------------------------------

# ウィンドウ（フレーム）の作成
root = tk.Tk()

# ウィンドウの名前を設定
root.title("UNIPA_Instance")

# ウィンドウの大きさを設定
root.geometry("1600x1200")




Frame1 = tk.Frame(root, height = 400, width = 400, relief='sunken',borderwidth=5)

Frame1.grid()

Frame2 = tk.Frame(root, relief='sunken',borderwidth=5)

Frame2.grid()

###################################
# 各曜日を示すラベル表示
label_Mon = tk.Label(Frame1,text="月曜日",)
label_Mon.grid(row = 0,column = 0)

label_Tue = tk.Label(Frame1,text="火曜日")
label_Tue.grid(row = 0,column = 1)

label_Wed = tk.Label(Frame1,text="水曜日")
label_Wed.grid(row = 0,column = 2)

label_Thu = tk.Label(Frame1,text="木曜日")
label_Thu.grid(row = 0,column = 3)

label_Fri = tk.Label(Frame1,text="金曜日")
label_Fri.grid(row = 0,column = 4)

label_Sta = tk.Label(Frame1,text="土曜日")
label_Sta.grid(row = 0,column = 5)
#####################################

# 月曜日時間割    
Mon_1 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_1["text"],0))
Mon_2 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_2["text"],0))
Mon_3 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_3["text"],0))
Mon_4 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_4["text"],0))
Mon_5 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_5["text"],0))
Mon_6 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Mon_6["text"],0))

# 火曜日時間割
Tue_1 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_1["text"],1))
Tue_2 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_2["text"],1))
Tue_3 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_3["text"],1))
Tue_4 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_4["text"],1))
Tue_5 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_5["text"],1))
Tue_6 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Tue_6["text"],1))

# 水曜日時間割
Wed_1 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_1["text"],2))
Wed_2 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_2["text"],2))
Wed_3 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_3["text"],2))
Wed_4 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_4["text"],2))
Wed_5 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_5["text"],2))
Wed_6 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Wed_6["text"],2))

# 木曜日時間割
Thu_1 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_1["text"],3))
Thu_2 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_2["text"],3))
Thu_3 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_3["text"],3))
Thu_4 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_4["text"],3))
Thu_5 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_5["text"],3))
Thu_6 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Thu_6["text"],3))

# 金曜日時間割
Fri_1 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_1["text"],4))
Fri_2 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_2["text"],4))
Fri_3 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_3["text"],4))
Fri_4 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_4["text"],4))
Fri_5 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_5["text"],4))
Fri_6 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Fri_6,4))

# 土曜日時間割
Sat_1 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_1["text"],5))
Sat_2 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_2["text"],5))
Sat_3 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_3["text"],5))
Sat_4 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_4["text"],5))
Sat_5 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_5["text"],5))
Sat_6 = tk.Button(Frame1,height = 5,width = 20,command=lambda:clicked(Sat_6["text"],5))


timetable = [
    Mon_1,Mon_2,Mon_3,Mon_4,Mon_5,Mon_6,
    Tue_1,Tue_2,Tue_3,Tue_4,Tue_5,Tue_6,
    Wed_1,Wed_2,Wed_3,Wed_4,Wed_5,Wed_6,
    Thu_1,Thu_2,Thu_3,Thu_4,Thu_5,Thu_6,
    Fri_1,Fri_2,Fri_3,Fri_4,Fri_5,Fri_6,
    Sat_1,Sat_2,Sat_3,Sat_4,Sat_5,Sat_6
    ]

#data = pd.read_csv("timeTable.csv").values.tolist()
try:
    with open("timeTable.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f) # readerオブジェクトの作成
        for r in reader: # for文を用いて一行ずつ読み込む
            data = r
# timeTable.csvが見つからなかった時は全て空白で埋める
except Exception:
    data = [
        "","","","","","",
        "","","","","","",
        "","","","","","",
        "","","","","","",
        "","","","","","",
        "","","","","",""
        ]  

for button in timetable:
    button["text"]=data[count]
    button.grid(row = i+1,column = j)
    i = i+1
    count=count+1
    if i==6:
        i = 0
        j = j+1

class_name = tk.Label(Frame2,height = 2,width = 20)

class_name.grid(row=0,column=0)

jugyoSiryo = tk.Button(Frame2,text="授業資料",command=materials,height = 2,width = 20)

jugyoSiryo.grid(row=0,column=1)

shirabasu = tk.Button(Frame2, text="シラバス",command=syllabus,height = 2,width = 20)

shirabasu.grid(row=0,column=2)

shinkyu = tk.Button(Frame2, text="進級チェック",command=promotion,height = 2,width = 20)

shinkyu.grid(row=0,column=3)

# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
fin = tk.Button(root, text="終了", command=Quit)

# ボタンの表示
fin.grid(row=2,column=0)



#　ラベルの作製
label = tk.Label(root,height=2,width=40)
#if ss.login == 1:
#    label["text"] = "UNIPAのログインに失敗しました\nIDとパスワードの入力をやり直してください"

#　ラベルの表示
label.grid(row=3,column=0)


# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop()


# ウインドウを閉じるときにログアウト
atexit.register(Quit)