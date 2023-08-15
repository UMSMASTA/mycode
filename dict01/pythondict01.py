#!/usr/bin/env python3
#Understanding dictionaries
#{key: value, key:value, ...}

def main():

    #create a dict. with 4 k:v pairs
    switch = {"hostname": "sw1", "ip":"10.0.1.1", "version": "1.2", "vendor":"cisco"}

    #prove that switch is indeed a dictionary
    print(type(switch))

    #display parts of the dictionary
    print(switch["hostname"])
    
    print(switch["ip"])

    #request a fake key
    print(switch["lynx"])

#call our main function
main()