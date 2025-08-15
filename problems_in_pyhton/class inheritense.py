class a:
    def __init__(self,name,cno):
        self.name=name
        self.cno=cno
    def hello(self):
        print("this car is mine",self.name)
        self.__hi()
    def __hi(self):
        print("this is my car no",self.cno)
c1=a("bmw",123)
class b(a):
    c1.hello()
    #this below one will not work because it is an private method
  # c1.__hi()
    
    
