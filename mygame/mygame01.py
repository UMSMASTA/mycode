#!/usr/bin/python3
#Driving a simple game framework

import json

def showInstructions():
    #Show the game instructions when called
    print('''
    RPG Game
    ========
    Commands:
        go [direction]
        get [item]
    ========
    Goal: Find the key and magic potion
    ========
    ''')

def showStatus():
    #determines status of player
    #print current location
    print('------------------------------')
    print('You are in the ' + currentRoom)
    #print what the player is carrying
    print('Inventory:', ', '.join(inventory))
    #check is there is an item in the room
    if "item" in rooms[currentRoom]:
        print('You see a ' + ', '.join(rooms[currentRoom]['item']))
        print("----------------------------")


#empty inventory
inventory = []


#dictionary linking a room to other rooms
rooms_file = open('rooms.csv', 'r')

rooms = json.load(rooms_file)


#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#breaking this loop means game over
while True:
    showStatus()

    #The player Must type something otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    #normalizing input:
    #.lower() makes it lower case, .split() turns it into a list
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #if they arent allowed to go that way
        else:
            print('You can\'t go that way')

    #if they type get first
    if move[0] == 'get':
        #make 2 checks
        #1. if the room contains an item
        #2 if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add item to inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the dictionary
            rooms[currentRoom]['item'].remove(move[1])
            #if theres no item in the room
        else:
            print('Can\'t get ' + move[1] + '!')

    #If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you.....GAME OVER!')
        break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion....YOU WIN')
        break

