#!/usr/bin/env python3


def main():

    beer_count = int(input("How many bottles of beer would you like to count down?\n"))

    for countdown in reversed(range(beer_count)):

        if beer_count >= 100:
            print("That's too many brews guy! Slow down!")
            break

        print(countdown, "bottles of beer on the wall!")
        print(countdown, "bottles of beer!")
        print("You take one down, pass it around.")
        print(countdown, "bottles of beer on the wall!\n")
    




main()
        



