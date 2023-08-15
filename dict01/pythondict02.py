#!/usr/bin/env python3
#Understanding dictionaries
#{key: value, key:value, ...}

def main():

    #create a dict. with 4 k:v pairs
    switch = {"hostname": "sw1", "ip":"10.0.1.1", "version": "1.2", "vendor":"cisco"}

    #prove that switch is indeed a dictionary
    print(type(switch))

    #display parts of the dictionary
    print(switch["hostname"],"\n")
    
    print(switch["ip"],"\n")

    #request a fake key
    #print(switch["lynx"])

    #request a fake key with .get()

    print("First test = .get()")
    print(switch.get("lynx"),"\n")

    print("Second test - .get()")
    print(switch.get("lynx", "Not a valid key\n"))

    print("Third test - .get()")
    print(switch.get("version"))

#call our main function
main()