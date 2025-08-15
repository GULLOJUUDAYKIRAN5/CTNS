class a:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def details(self,name):
        print(f'my name is {name}')
        print(f'my age is {self.age}')
#by using inheritence we are using the details method  from a
class b(a):
    def __init__(self,name,age):
        self.name=name
        self.age=age

a1=a("uday",5)
a2=a("kiran",7)
a1.details("naveen")
b1=b("prince",10)
b1.details("ravi")
