class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownum(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        print(newreal,"i+",newimg,"j")
        #return (newreal,newimg)
    def __sub__(self,num2):
        re=num2.real-self.real
        im=num2.img-self.img
        print(re,"i+",im,"j")
num1=complex(1,5)
num1.shownum()
num2=complex(2,6)
num1+num2
num1-num2
num3,num4=num1.adding(num2)
print(num3,"i+",num4,"j")

