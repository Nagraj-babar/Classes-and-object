# Write a python program to init default values for user object using __init__ method.
class user:
    def __init__(self,name='nagraj',age=24):
        self.name=name
        self.age=age
        print('name:',self.name,'Age: ',self.age)
u1=user(name='NAGRAJ',age=23)
u2=user()
