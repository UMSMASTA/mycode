from datetime import datetime
from netmiko import ConnectHandler

#dictionary of connect info for cisco

#cisco3 = {
#           'device_type: 'cisco_ios',
#           'host': 'cisco3.example.com',
#           'username': 'admin',
#           'password': 'cisco123',
#           }

#cisco_asa = {
#           'device_type': 'cisco_asa',
#           'host': '10.10.10.88',
#           'username': 'admin',
#           'password': 'cisco123',
#           'secret': 'cisco123',
#             }

#cisco_xrv = {
#    'device_type': 'cisco_xr', 
#    'host': '10.10.10.77', 
#    'username': 'admin', 
#    'password': 'cisco123', 
#    }

arista1 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-1', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

arista2 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-2', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

#hp_procurve = { 
#    'device_type': 'hp_procurve', 
#    'host': '10.10.10.68', 
#    'username': 'admin', 
#    'password': '!cisco123', 
#    } 

#juniper_srx = { 
#    'device_type': 'juniper', 
#    'host':   'srx1.domain.com', 
#    'username': 'admin', 
#    'password': '!cisco123', 
#    }

#make a list containing all of the login info
#all_devices = [cisco3, cisco_asa, cisco_xrv, arista8, hp_procurve, juniper_srx]

all_devices = [arista1, arista2]

#when our script begins, get the start time
start_time = datetime.now()

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show arp")

    print(f"\n\n-------- Device {a_device['device_type']} ---------")
    print(output)
    print("---------- End ---------")

end_time = datetime.now()

total_time = end_time - start_time
print(f"Finished in {total_time} seconds")

