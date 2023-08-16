
#import random module to roll random dice
import random


#function to simulate two dice being rolled for both user and enemy.
def user_diceroll():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
   
    z=x+y
    return z

def enemy_diceroll():
    
    monster_x = random.randint(1, 6)
    return monster_x


#main game function
def main():
#defining health
    enemy_health = 0
    user_health = 20
#defining attack that is calling from the diceroll runctions made earlier
    user_attack = user_diceroll()
    enemy_attack = enemy_diceroll()

#Input to choose difficulty
    print("Choose your opponent difficulty!")

    user_input = input("Easy, Medium , Hard: ")

    if user_input == 'Easy':
        enemy_health = 20
    
    elif user_input == 'Medium':
        enemy_health = 40

    else:
        enemy_health = 60

#while loop for the main game function
    while True:

#input for user decision
        print("Make your choice: ")
        user_turn = input("1. Attack\n2.Block\n 3. Run Away\n")

#if User chooses to attack, then the enemy health is subtracted by the user attack, prints details
        if user_turn == '1':
            
            enemy_health = enemy_health - user_attack
            print("You've attacked the creature for", user_attack, "damage! The creature now has", enemy_health, 'hp.')
            
            #enemy attack showing the same thing, and overall list
            user_health = user_health - enemy_attack
            print("Now the enemy attacks...\n")
            print("the creature attacks for", enemy_attack, "damage! You now have", user_health, "HP.")
 #if user chooses to block, it cancels the attack, however it does show what the enemy rolls.            
        elif user_turn == '2':

            print("You block the enemy's incoming attack!")
            print("The monster attacked for", enemy_attack, "damage, but your block cancelled the attack!")

#else statement to give up, also breaks the loop
        else:
            print("You run away in cowardice! You lose!")
            break
#Overall HP between rounds
        print('You:', user_health, "Enemy:", enemy_health)
        
#if-else statement on victory conditions

#if enemy health is depleted, and user has health, you win
        if enemy_health <= 0 and user_health >= 0:
            print("You have slain the beast! You win!")
            break
#if enemy has health, and you don't you lose
        elif enemy_health >= 0 and user_health <= 0:
            print("The monster has killed you. Better luck next time!")
            break
#If any other person has health, restart loop
        else:
            continue

#call function in order to play again
    continue_play()


          
def continue_play():

    play_again = input("Would you like to play again? Y/N: ")

    if play_again == 'Y':
        main()
    else:
        print("GG!")


main()

    
