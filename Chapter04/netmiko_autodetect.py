#!/usr/bin/env python
# -*- coding: utf-8 -*-


from netmiko import SSHDetect, Netmiko

device = {
    'device_type': 'autodetect',
    'host': '192.168.10.20',
    'username': 'admin',
    'password': "Cisc0123",
}

detect_device = SSHDetect(**device)
device_type = detect_device.autodetect()
print(device_type)
print(detect_device.potential_matches)

device['device_type'] = device_type
connection = Netmiko(**device)
