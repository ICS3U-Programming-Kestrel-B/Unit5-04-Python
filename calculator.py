#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 6, 2022
# This program asks for an
# operating symbol, a first
# number and a second number,
# then does the operation

import math

# making calculate function
def calculate(user_sign, first_num, second_num):
    # initializing answer
    answer = 0
    try:
        # checking to see if first_num is a float
        first_num_float = float(first_num)

        try:
            # checking to see if second_num is a float
            second_num_float = float(second_num)

            # checking to see what calculation to do
            if user_sign == "+":
                answer = first_num_float + second_num_float
            elif user_sign == "-":
                answer = first_num_float - second_num_float
            elif user_sign == "/":
                answer = first_num_float / second_num_float
            elif user_sign == "*":
                answer = first_num_float * second_num_float
            else:
                answer = "Sign error"

        except ValueError:
            # string message
            print("\n")
            print("Please enter a valid second number.")
        # finally:
        # print("\n")
    except ValueError:
        # string message
        print("\n")
        print("Please enter a valid first number.")
    # finally:
    # print("\n")

    return answer


def main():
    # introductory paragraph
    print("This program asks for an")
    print("operating symbol, a first")
    print("number and a second number,")
    print("then does the operation")
    print("")

    # getting user input
    # initializing user_mark
    user_sign = input("Enter an operation (+, -, /, *): ")

    # initializing first_num
    first_num = input("Enter your first number: ")

    # initializing second_num
    second_num = input("Enter your second number: ")

    # calling function
    answer = calculate(user_sign, first_num, second_num)
    if answer != "Sign error":
        # displaying the calculation
        print("{} {} {} = {}".format(first_num, user_sign, second_num, answer))
    else:
        # sign error message
        print("Please enter a valid sign")


if __name__ == "__main__":
    main()
