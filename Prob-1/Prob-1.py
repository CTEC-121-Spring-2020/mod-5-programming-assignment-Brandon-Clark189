# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Brandon Norotn

# Input, enter number between 1-10
# Process, Convert number to roman numeral
# Output String showing that converted roman numeral and the original input to terminal

# function definition

# unit test function
def romanNumeral(number):
    if number == 1:
        return "I"
    elif number == 2:
        return "II"
    elif number == 3:
        return "III"
    elif number == 4:
        return "IV"
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 7:
        return "VII"
    elif number == 8:
        return "VIII"
    elif number == 9:
        return "IX"
    elif number == 10:
        return "X"
    else: 
        return "Input outside valid range"




def unitTest():
    print("\nUnit Tests")
    
    print("number inputted: 1\tRoman nurmeral:", romanNumeral(1))
    print("number inputted: 2\tRoman nurmeral:", romanNumeral(2))
    print("number inputted: 3\tRoman nurmeral:", romanNumeral(3))
    print("number inputted: 4\tRoman nurmeral:", romanNumeral(4))
    print("number inputted: 5\tRoman nurmeral:", romanNumeral(5))
    print("number inputted: 6\tRoman nurmeral:", romanNumeral(6))
    print("number inputted: 7\tRoman nurmeral:", romanNumeral(7))
    print("number inputted: 8\tRoman nurmeral:", romanNumeral(8))
    print("number inputted: 9\tRoman nurmeral:", romanNumeral(9))
    print("number inputted: 10\tRoman nurmeral:", romanNumeral(10))
    print("number inputted: 11\tRoman nurmeral:", romanNumeral(11))
    print()

 
unitTest()
