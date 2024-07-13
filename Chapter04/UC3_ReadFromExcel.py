#!/usr/bin/env python
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException
from pprint import pprint
import openpyxl

def load_devices_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    devices = {}
    
    for index, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if index == 1:
            continue
        
        hostname = row[0]
        ipaddr = row[1]
        username = row[2]
        password = row[3]
        enable_password = row[4]
        vendor = row[5]

        devices[hostname] = {
            'device_type': vendor,
            'ip': ipaddr,
            'username': username,
            'password': password,
            'secret': enable_password
        }
    
    return devices

def connect_and_run_command(device):
    print(f"########## Connecting to Device {device['ip']} ############")
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        print("***** show ip configuration of Device *****")
        output = net_connect.send_command("show ip int brief")
        print(output)

        net_connect.disconnect()

    except NetMikoTimeoutException:
        print(f"======= TIMEOUT OCCURRED WITH {device['ip']} =======")

    except NetMikoAuthenticationException:
        print(f"======= AUTHENTICATION FAILED WITH {device['ip']} =======")

    except Exception as unknown_error:
        print(f"======= UNKNOWN ERROR OCCURRED WITH {device['ip']} =======")
        print(unknown_error)

if __name__ == "__main__":
    devices = load_devices_from_excel(r"./UC3_devices.xlsx")
    pprint(devices)
    
    for hostname, device in devices.items():
        connect_and_run_command(device)
