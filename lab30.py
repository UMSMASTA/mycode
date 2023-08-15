#!/usr/bin/env python3

import html


trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():

    question= trivia["question"]
    correct= trivia["correct_answer"]
    incorrect1= trivia["incorrect_answers"][0]
    incorrect2= trivia["incorrect_answers"][1]
    incorrect3= trivia["incorrect_answers"][2]

    print("Here is your trivia question!\n")
    print(question)

    print('A:', html.unescape(correct))
    print('B:', html.unescape(incorrect1))
    print('C:', html.unescape(incorrect2))
    print('D:' ,html.unescape(incorrect3))
    
    user_input = input('Make your choice: ')

    case_input = user_input.lower()

    if case_input == "a":
        print("Correct")
    elif case_input == "b":
        print("B is not the correct answer.")
    elif case_input == "c":
        print("C is not the correct answer")
    elif case_input == "d":
        print("D is not the correct answer.")

while True:
    main()
    try_again = input('Would you like to play again? Y/N: ')

    if try_again == 'N':
        break

    


