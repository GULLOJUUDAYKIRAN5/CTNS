class order:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __gt__(self,a2):
        if self.a+self.b>a2.a+a2.b:
            return True
        else:
            return False

o1=order(5,50)
o2=order(6,60)
print(o1>o2)
