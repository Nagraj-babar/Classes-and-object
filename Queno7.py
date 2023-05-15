'''Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).'''
class Laptop:
    def __init__(self):
        self.brand='DELL (Alienware)'
        self.ram= 16
        self.cpu='i9'
        self.hdd='1 Tb'
        #self.showConfig()
    def showConfig(self):
        print('Brand= ',self.brand)
        print('Ram= ',self.ram)
        print('CPU= ',self.cpu)
        print('HDD= ',self.hdd)
obj1=Laptop()
obj1.showConfig()