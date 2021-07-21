"""
BASIC CALCULATOR

This app is a basic calculator that runs in the terminal. It will continue to run unless it has been specified to quit.

The goal of this was for me to learn more about functions, *args, while loop, for loop, and etc.
"""
def addition(numbers):
    sum_of_num = 0
    for i in numbers:
        sum_of_num += float(i)
    return sum_of_num


def subtraction(numbers):
    numbers = list(numbers)
    difference = float(numbers[0])
    numbers.pop(0)
    for (i) in numbers:
        difference -= int(i)
    return difference


def multiplication(numbers):
    product = 1
    for i in numbers:
        product *= float(i)
    return product


def division(numbers):
    numbers = list(numbers)
    quotient = int(numbers[0])
    numbers.pop(0)
    for i in numbers:
        quotient /= float(i)
    return format(quotient, ".3f")


print("\n---Welcome to basic calculator! Enter the appropriate letter to do basic calculations---")
letter = ''
while letter.upper() != 'Q':
    print("\n| A for addition |\n| S for subtraction |\n| M for multiplication |\n| D for division |\n| Q for quit |")
    letter = input("Letter of choice: ").upper().strip()
    if letter == 'Q':
        break
    elif (letter != 'A') and (letter != 'S') and (letter != 'M') and (letter != 'D'):
        print("\nYou didn't enter the correct letter. Try again.")
        continue
    numbers = tuple(input("Enter numbers (add a space between each number): ").split())

    if letter.upper() == 'A':
        answer = addition(numbers)
    elif letter.upper() == 'S':
        answer = subtraction(numbers)
    elif letter.upper() == 'M':
        answer = multiplication(numbers)
    elif letter.upper() == 'D':
        answer = division(numbers)

    print("\n# The answer is: {} #".format(answer))
