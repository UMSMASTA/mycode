#!/usr/bin/env python3

def main():

    #dictionary list
    marvelchars = {"starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }



    
    #initial input print for character
    print("Which character do you want to know about?")
    charname = input("(Starlord, Mystique, Hulk): ").lower()
    
    

    #initial input print for stat
    print("Thank you! Which statistic fo you want to know about?")
    charstat = input("(Real name, Powers, Archenemy: ").lower()
    

    #prints selected stat, using title() to capitalize the value

    print(f"{charname.title()}'s {charstat} is:", marvelchars[charname][charstat].title() +".")

#while loop to repeat program until user types n
while True:
    main()
    if input("Would you like to ask again? Y/N: ").upper() == "N":
        break


