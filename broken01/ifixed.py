#!/usr/bin/env python3


# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.


calc1 = 0.0
calc2 = 0.0
operation = ""
while calc1 != "q":
    calc1 = input("What is the first operator? Or, enter q to quit:\n ")
    if calc1.lower() == "q":
        break
    calc1 = float(calc1)
    calc2 = input("What is the second operator? Or, enter q to quit:\n ")
    if calc2.lower() == "q":
        break
    calc2 = float(calc2)
    operation = input("Enter an operation to perform on the two operators (+ or -): ")
    if operation == "+":
        print("\n" , float(calc1) , " + ", + float(calc2) , " = ", float(calc1 + calc2))
    elif operation == '-':
        print("\n" , float(calc1) , " - " , float(calc2) , " = " , float(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
