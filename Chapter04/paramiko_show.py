#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import time

# 通過繼承 SSHClient() 來創建SSH客戶端
Channel = paramiko.SSHClient() 

# 設置 Paramiko 的參數，使其能夠自動添加任意未知的主機密鑰並信任與服務器之間的連接
Channel.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 將遠程主機的訊息(IP地址、用戶名和密碼等)傳遞給 connect() 函數
# Look_For_Keys: 默認True，強制Paramiko使用密鑰進行身分驗證(SSH public/private key)
# allow_agent: 默認True，表示是否允許連接到SSH代理
Channel.connect(hostname="10.10.88.112", username='admin', password='access123', look_for_keys=False, allow_agent=False)

# invoke_shell()將啟動一個連接到SSH 服務器的交互式shell會話
shell = Channel.invoke_shell()  # This will set interactive shell

# 使用 send() 函數發送命令
shell.send("enable\n")
shell.send("access123\n")
shell.send("terminal length 0\n")
shell.send("show ip int b\n")
shell.send("show arp \n")

# 如果遠程設備執行耗時很長的命令，如show tac，就要強制 Python 等待一段時間，直到設備
# 生成輸出並將結果返回給Python，否則 Python可能得不到正確的輸出結果
time.sleep(2)

print(shell.recv(5000)) # This will receive everything from the buffer, if you need to receive specifc output, the you should execute the command
                        # and immediately receive the output before executing the 2nd command, Also you should sleep a little
Channel.close()
