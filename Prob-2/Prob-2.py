# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Brandon Norton

# Input: Enter a price of item, and amount of money given
# Process: calculate total change, and the number of tens, fives, ones, quarters, dimes, nickels, and pennies recieved as change
# Ourtput: String showing cost of item, total change, money given, and each denomination of dollar bills and quarters given as change starting from 10$ in terminal
# function definition


# main function definition


def main():

    cost = 5.99
    print("Cost of item: $", cost)
    moneyGiven = 12.72
    print("Money given: $", moneyGiven)
    change = moneyGiven - cost
    print("Change: $", change)

    totalChange = int(round(change * 100))
    print("Total Change:",totalChange // 100)
    
    #tens
    ten = totalChange // 1000
    if ten >= 1:
        print("Number of Tens:",ten)

    totalChange = totalChange - (ten * 1000)
    
    #Fives
    five = totalChange // 500
    if five >= 1:
        print("Number of Fives:",five)

    totalChange = totalChange - (five * 500)
    

    #ones
    one = totalChange // 100
    if one >= 1:
        print("Number of Ones:",one)
    
    totalChange = totalChange - (one * 100)
    

    #quarters
    quarter = totalChange // 25
    if quarter >= 1:
        print("Number of quarters:", quarter)
    
    totalChange = totalChange - (quarter * 25)

    #Dimes
    dime = totalChange // 10
    if dime >= 1:
        print("Number of dimes:", dime)

    totalChange = totalChange - (dime * 10)

    #nickels
    nickel = totalChange // 5
    if nickel >= 1:
        print("Number of nickels:", nickel)

    totalChange = totalChange - (nickel * 5)

    #pennies
    penny = totalChange // 1
    if penny >= 1:
        print("number of pennies:", penny)

        



main()
