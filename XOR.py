# coding: utf-8
import os
import subprocess

# 暗号化：引数の２つの文字列をXORした結果をhex文字列で返す
# src_text=暗号化したい文字列
# key=暗号化するためのキー文字列
def crypto_text_to_hex(src_text, key):
    if src_text and key:
        xor_code = key
        # keyが短い場合は、繰り返して必要バイト数を準備する
        while len(src_text) > len(xor_code):
            xor_code += key
        return "".join([chr(ord(data) ^ ord(code))
                        for (data, code) in zip(src_text, xor_code)]).encode().hex()

# 複号：引数のHex文字列とkeyをXORして戻した文字列で返す
# hex_text=暗号化されているhex文字列
# key=複号するためのキー文字列
def decrypto_hex_to_text(hex_text, key):
    if hex_text and key:
        try:
            crypt_data = bytes.fromhex(hex_text).decode()
        except ValueError:
            crypt_data = None

        if crypt_data:
            xor_code = key
            # keyが短い場合は、繰り返して必要バイト数を準備する
            while len(crypt_data) > len(xor_code):
                xor_code += key
            return "".join([chr(ord(data) ^ ord(code))
                            for (data, code) in zip(crypt_data, xor_code)])

# 固有key作成
def createKey():
    # Windowsの場合
    if os.name == "nt":
        cmd = "getmac /nh"
        return subprocess.check_output(cmd.split())
    # MacおよびLinux(多分)の場合
    else :
        cmd = "ifconfig en0"
        ifconfig = subprocess.check_output(cmd.split())
        list_Ifconfig = ifconfig.splitlines()
        # MACアドレスが表示される行を検索
        for i in range(10):
            list_Ifconfig[i] = str(list_Ifconfig[i],'utf-8')
            if "ether" in list_Ifconfig[i]:
            # 余計なものを排除
                return list_Ifconfig[i][7:30]
