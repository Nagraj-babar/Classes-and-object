'''Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values'''
class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
        print('empid=',self.empid,'name=',self.name,'salary=',self.salary)
e1=int(input('please enter your employee id here >> '))
n1=input('please enter your name here >> ')
s1=int(input('please enter your salary here >> '))
obj1=Employee(e1,n1,s1)
