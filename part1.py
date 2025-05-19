#build two functions for discounting products on a website. be able to use both
#student Discount: discount current price by 10%
#regular buyers discount: discounts additional 5% on current student discounted price
from importlib.util import source_hash


def StudentDiscount(currentPrice):
    newPrice = 0 + float(currentPrice)
    newPrice -= float(currentPrice) * 0.10
    return newPrice

def RegularDiscount(currentPrice):
    newPrice = 0 + float(currentPrice)
    newPrice -= float(currentPrice) * 0.05
    return newPrice


student = input("Are You a student? (y/n): ")
regular = input("would you like the regular discount?: (y/n)")
currentCost = input("Please enter the current total: $")

if student == 'y' or student == 'Y':
    currentCost = StudentDiscount(currentCost)

if regular == 'y' or regular == 'Y':
    currentCost = RegularDiscount(currentCost)

print("You're cost is: " + '${:,.2f}'.format(currentCost))