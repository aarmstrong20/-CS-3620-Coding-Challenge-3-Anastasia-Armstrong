# create an obj oriented superclass name computer with two subclasses named:
#   Desktop -> one specification exclusive: case style
#       get_data
#       display
#   Laptop -> one specification exlcusive: weight
#       get_data
#       display
#define 2 methods in computer named
#   getspecs -> get specifications
#   displayspecs -> display specification
import os


class Computer:
    def __init__(self, name, price, CPU):
        self.name = name
        self.price = price
        self.CPU = CPU
    def get_data(self):
        self.name = input("Computer Name: " )
        self.price = input("Computer price: $")
        self.CPU = input("Computer CPU: " )
    def display_specs(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("CPU: ", self.CPU)




class Laptop(Computer):
    def add_laptop(self, name, price, CPU,  weight):
        super().__init__( name, price, CPU)
        self.weight = weight
    def get_laptop(self):
        super().get_data()
        self.weight = input("Laptop weight: ")
    def display_laptop_specs(self):
        super().display_specs()
        print("Weight: ", self.weight)

class Desktop(Computer):
    def add_desktop(self, name, price, CPU,  caseStyle):
        super().__init__( name, price, CPU)
        self.caseStyle = caseStyle
    def get_desktop(self):
        super().get_data()
        self.caseStyle = input("Case Style: ")
    def display_desktop_specs(self):
        super().display_specs()
        print("Case Style: ", self.caseStyle)



laptop1 = Laptop("","","")
desktop1 = Desktop("","", "")
print("Laptop")
laptop1.get_laptop()
print("Desktop")
desktop1.get_desktop()
laptop1.display_laptop_specs()
desktop1.display_desktop_specs()