#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4.1.3 page 55

from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.20',
    'username': 'admin',
    'password': 'Cisc0123',
    'secret': 'Cisc0123',
}

connection = ConnectHandler(**R1)

connection.enable()
output = connection.send_command("show ip int b")
print("######################## ↓↓↓ Print show ip int brief ↓↓↓ #######################")
print(output)


###############Show the prompt and command#######################
# ↓

from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.20',
    'username': 'admin',
    'password': 'Cisc0123',
    'secret': 'Cisc0123',
}

connection = ConnectHandler(**R1)

connection.enable()

# strip_command會移除發送的指令 "show ip int b"
# strip_prompt會移除提示符 "lax-edg-r1#"
output = connection.send_command("show ip int b", strip_command=False, strip_prompt=False) 
print("###################### ↓↓↓ Show the prompt and command ↓↓↓ #####################")
print(output)

# print("########## Send Config From File ############")
# connection.send_config_from_file(config_file="/root/"+sw_ip+".txt")


###################################################################################

# CDP Neighbors


from netmiko import ConnectHandler
import time

SW3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.20',
    'username': 'admin',
    'password': 'Cisc0123',
    'secret': 'Cisc0123',
}

connect_sw3 = ConnectHandler(**SW3)

connect_sw3.enable()

# prepend the command prompt to the result (used to identify the local host)
result = connect_sw3.find_prompt() + "\n"

# execute the show cdp neighbor detail command
# we increase the delay_factor for this command, because it take some time if many devices are seen by CDP
result += connect_sw3.send_command("show cdp neighbor detail", delay_factor=2)
print("###################### ↓↓↓ Print CDP Neighbors Detial ↓↓↓ #####################")
print(result)

# close SSH connection
connect_sw3.disconnect()

###################################################################################

# print("########## Sending Configuration to Router ############")
R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.20',
    'username': 'admin',
    'password': 'Cisc0123',
    'secret': 'Cisc0123',
}

connect_R1 = ConnectHandler(**R1)

connect_R1.enable()



router_config = ["int lo0",  # list could be generated from file!
                 "ip add 4.4.4.4 255.255.255.0",
                 "int lo1",
                 "ip add 5.5.5.5 255.255.255.255"]

output = connect_R1.send_config_set(router_config)  # Netmiko will send "conf t"

print(output)
# connect_sw2.exit_config_mode()
