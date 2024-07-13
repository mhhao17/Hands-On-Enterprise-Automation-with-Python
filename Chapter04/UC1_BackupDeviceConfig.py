#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ******* 功能說明 ********
# 此代碼對應到 book Page 68
# 使用文本文件定義設備資訊 (UC1_devices.txt)
# 配置備份設備清單使用.txt，設備相關資訊使用逗號分隔如 <device_ip>,<username>,<password>,<enable_password>,<vendor>
# 使用 with open 導入外部文件 "UC1_devices.txt"，在導入的文件對象上使用 readlines() 將文件中的每一行組成列表
# for 循環逐行讀取，以 split() 函數獲取設備資訊
# 根據設備 IP 地址格式化輸出文件名 (dev_10.10.88.110_.cfg)

from netmiko import ConnectHandler
from datetime import datetime

# 使用with open讀取文本文件並存成列表，產生的格式如下
#         [0]      [1]     [2]      [3]     [4]
# ['192.168.10.20,admin,Cisc0123,access123,cisco\n', 
# '192.168.10.21,admin,Cisc0123,access123,Cisco\n', 
# '192.168.10.22,admin,Cisc0123,access123,Cisco\n', 
# '10.10.88.113,admin,Cisc0123,access123,Cisco\n', 
# '10.10.88.114,admin,Cisc0s123,access123,Cisco']
# {ipaddr}{username}{password}{enable_password}{vendor}
with open(
        "./UC1_devices.txt") as devices_file:
    devices = devices_file.readlines() 

for line in devices:
    line = line.strip("\n") # 使用.strip("\n")將\n去掉
    ipaddr = line.split(",")[0] # 將用逗號分隔出來的第[0]索引附值給 ipaddr
    username = line.split(",")[1] # 將用逗號分隔出來的第[1]索引附值給 ipaddr
    password = line.split(",")[2] # 將用逗號分隔出來的第[2]索引附值給 ipaddr
    enable_password = line.split(",")[3] # 將用逗號分隔出來的第[3]索引附值給 ipaddr
    vendor = line.split(",")[4] # 將用逗號分隔出來的第[4]索引附值給 ipaddr

    # 使用if函數判斷 vendor 值，如果 vendor=cisco, 將字串 cisco_ios 賦值給 device_type 變數，將字串 "show running-config" 賦值給 backup_command 變數
    if vendor.lower() == "cisco": 
        device_type = "cisco_ios"
        backup_command = "show running-config"

    elif vendor.lower() == "juniper":
        device_type = "juniper"
        backup_command = "show configuration | display set"

    print(str(datetime.now()) + " Connecting to device {}".format(ipaddr))

    net_connect = ConnectHandler(device_type=device_type,
                                 ip=ipaddr,
                                 username=username,
                                 password=password,
                                 secret=enable_password)
    net_connect.enable()
    running_config = net_connect.send_command(backup_command)

    print(str(datetime.now()) + " Saving config from device {}".format(ipaddr))

    f = open("dev_" + ipaddr + "_.cfg", "w")
    f.write(running_config)
    f.close()
    print("==============================================")

# Result should be
# dev_10.10.88.110_.cfg
# dev_10.10.88.111_.cfg
# dev_10.10.88.112_.cfg
# dev_10.10.88.113_.cfg
# dev_10.10.88.114_.cfg