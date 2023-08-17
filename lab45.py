#!/usr/bin/env python3

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


yuck = ["carrots", "celery", "bananas", "apples", "oranges"]

#NE_animals = farms[0]["agriculture"]

#for animal in NE_animals:
    #print(animal)

user_input = input("Choose the farm you wish to know more about: ")

if user_input == 'NE':
    agriculture = farms[1]["agriculture"]
elif user_input == 'W':
    agriculture = farms[3]["agriculture"]
elif user_input == "E":
    agriculture = farms[2]["agriculture"]
elif user_input == "SW":
    agriculture = farms[0]["agriculture"]
else:
    print("You did not select a valid farm!")

for animal in agriculture:
    if animal not in yuck:
        print(animal)




