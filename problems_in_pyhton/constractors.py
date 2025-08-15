class computer:
    def __init__(self):
        self.name="uday"
        self.no=99
    def update(self):
        self.age=100
        self.name="maheshwari"
    def compare(self,c2):
        if(self.age==c2.no):
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.update()
if c1.compare(c2):
     print("they  are equal")
else:
    print("they are not equal")

print(c1.name,c1.age)
print(c2.name,c2.no)

