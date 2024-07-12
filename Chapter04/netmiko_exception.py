
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException, NetMikoTimeoutException

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.20',
    'username': 'admin',
    'password': 'Cisc0123',
    'secret': 'Cisc0123',
}

print("########## Connecting to Device {0} ############".format(device['ip']))
try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    print("***** show ip configuration of Device *****")
    output = net_connect.send_command("show ip int b")
    print(output)

    net_connect.disconnect()

except NetMikoTimeoutException:
    print("================ SOMETHING WRONG HAPPEN WITH {0} ==================".format(device['ip']))

except AuthenticationException:
    print("================ Authentication Failed with {0} ====================".format(device['ip']))

except Exception as unknown_error:
    print("================ SOMETHING UNKNOWN HAPPEN WITH {0} ================")
