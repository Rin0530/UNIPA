import tkinter
import os
import csv
import XOR
from pathlib import Path


# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

# ウィンドウの名前を設定
root.title("timeTableInput")

# ウィンドウの大きさを設定
root.geometry("1200x600")

def Confirm_Pass():
    root = Path("./.pass")
    key = XOR.createKey()
    hex_src1 = XOR.crypto_text_to_hex(pass_Box1.get(),key)
    hex_src2 = XOR.crypto_text_to_hex(pass_Box2.get(),key)
    if root.is_file():
        os.remove(".pass")
    os.system("echo "+hex_src1+" >> .pass")
    os.system("echo "+hex_src2+" >> .pass")
    fin_Label["text"]="ID,パスワードを保存しました"

def Confirm_TimeTable():
    root = Path(".timeTable.csv")
    if root.is_file():
        os.remove(".timeTable.csv")
    tt = []
    tt.append(Mon_1.get())
    tt.append(Mon_2.get())
    tt.append(Mon_3.get())
    tt.append(Mon_4.get())
    tt.append(Mon_5.get())
    tt.append(Mon_6.get())
    tt.append(Tue_1.get())
    tt.append(Tue_2.get())
    tt.append(Tue_3.get())
    tt.append(Tue_4.get())
    tt.append(Tue_5.get())
    tt.append(Tue_6.get())
    tt.append(Wed_1.get())
    tt.append(Wed_2.get())
    tt.append(Wed_3.get())
    tt.append(Wed_4.get())
    tt.append(Wed_5.get())
    tt.append(Wed_6.get())
    tt.append(Thu_1.get())
    tt.append(Thu_2.get())
    tt.append(Thu_3.get())
    tt.append(Thu_4.get())
    tt.append(Thu_5.get())
    tt.append(Thu_6.get())
    tt.append(Fri_1.get())
    tt.append(Fri_2.get())
    tt.append(Fri_3.get())
    tt.append(Fri_4.get())
    tt.append(Fri_5.get())
    tt.append(Fri_6.get())
    tt.append(Sat_1.get())
    tt.append(Sat_2.get())
    tt.append(Sat_3.get())
    tt.append(Sat_4.get())
    tt.append(Sat_5.get())
    tt.append(Sat_6.get())
    with open("./.timeTable.csv","w",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(tt)
    fin_Label["text"]="時間割の書き込みを保存しました"



Frame1 = tkinter.Frame(root, height = 400, width = 400, relief='sunken',borderwidth=5)

Frame1.grid()

Frame2 = tkinter.Frame(root,relief='sunken',borderwidth=5)

Frame2.grid()

Frame3 = tkinter.Frame(root,relief='sunken',borderwidth=5)

Frame3.grid()

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
Mon_1 = tkinter.Entry(Frame1)
Mon_2 = tkinter.Entry(Frame1)
Mon_3 = tkinter.Entry(Frame1)
Mon_4 = tkinter.Entry(Frame1)
Mon_5 = tkinter.Entry(Frame1)
Mon_6 = tkinter.Entry(Frame1)

Mon_1.grid(row = 1,column = 0)
Mon_2.grid(row = 2,column = 0)
Mon_3.grid(row = 3,column = 0)
Mon_4.grid(row = 4,column = 0)
Mon_5.grid(row = 5,column = 0)
Mon_6.grid(row = 6,column = 0)

# 火曜日時間割
Tue_1 = tkinter.Entry(Frame1)
Tue_2 = tkinter.Entry(Frame1)
Tue_3 = tkinter.Entry(Frame1)
Tue_4 = tkinter.Entry(Frame1)
Tue_5 = tkinter.Entry(Frame1)
Tue_6 = tkinter.Entry(Frame1)

Tue_1.grid(row = 1,column = 1)
Tue_2.grid(row = 2,column = 1)
Tue_3.grid(row = 3,column = 1)
Tue_4.grid(row = 4,column = 1)
Tue_5.grid(row = 5,column = 1)
Tue_6.grid(row = 6,column = 1)

# 水曜日時間割
Wed_1 = tkinter.Entry(Frame1)
Wed_2 = tkinter.Entry(Frame1)
Wed_3 = tkinter.Entry(Frame1)
Wed_4 = tkinter.Entry(Frame1)
Wed_5 = tkinter.Entry(Frame1)
Wed_6 = tkinter.Entry(Frame1)

Wed_1.grid(row = 1,column = 2)
Wed_2.grid(row = 2,column = 2)
Wed_3.grid(row = 3,column = 2)
Wed_4.grid(row = 4,column = 2)
Wed_5.grid(row = 5,column = 2)
Wed_6.grid(row = 6,column = 2)

# 木曜日時間割
Thu_1 = tkinter.Entry(Frame1)
Thu_2 = tkinter.Entry(Frame1)
Thu_3 = tkinter.Entry(Frame1)
Thu_4 = tkinter.Entry(Frame1)
Thu_5 = tkinter.Entry(Frame1)
Thu_6 = tkinter.Entry(Frame1)

Thu_1.grid(row = 1,column = 3)
Thu_2.grid(row = 2,column = 3)
Thu_3.grid(row = 3,column = 3)
Thu_4.grid(row = 4,column = 3)
Thu_5.grid(row = 5,column = 3)
Thu_6.grid(row = 6,column = 3)

# 金曜日時間割
Fri_1 = tkinter.Entry(Frame1)
Fri_2 = tkinter.Entry(Frame1)
Fri_3 = tkinter.Entry(Frame1)
Fri_4 = tkinter.Entry(Frame1)
Fri_5 = tkinter.Entry(Frame1)
Fri_6 = tkinter.Entry(Frame1)

Fri_1.grid(row = 1,column = 4)
Fri_2.grid(row = 2,column = 4)
Fri_3.grid(row = 3,column = 4)
Fri_4.grid(row = 4,column = 4)
Fri_5.grid(row = 5,column = 4)
Fri_6.grid(row = 6,column = 4)

# 土曜日時間割
Sat_1 = tkinter.Entry(Frame1)
Sat_2 = tkinter.Entry(Frame1)
Sat_3 = tkinter.Entry(Frame1)
Sat_4 = tkinter.Entry(Frame1)
Sat_5 = tkinter.Entry(Frame1)
Sat_6 = tkinter.Entry(Frame1)

Sat_1.grid(row = 1,column = 5)
Sat_2.grid(row = 2,column = 5)
Sat_3.grid(row = 3,column = 5)
Sat_4.grid(row = 4,column = 5)
Sat_5.grid(row = 5,column = 5)
Sat_6.grid(row = 6,column = 5)

label = tkinter.Label(Frame2,text="UNIPAのIDとパスワードを入力してください")
label.grid(row = 0,column = 1)

dummy = tkinter.Label(Frame1)
dummy.grid(row=7)

pass_Box1 = tkinter.Entry(Frame2)

pass_Box1.grid(row = 0, column = 2)

pass_Box2 = tkinter.Entry(Frame2,show="*")

pass_Box2.grid(row = 0, column = 3)

Botan = tkinter.Button(Frame3,height = 2,width = 13,text="時間割書き込み",command=Confirm_TimeTable)
Botan.grid(row = 0,column = 0)

Button =tkinter.Button(Frame3,height = 2,width = 13,text="パスワード書き込み",command=Confirm_Pass)
Button.grid(row = 0,column = 1)

fin_Label = tkinter.Label(root)
fin_Label.grid()

root.mainloop()