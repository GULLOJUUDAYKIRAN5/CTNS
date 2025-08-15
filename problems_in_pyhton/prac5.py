class emp:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showdet(self):
        print(self.role,self.dept,self.sal)
class eng(emp):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("stud","cse",0)
e1=emp("acc","finanac",3000)
e1.showdet()
en1=eng("uday",19)
en1.showdet()
