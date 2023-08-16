#!/usr/bin/env python3

round = 0
answer = " "
while round <3 and answer != "Brian":

    round = round+1

    answer = input('Finish the movie title, "Monty Python\'s The Life of _ _ _ _ _"')
    answer = answer.capitalize()
    if answer == 'Brian':
        print('Correct')
        break
    elif round ==3:
        print("Sorry, the answer was Brian.")
        break
    elif answer == 'Shrubbery':
        print("You gave the super secret answer!")
        break
    else:
        print("Sorry! Try again!")