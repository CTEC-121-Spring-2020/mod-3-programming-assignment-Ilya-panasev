# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Ilya Panasevich

"""
Input: person's name, person's hourly wage, and person's hours
Processes: calculate normal pay and time and half pay, calculate tax withholding,
calculate medical insurance withholding, calculate total take home pay.
Output: Display employee's name, regular wage, overtime wage, total wage,
tax withholding, insurance withholding, and take home pay.  
"""

def main():
    # inputs
    empName = input("Please type your full name:")
    empWage = eval(input("Please type your hourly wage (don't use $, decimals are fine):"))
    empHours = eval(input("Please type your total work hours:"))
    
    # two-way
    if empHours > 40:
        RegularWage = 40 * empWage
        OvertimeWage = (empHours - 40) * 1.5 * empWage
    else:
        RegularWage = empHours * empWage
        OvertimeWage = 0
    
    TotalWage = RegularWage + OvertimeWage
    TaxWithholding = TotalWage * 0.20
    InsurWithholding = TotalWage * 0.10
    TakeHome = TotalWage - TaxWithholding - InsurWithholding

    # outputs
    print("\nYour name:", empName)
    print("Your regular wage:", RegularWage)
    print("Your overtime wage:", OvertimeWage)
    print("Your total wage (regular plus overtime wage):", TotalWage)
    print("Taxes withheld from your wage:", TaxWithholding)
    print("Insurance cost withheld from your wage:", InsurWithholding)
    print("Your total take home pay (total wage minus taxes and insurance):", TakeHome, "\n")

main()