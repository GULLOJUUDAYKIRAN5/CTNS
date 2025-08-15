class student:
    def __init__(self):
       self.m1=int(input("enter hte mrks"))
       self.m2=int(input("enter the marks"))
       self.m3=int(input("enter the marks"))
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
s1=student()
s2=student()
print(s1.get_m1())
s1.set_m1(15)
print(s1.get_m1())

print(s1.avg())
print(s2.avg())
