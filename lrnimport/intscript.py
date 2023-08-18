#!/usr/bin/env python3

import subprocess 

subprocess.call(["ip","link","show","up"])

print("This program will cehck your interfaces.")

interface = input("Enter an interface, like, ens3: ")

subprecoess.call((["ip", "addr", "show", "dev", interface]))

subprocess.call((["ip", "route", "show", "dev", interface]))

