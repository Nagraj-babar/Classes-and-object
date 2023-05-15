# create 3 Laptop objects and add them to the list in the sorted order based on the ram size.
class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    def __lt__(self,other):
        return self.ram < other.ram
    def sort(self):
        return [self.brand,self.ram,self.cpu,self.hdd]
obj1=Laptop('dell',18,'i9','1tb')
obj2=Laptop('lenovo',12,'i7','1tb')
obj3=Laptop('hp',8,'i7','1Tb')
l1=[]
if obj1<obj2 and obj1<obj3:
    if obj2<obj3:
       l1.append(obj1.sort()),l1.append(obj2.sort()),l1.append(obj3.sort())
    else:
       l1.append(obj1.sort()),l1.append(obj3.sort()),l1.append(obj2.sort())
elif obj2<obj1 and obj2<obj3:
    if obj1<obj3:
        l1.append(obj2.sort()),l1.append(obj1.sort()),l1.append(obj3.sort())
    else:
        l1.append(obj2.sort()),l1.append(obj3.sort()),l1.append(obj1.sort())
elif obj3<obj1 and obj3<obj2:
    if obj2<obj1:
        l1.append(obj3.sort()),l1.append(obj2.sort()),l1.append(obj1.sort())
    else:
        l1.append(obj3.sort()),l1.append(obj1.sort()),l1.append(obj2.sort())
print(l1)



    



