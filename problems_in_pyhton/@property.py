class student:
    def __init__(self,m,c,p):
        self.m=m
        self.c=c
        self.p=p
        self.percent=(self.m+self.p+self.c)/3
    def percentage(self):
        print((self.m+self.p+self.c)/3)
    @property
    def pre(self):
        return (self.m+self.p+self.c)/3
s1=student(100,100,100)
print(s1.percent)
s1.percentage()
s1.p=90
s1.percentage()
#even tho we changed the p values it is showing again the previous values
print(s1.percent)
print(s1.pre)
