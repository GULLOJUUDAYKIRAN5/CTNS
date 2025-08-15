class student:
    name="uday"
    def __init__(self,name,no):
        self.name=name
        self.no=no
        student.name=name
        self.__class__.name="uday"
    @classmethod
    def namechange(cls,name):
        cls.name=name

s1=student("kiran",1)
s1.namechange("uday")
print(s1.name)
print(student.name)
