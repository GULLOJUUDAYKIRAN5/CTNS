class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def welcome(self):
        print("welcome to the class",self.name,"age is",self.age)
s1=student("uday",15)
s1.welcome()
s2=student("kiran",19)
s2.welcome()
