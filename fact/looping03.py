#!/usr/bin/env python3
import time
import uuid


howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDS...")

time.sleep(3)

for rando in range(howmany):
    print(uuid.uuid4() )

