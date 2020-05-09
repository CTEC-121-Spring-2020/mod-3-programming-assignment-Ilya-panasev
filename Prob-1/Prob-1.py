# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Ilya Panasevich

"""
Input: order sub total
Processes: if the order subtotal is greater than or equal to 10 then
shipping cost will be deducted down to 0. If it is less than 10 then 
the shipping cost will remain 2.99.
Output: shipping cost
"""

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    if orderSubTotal >= 10.00:
        shippingCost = 0.0

    return shippingCost

def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    print("Shipping cost if subtotal > 10.00:\t", shippingCost(11.99))


if __name__ == "__main__":
    unitTest()
