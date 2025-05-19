##storeList = a dictionary of all items and prices in store
## discount = function to discount price by 10%

def discount(list):
    for key, value in list.items():
       list[key] += value * 0.10

storeList = {
    'shirt' : 12.00,
    'pants' : 20.00,
    'jacket' : 30.00,
    'hat' : 6.00
}

print(storeList)
discount(storeList)
print(storeList)