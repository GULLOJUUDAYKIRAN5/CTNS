class student:
    def __init__(self,fullname,age):
        print("uday is from batch 1")
        self.name=fullname
        self.age=age

s1=student("uday",16)
print(s1.name,s1.age)
s2=student("kiran",17)
print(s2.name,s2.age)
