#!/usr/bin/env python3

round = 0

while round <3 and answer != "Brian":

    round = round+1

    answer = input('Finish the movie title, "Monty Python\'s The Life of _ _ _ _ _"')

    if answer == 'Brian':
        print('Correct')
        break
    elif round ==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")