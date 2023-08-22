#!usr/bin/env python3
#US Open Switch Checker

'''This will ping the router, check the router, check interface uptime, apply new config'''

import os
import csv
import bootstrapper

from netmiko import ConnectHandler

def get_csv(fileloc):

    d = {}

    with open(fileloc, "r") as foo:
        for row in csv.DictReader(foo):
            #first value of row == hostname:sw1, driver: arista
            keypair = {row['hostname']: row['driver']}
            d.update(keypair)
    return d #return the completed dictionary

#ping router function
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #error check
    if response == 0:
        return True

    else:
        return False

#Check interface
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type,
                                        ip=dev_ip,
                                        username=dev_un,
                                        password=dev_pw)
        
        my_command = open_connection.send_command("show ip int brief")

    except:
        my_command = "** ISSUING COMMAND FAILED**"

    finally:
        #no matter what, this will return "my_command"
        return my_command

#Login to router - SSH Check with netmiko
def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type,
                                        ip=dev_ip,
                                        username=dev_un,
                                        password=dev_pw) 
        return True

    except:
        return False

def main():

    file_location = input("Host file location [Press ENTER for default: 'host_list.csv']\n") or "host_list.csv"

    entry = get_csv(file_location)

    print("\n**** BEGIN SSH CHECKING ****")
    for switchip in entry:
        if login_router(f"{entry[switchip]}",
                        switchip,
                        "admin",
                        "alta3"):
            
            print("\n\t**HOST: -" + switchip + " - SSH connectivity UP\n")
        else:
             print("\n\t**HOST: -" + switchip + " - SSH connectivity DOWN\n")

    
    print("\n**** BEGIN ICMP CHECKING ****")
    for switchip in entry:
        if ping_router(switchip):
          print("\n\t**HOST: -" + switchip + " - responding to ICMP\n")

        else:
            print("\n\t**HOST: -" + switchip + " - NOT responding to ICMP\n")

    print("\n**** BEGIN SHOW IP INT BRIEF ****")
    for switchip in entry:
        result = interface_check(f"{entry[switchip]}", switchip, "admin", "alta3")
        print("\n" + result)

    print("\n**** NEW BOOTSTRAPPING CHECK ****")

    ynchk = input("\n Would you like to apply a new configuration? y/N \n") or "n"

    if ynchk.lower() in ["y", "yes"]:
        conf_loc = input("\nEnter name of new config file. \n")
        conf_ip = input("\nHostname of the device to be configured? \n")

    if bootstrapper.bootstrapper(f"{entry[switchip]}", switchip, "admin", "alta3", conf_loc):
        print("\nNEW configuration applied!")

    else:
        print("\nProblem in applying new configuration!")

if __name__ == "__main__":
    main()
               
