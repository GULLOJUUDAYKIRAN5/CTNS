class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("the avg of",self.name,"is",sum/3)
s1=student("uday",[10,10,10])
s1.avg()
s1.name="naveen"
#we can also change the data values like above when ever we want
s1.avg()
