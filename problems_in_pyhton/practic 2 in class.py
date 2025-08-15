class account:
    #this staticmethos is used to create a method without self
    @staticmethod
    def hello():
        print("this is your bank")
    def __init__(self,balance,accno):
        self.bal=balance
        self.accno=accno
    def debit(self,amount):
        self.bal=self.bal-amount
        print("this much of amount ",amount,"is debited")
        print("the remaining balance is",self.bal) 
    def creadit(self,amount):
        self.bal+=amount
        print("this much of amount ",amount,"is creadited")
        print("the remaining balance is",self.bal) 
    def balance(self):
        print("the remaining balance is",self.bal)
a1=account(1000,10)
a1.hello()
a1.debit(500)
a1.creadit(700)
a1.balance()
