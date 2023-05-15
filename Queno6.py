# Write a python program to create 3 user objects and find the youngest of all.
class Age:
    def __init__(self,age):
        self.age=age
    def __gt__(self,other):
        return self.age > other.age
b1=int(input('Enter the age of first object: '))
b2=int(input('Enter the age of secound object: '))
b3=int(input('Enter the age of third object: '))
obj1=Age(b1)
obj2=Age(b2)
obj3=Age(b3)
if obj1>obj2 and obj1>obj3:
    print('Youngest object is first which is: ',obj1.age)
elif obj2>obj1 and obj2>obj3:
    print('Youngest object is secound which is: ',obj2.age)
elif obj3>obj1 and obj3>obj2:
    print('Youngest object is third which is: ',obj3.age)
else:
    print('All objectes have equal age')