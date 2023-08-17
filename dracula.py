#!/usr/bin/env python3

vampire = 0
with open('dracula.txt', "r") as foo:
    with open("vampire.txt", "w") as fang:
   
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                vampire += 1
                print("The word vampire is found", vampire, "times.")
                fang.write(line)
    