# Write a python program to create 2 objects of the user class and assign different values.
class user:
    def __init__(self):
        self.cpu='i9'
        self.ram=16
u1=user()
u2=user()
print(u1.cpu)
print(u1.ram)
u2.cpu='i7'
u2.ram=12
print(u2.cpu)
print(u2.ram)