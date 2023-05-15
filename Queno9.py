# Write a python program to create a School class and 3 instance variables and 1 class variable.
class school:
    schname='New English School Satara'  # class variable
    def __init__(self):                     # instance method is used to creat instance variable
     self.name='Nagraj babar'
     print(school.schname,self.name,sep='\n')
obj1=school()
#print(obj1.schname)


