class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
    def per(self):
        return 2*3.14*self.r

c1=circle(5)
print(c1.area())
print(c1.per())
