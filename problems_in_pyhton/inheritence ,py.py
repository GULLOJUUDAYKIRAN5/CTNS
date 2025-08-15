class a:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b,"form a")
    def feature1(self):
        print(self.a)
class b(a):
    
    def __init__(self,c,d):
        self.c=c
        self.d=d
        super().__init__(5,6)
        print(self.c,self.d,"from b")
    def feature2(self):
        print(self.c)
        print
class c(b):
    def __init__(self):
        print("this is c")
        super().__init__(9,8)
b1=b(3,4)
a1=a(1,2)
c1=c()
b1.feature1()

    
            
