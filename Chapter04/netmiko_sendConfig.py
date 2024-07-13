#!/usr/bin/env python
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler

SW2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.20',
    'username': 'admin',
    'password': 'Cisc0123',
    'secret': 'Cisc0123',
}

core_sw_config = ["int range e0/1 - 2", "switchport trunk encapsulation dot1q",
                  "switchport mode trunk", "switchport trunk allowed vlan 1,2"]

# .format(SW2['ip']))意思是先讀SW2這個字典，再來找到ip這個鍵的第0索引
print( "########## Connecting to Device {0} ############".format(SW2['ip']))
net_connect = ConnectHandler(**SW2)
net_connect.enable()

print( "***** Sending Configuration to Device *****")
net_connect.send_config_set(core_sw_config)

###################################################################################


# Send Configuration from file


# from netmiko import ConnectHandler

# connect_sw2 = ConnectHandler(**SW2)

# connect_sw2.enable()

# connect_sw2.send_config_from_file(config_file="./" + '192.168.10.20' + ".txt")
# connect_sw2.disconnect()
