#!/usr/bin/env python3


import crayons


def devicereboot(rebootcmd):

    for ip in rebootcmd.keys():
        print(f"Connecting to...{crayons.green(ip)}. REBOOTING NOW!")


def commandpush(devicecmd):

    for ip in devicecmd.keys():
        print(f"Handshaking. .. ... connecting with {ip}")

        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')

    return None

def main():

    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":["interface eth1/1","shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher")
    print("\nData set found\n")

    commandpush(devicecmd)

    devicereboot(devicecmd)

main()