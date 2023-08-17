#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:


## display file to the screen - .read()
    configblog = configfile.readlines()

## break configblog across line boundaries (strips out \n)


## display list with no "\n"
    print(configblog)

## Always close your file
configfile.close()
