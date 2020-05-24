# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Brandon Norton

# Input: Square feet of wall space, cost of gallons of paint
# process: calculate estimate of hours and cost of job
# Output: Prints estimate of hours, and cost of job

# function definition

from math import *

# main function definition
def estimate(squareFeet, costofPaint):
   hours =ceil((squareFeet / 112) * 8)
   gallons = ceil((squareFeet / 112) * 1)
   print("Hours of labor required:", hours, "hours")
   print("Gallons of paint needed:", gallons, "gallons")
   print("Square feet of job:", squareFeet, "square feet")
   print("Cost of paint per gallon: $",costofPaint)
   costofLabor = hours * 35.00
   print("Labor costs: $", costofLabor)
   paintCost = gallons * costofPaint
   print("Total cost of paint $", paintCost)
   totalCost = costofLabor + paintCost + 99.00
   print("Setup fee: $99")
   print("Total cost of job: $", totalCost)
   

    


def main():

    squareFeet = eval(input("Please input number of square feet for job: "))
    costofPaint = eval(input("Please input cost of paint: "))
    print()

    estimate(squareFeet, costofPaint)
    '''
    print("Test 1")
    estimate(300, 10)
    print()
    print("Test 2")
    estimate(562, 28.50)
    '''
    
main()
