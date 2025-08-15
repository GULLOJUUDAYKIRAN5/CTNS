class Addtion:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        x=(self.a+self.b)+(other.a+other.b)
        return x
a1=Addtion(3,4)
a2=Addtion(4,5)
print(a1+a2)








