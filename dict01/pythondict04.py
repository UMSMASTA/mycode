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

    print("Fourth test - .keys()")
    print(switch.keys(),"\n")

    print("Fifth test - .values()")
    print(switch.values(),"\n")

    #remove a value from our dictionary using del
    del switch["vendor"]
    print(switch,"\n")

    #remove a value using pop
    print("Seventh test - .pop()")
    print(switch.pop("version"))
    print(switch.keys())
    print(switch.values(),"\n")

    #add another value to the dictoinary
    print("Ninth test - ADD a new value")
    switch["password"] = "qwerty"
    print(switch.keys())
    print(switch.values(),"\n")

    #select a value from the results
    #we must first convert value into list
    print(list(switch.values())[2])



#call our main function
main()