class student:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print(self.name)
s1=student("udya")
s1.hello()
del s1.name
print(s1.name)
