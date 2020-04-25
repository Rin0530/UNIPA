# UNIPA
UNIPA代替GUIアプリ

下記のpip及びpythonは各自の環境に合わせてpip3やpython3などと読み替えて下さい

動作確認環境 MacOS X 10.14~,Windows10
Google Chrome 80.0.3987.149

必ず最初に  
"pip install selenium"  
"pip install chromedriver-binary==80.0.3987.106.0"  
を実行して下さい.(括弧内は自分の環境に合わせて下さい)

'python -c "import tkinter;print(tkinter.TkVersion)"'  
を実行して8.5以下だった場合は[このリンク先](https://qiita.com/person0/items/4a8d4bf490510e8f71ab)を参考に  
バージョンを8.6に上げておいて下さい

timeTable_Import.py,timeTable_Input.pyは初回もしくは時間割、パスワードが変更になったときに実行して下さい  
timeTable_Import.pyは第一引数にUNIPAのID、第二引数にパスワードを入れて実行して下さい  
↑2度目以降でID,パスワードが変更されていない場合は引数無しで実行できるように変更しました  
普通に使う場合はpy_GUI.pyを実行して下さい

Windows10対応しました(多分)

シラバスをスクリーンショットではなく新たなウインドウを作成してそこに表示するように変更しました

スクロールはスクロールバーをドラッグすることでのみできます

進級判定及び平均点は個人の環境によるところが多いので不具合がある場合があります