import random


#function to simulate two dice being rolled.
def user_diceroll():

    x = random.randint(1, 6)
    y = random.randint(1, 6)
   
    z=x+y
    return z

def enemy_diceroll():
    
    monster_x = random.randint(1, 6)
    return monster_x



def main():

    enemy_health = 0
    user_health = 20

    print("Choose your opponent difficulty!")

    user_input = input("Easy, Medium , Hard: ")

    if user_input == 'easy':
        enemy_health = 20
    
    elif user_input == 'medium':
        enemy_health = 40

    else:
        enemy_health = 60

    game_turn()

    continue_play()


def game_turn():

    while True:

        print("Make your choice: ")
        user_turn = input("1. Attack\n2.Block\n 3. Run Away\n")

        if user_turn == '1':
            user_diceroll()

            enemy_health = enemy_health - user_diceroll()
            print("You've attacked the creature for", user_diceroll(), "damage! The creature now has", enemy_health, 'hp.')
            
            enemy_diceroll()
            user_health = user_health - monster_x
            print("Now the enemy attacks...\n")
            print("the creature attacks for", monster_x, "damage! You now have", user_health, "HP.")
           
        elif user_turn == '2':

            print("You block the enemy's incoming attack!")
            enemy_diceroll()
            print("The monster attacked for", monster_x, "damage, but your block cancelled the attack!")


        else:
            print("You run away in cowardice! You lose!")
            break

        print('You:', user_health, "Enemy:", enemy_health)

        if enemy_health == 0 & user_health != 0:
            print("You have slain the beast! You win!")
            break

        elif enemy_health != 0 & user_health == 0:
            print("The monster has killed you. Better luck next time!")
            break

           
def continue_play():

    play_again = input.lower(("Would you like to play again? Y/N: "))

    if play_again == 'y':
        game_turn()
    else:
        print("GG!")


main()

    
