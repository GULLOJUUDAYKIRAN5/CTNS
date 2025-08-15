class computer:
    def __init__(self,core,ram):
        self.core=core
        self.ram=ram


    def config(self):
        print(f'the config is {self.core} and {self.ram}')

comp1=computer('i5',16)
comp2=computer('ryzen',8)

computer.config(comp1)
comp2.config()
