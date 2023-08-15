#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

ipchk = input("Please enter an IP address: ")

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)

else:
    print("You did not aply a valid IP address.")
