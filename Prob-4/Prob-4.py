# Module 3
#   Programming Assignment 4
#     Prob-4.py

# Ilya Panasevich

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""

def coffeeProcessor():

    # define variables
    overHead = 1.25
    priceOfCoffee = 16.50

    # get number of pounds from user
    # added a quatation mark to fix the input line below.
    # changed evaluate to eval()
    # added \n to make it easier to see the number you type
    quantity = eval(input("How many pounds of coffee would you like to order?\n"))
    
    # Check number of pounds ordered
    # If less than or equal to 10 pounds we must charge for shipping
    if quantity <= 10:
        shippingPerPound = .76
    else:
        shippingPerPound = 0      

    # Calculate cost of order
    # changed quntity to quantity
    costOfOrder = (quantity * priceOfCoffee) + (quantity * shippingPerPound) + overHead

    # Print result
    # added a quotation mark to the beginning of the print statement
    print("The cost of the order is:", costOfOrder)

# start the program
# removed go from gocoffeeProcessor

coffeeProcessor()