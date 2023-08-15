#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

ipchk = input("Please enter an IP address: ")

# a string tests as True

if ipchk == "192.168.70.1":
    print("IP cannot be the same as the default gateway.")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)

else:
    print("You did not aply a valid IP address.")
