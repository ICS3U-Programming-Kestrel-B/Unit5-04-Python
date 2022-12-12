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
    # initializing error_check
    error_check = "No error"
    try:
        # checking to see if first_num is a float
        first_num_float = float(first_num)

        try:
            # checking to see if second_num is a float
            second_num_float = float(second_num)

            if user_sign == "+":
                answer = first_num_float + second_num_float
                complete_string = first_num + " + " + second_num + " = " + answer
                return complete_string
            elif user_sign == "-":
                answer = first_num_float - second_num_float
                complete_string = first_num + " - " + second_num + " = " + answer
                return complete_string
            elif user_sign == "/":
                answer = first_num_float / second_num_float
                complete_string = first_num + " / " + second_num + " = " + answer
                return complete_string
            elif user_sign == "*":
                multiplication_answer = first_num_float * second_num_float
                complete_string = first_num + " * " + second_num + " = " + multiplication_answer
                return complete_string
            else:
                complete_string = "Sign error"
                return complete_string


        except ValueError:
            # string message
            print("\n")
            print("Please enter a valid second number.")
        finally:
            print("\n")
    except ValueError:
        # string message
        print("\n")
        print("Please enter a valid first number.")
    finally:
        print("\n")

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
    calculated = calculate(user_sign, first_num, second_num)
    # calculate(user_sign, first_num, second_num)

    # checking if input is valid
    if calculated != "Sign error":
        # displaying to user
        print(calculated)
    else:
        # error message
        print("Please enter a valid sign.")


if __name__ == "__main__":
    main()
