class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __gt__(self,other):
        if(self.m1+self.m2>other.m1+other.m2):
            return True
        else:
            return False


s1=student(10,20)
s2=student(20,30)
if s1>s2:
    print(s1.m1, "is big")
else:
    print(s2,"is bigger")
